from django.http import HttpResponse

from django.views import View


class ToDoView(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse('<ul>'
                            '<li>Установить python - сделано!</li>'
                            '<li>Установить django- сделано!</li>'
                            '<li>Запустить сервер- сделано!</li>'
                            '<li>Порадоваться результату- сделано!</li>'
                            '</ul>')
