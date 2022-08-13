from django.urls import path
from app_news.views import *

urlpatterns = [
    path('all_news/', NewsListView.as_view(), name='all_news'),
    path('create_news/', NewsCreateView.as_view(), name='create_news'),
    path('all_news/<int:pk>/edit/', NewsUpdateView.as_view(), name='edit'),
    path('all_news/<int:pk>/', NewsDetailView.as_view(), name='news-detail'),

]
