from _csv import reader

from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.views import generic, View
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import PermissionRequiredMixin, UserPassesTestMixin


class NewsListView(generic.ListView):
    model = News
    contexts_object_name = 'news_list'
    template_name = 'app_news/news_list.html'

    def get_queryset(self):
        model = super(NewsListView, self).get_queryset()
        ordering_by_teg = self.request.GET.get('tag')
        if ordering_by_teg:
            return News.objects.filter(tag=Tegs.objects.get(name=ordering_by_teg))
        return News.objects.all()

    def get_context_data(self, **kwargs):
        data = super(NewsListView, self).get_context_data(**kwargs)
        data['tegs'] = Tegs.objects.all()
        return data


class NewsCreateView(PermissionRequiredMixin, generic.CreateView):
    model = News
    template_name = 'app_news/create_news.html'
    permission_required = ('app_news.add_news', )
    fields = ('text', 'tag',)

    def handle_no_permission(self):
        return render(self.request, 'app_news/create_news_access_restricted.html', {})

    def form_valid(self, form):
        new_object = form.save()
        new_object.user = self.request.user
        for item in self.request.FILES.getlist('gallery'):
            Gallery.objects.create(img=item, news=new_object)
        return super().form_valid(form)


class NewsUpdateView(UserPassesTestMixin, UpdateView):
    model = News
    template_name = 'app_news/edit.html'
    fields = ['text']

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
        data['blog_pic'] = Gallery.objects.filter(news=self.get_object())
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


def csv_download(request):
    if request.method == 'POST':
        upload_file_form = CSVForm(request.POST, request.FILES)
        if upload_file_form.is_valid():
            file = upload_file_form.cleaned_data['file'].read()
            text = file.decode('utf-8').split('\n')
            user = request.user
            csv_reader = reader(text, delimiter=',', quotechar='"')
            for item in csv_reader:
                News.objects.create(text=item[0], user=user, tag=None, )
            return HttpResponse(content='Записи успешно добавлены', status=200)
    else:
        upload_file_form = CSVForm()

        context = {'form': upload_file_form}
        return render(request, 'app_news/csv_upload.html', context=context)
