from django.http import HttpResponse
import random
from django.views import View

elements = ['Cat', 'Car', 'House', 'Human', 'Dog', 'Horse', 'Deer', 'Forest', 'Bird', '10']


class ToDoView(View):

    def get(self, request, *args, **kwargs):
        global elements
        return HttpResponse('<ul>'
                            f'<li>{random.choice(elements)}</li>'
                            f'<li>{random.choice(elements)}</li>'
                            f'<li>{random.choice(elements)}</li>'
                            f'<li>{random.choice(elements)}</li>'
                            f'<li>{random.choice(elements)}</li>'
                            '</ul>')
