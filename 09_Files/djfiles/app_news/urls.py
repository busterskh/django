from django.urls import path
from app_news.views import *
from app_users.views import *

urlpatterns = [
    path('', MainPage.as_view(), name='main_page'),
    path('all_news/', NewsListView.as_view(), name='all_news'),
    path('create_news/', NewsCreateView.as_view(), name='create_news'),
    path('all_news/<int:pk>/edit/', NewsUpdateView.as_view(), name='edit'),
    path('all_news/<int:pk>/', NewsDetailView.as_view(), name='news-detail'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('registration/', ProfileCreate.as_view(), name='registration'),
    path('user/<int:pk>/', ProfileDetailView.as_view(), name='profile'),
    # path('user/<int:pk>/edit_profile/', update_form, name='edit_profile'),
    path('create_news_csv/', csv_download, name='create_news_csv'),
    path('user/<int:pk>/edit_profile1/', UpdateProfile.as_view(), name='edit_profile'),

]
