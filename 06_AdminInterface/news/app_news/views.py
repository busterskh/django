from django.http import HttpResponseRedirect
from django.shortcuts import render
from app_news.forms import *
from app_news.models import *
from django.views import generic
from django.views.generic.edit import UpdateView, CreateView


class NewsListView(generic.ListView):
    model = News
    contexts_object_name = 'news_list'


class NewsCreateView(CreateView):
    model = News
    template_name = 'app_news/create_news.html'
    fields = '__all__'


class NewsUpdateView(UpdateView):
    model = News
    template_name = 'app_news/edit.html'
    fields = ['title', 'text', 'is_active', ]


class NewsDetailView(generic.DetailView):
    model = News
    context_object_name = 'news_object'

    def get_context_data(self, **kwargs):
        data = super(NewsDetailView, self).get_context_data(**kwargs)
        data['comments_list'] = Comment.objects.filter(
            news_id=News.objects.get(id=self.kwargs.get(self.pk_url_kwarg, None)))
        data['comments_form'] = CommentForm()
        return data

    def post(self, request, pk):
        comment_form = CommentForm(request.POST)

        if comment_form.is_valid():
            Comment.objects.create(**comment_form.cleaned_data, news_id=News.objects.get(id=pk))
            return HttpResponseRedirect(f'/all_news/{pk}/')
        return render(request, 'app_news/news_detail.html', context={'comment_form': comment_form, 'news_id': pk, })
