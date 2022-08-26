from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect
from django.shortcuts import render
from app_news.forms import *
from app_news.models import *
from django.views import generic, View
from django.views.generic.edit import UpdateView
from app_users.models import Profile


class NewsListView(generic.ListView):
    model = News
    contexts_object_name = 'news_list'
    queryset = News.objects.filter(is_active=True)

    def get_ordering(self):
        ordering = self.request.GET.get('orderby')
        return ordering

    def get_context_data(self, **kwargs):
        data = super(NewsListView, self).get_context_data(**kwargs)
        data['tegs'] = Tegs.objects.all()
        return data


class NewsCreateView(View):

    def get(self, request):
        if not request.user.has_perm('app_news.add_news'):
            raise PermissionDenied()
        news_form = NewsForm()
        return render(request, 'app_news/create_news.html', context={'news_form': news_form})

    def post(self, request):

        if not request.user.has_perm('app_news.add_news'):
            raise PermissionDenied()
        news_form = NewsForm(request.POST)

        if news_form.is_valid():
            News.objects.create(**news_form.cleaned_data, user=request.user)
            profile = Profile.objects.get(user=request.user)
            profile.news_count += 1
            profile.save()
            return HttpResponseRedirect('/all_news/')


class NewsUpdateView(UpdateView):
    model = News
    template_name = 'app_news/edit.html'
    fields = ['title', 'text', ]


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


