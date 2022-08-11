from django import forms
from app_news.models import *


class NewsForm(forms.ModelForm):

    class Meta:
        model = News
        fields = '__all__'


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        exclude = ('news_id', )
