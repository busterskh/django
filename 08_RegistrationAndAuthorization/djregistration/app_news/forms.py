from django import forms
from app_news.models import *


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment

        exclude = ('news_id', 'user', )


class CommentFormAuthenticate(forms.ModelForm):

    class Meta:
        model = Comment

        exclude = ('news_id', 'user_name', 'user')


class NewsForm(forms.ModelForm):

    class Meta:
        model = News
        exclude = ('user', 'is_active', 'tag')
