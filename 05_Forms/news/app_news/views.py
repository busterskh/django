from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render
from app_news.forms import *
from app_news.models import *
from django.views import generic, View


class NewsListView(generic.ListView):
    model = News
    contexts_object_name = 'news_list'


class NewsFormView(View):
    def get(self, request):
        news_form = NewsForm()

        return render(request, 'app_news/create_news.html', context={'news_form': news_form})

    def post(self, request):
        news_form = NewsForm(request.POST)

        if news_form.is_valid():

            News.objects.create(**news_form.cleaned_data)
            return HttpResponseRedirect('/all_news/')

        return render(request, 'app_news/create_news.html', context={'news_form': news_form})


class NewsEditFormView(View):

    def get(self, request, news_id):
        news = News.objects.get(id=news_id)
        news_form = NewsForm(instance=news)
        return render(request, 'app_news/edit.html', context={'news_form': news_form, 'news_id': news_id})

    def post(self, request, news_id):
        news = News.objects.get(id=news_id)
        news_form = NewsForm(request.POST, instance=news)

        if news_form.is_valid():
            news.save()
            return HttpResponseRedirect(f'/all_news/{news_id}')
        return render(request, 'app_news/edit.html', context={'news_form': news_form, 'news_id': news_id})


class NewsDetailView(generic.DetailView):
    model = News
    context_object_name = 'news_object'

    def get_context_data(self, **kwargs):
        data = super(NewsDetailView, self).get_context_data(**kwargs)
        data['comments_list'] = Comment.objects.filter(news_id=self.kwargs.get(self.pk_url_kwarg, None))
        data['comments_form'] = CommentForm()
        return data

    def post(self, request, pk):
        comment_form = CommentForm(request.POST)

        if comment_form.is_valid():
            Comment.objects.create(**comment_form.cleaned_data, news_id=pk)
            return HttpResponseRedirect(f'/all_news/{pk}/')
        return render(request, 'app_news/news_detail.html', context={'comment_form': comment_form, 'news_id': pk, })
