from django.urls import path
from advertisements_app.views import *

urlpatterns = [
    path('advertisements', AdvertisementListView.as_view(), name='advertisements'),
    path('category', CategoryListView.as_view(), name='category'),
    path('advertisements/<int:pk>', AdvertisementDetailView.as_view(), name='advertisements-detail'),

]
