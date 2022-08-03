from django.shortcuts import render
from advertisements_app.models import *
from django.views import generic


class AdvertisementListView(generic.ListView):
    model = Advertisement
    context_object_name = 'advertisement_list'


class CategoryListView(generic.ListView):
    model = Category
    context_object_name = 'category_list'


class AdvertisementDetailView(generic.DetailView):
    model = Advertisement

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.views += 1
        self.object.save()
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)
