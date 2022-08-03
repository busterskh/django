from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

count_post = 0
advertisements = [
        'Мастер на час',
        'Выведение из запоя',
        'Услуги экскаватора-погрузчика, гидромолота, ямобура',
        'Агенство недвижимости. Покупка/Продажа',
        'Продам машину'
    ]
regions = ['Харьков', 'Киев', 'Днепр', 'Одесса']


class Home(View):
    def get(self, request):
        global advertisements
        return render(request, 'advertisements_app/home.html', {'advertisements_app': advertisements,
                                                            'regions': regions})

    def post(self, request):
        global advertisements
        return render(request, 'advertisements_app/adver.html', {'advertisements_app': advertisements})


class Advertisements(View):
    def get(self, request):
        global regions
        return render(request, 'advertisements_app/adver.html', {'advertisements_app': advertisements})

    def post(self, request):
        global count_post
        count_post += 1
        return render(request, 'advertisements_app/successful.html', {'count_post': count_post})


class Contacts(TemplateView):
    template_name = 'advertisements_app/contacts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["name"] = 'Наши контакты:'
        context["title"] = 'Контакты'
        context["address"] = "London Stack Overflow Ltd. Bentima House 168-172 Old Street London, EC1V 9BP"
        context["phone"] = "+44 800 048 8989"
        context["email"] = "legal@stackoverflow.com"

        return context


class About(TemplateView):
    template_name = 'advertisements_app/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["name"] = 'О компании'
        context["title"] = 'О компании'
        context["description"] = "Empowering the world to develop technology through collective knowledge." \
                                 "Our public platform serves 100 million people every month, making it one of" \
                                 " the most popular websites in the world.Our asynchronous knowledge management" \
                                 " and collaboration offering, Stack Overflow for Teams," \
                                 " is transforming how people work."
        return context

