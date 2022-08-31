from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from app_news.forms import *
from app_news.models import *
from django.views import generic, View
from django.views.generic.edit import UpdateView
from app_users.models import Profile
from django.contrib.auth.mixins import PermissionRequiredMixin, UserPassesTestMixin


class NewsListView(generic.ListView):
    model = News
    contexts_object_name = 'news_list'
    template_name = 'app_news/news_list.html'

    def get_queryset(self):
        model = super(NewsListView, self).get_queryset()
        ordering = self.request.GET.get('orderby')

        ordering_by_teg = self.request.GET.get('tag')
        if ordering_by_teg:
            return News.objects.filter(tag=Tegs.objects.get(name=ordering_by_teg))
        elif ordering:
            return model.order_by(ordering)
        return self.ordering

    def get_context_data(self, **kwargs):
        data = super(NewsListView, self).get_context_data(**kwargs)
        data['tegs'] = Tegs.objects.all()
        return data


class NewsCreateView(PermissionRequiredMixin, generic.CreateView):
    model = News
    template_name = 'app_news/create_news.html'
    fields = ('title', 'text', 'tag', )
    permission_required = ('app_news.add_news', )

    def handle_no_permission(self):
        return render(self.request, 'app_news/create_news_access_restricted.html', {})

    def post(self, request, *args, **kwargs):
        form = self.get_form()

        if form.is_valid():
            News.objects.create(**form.cleaned_data, user=request.user)
            try:
                profile = Profile.objects.get(user=request.user)
                profile.news_count += 1
                profile.save()
            except BaseException:
                pass
            return HttpResponseRedirect('/all_news/')


class NewsUpdateView(UserPassesTestMixin, UpdateView):
    model = News
    template_name = 'app_news/edit.html'
    fields = ['title', 'text', ]

    def test_func(self):
        if self.request.user.is_superuser:
            return True
        news = self.get_object()
        return news.user == self.request.user

    def handle_no_permission(self):
        if not self.request.user.is_authenticated:
            return redirect('/login/')
        else:
            raise PermissionDenied()


class NewsDetailView(generic.DetailView):
    model = News
    context_object_name = 'news_object'

    def get_context_data(self, **kwargs):
        data = super(NewsDetailView, self).get_context_data(**kwargs)
        data['comments_list'] = Comment.objects.filter(
            news_id=News.objects.get(id=self.kwargs.get(self.pk_url_kwarg, None)))
        if self.request.user.is_authenticated:
            data['comments_form'] = CommentFormAuthenticate()
        else:
            data['comments_form'] = CommentForm()
        return data

    def post(self, request, pk):
        if self.request.user.is_authenticated:
            comment_form = CommentFormAuthenticate(request.POST)

            if comment_form.is_valid():
                Comment.objects.create(**comment_form.cleaned_data, news_id=News.objects.get(id=pk),
                                       user_name=request.user.username,
                                       user=request.user)
                return HttpResponseRedirect(f'/all_news/{pk}/')
        else:
            comment_form = CommentForm(request.POST)

            if comment_form.is_valid():
                Comment.objects.create(**comment_form.cleaned_data, news_id=News.objects.get(id=pk))
                return HttpResponseRedirect(f'/all_news/{pk}/')

        return render(request, 'app_news/news_detail.html', context={'comment_form': comment_form, 'news_id': pk, })


class MainPage(View):

    def get(self, request):
        return HttpResponseRedirect('all_news/')
