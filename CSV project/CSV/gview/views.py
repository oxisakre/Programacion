from re import template
from gview.models import Person

from django.views import View
from django.shortcuts import render

# Create your views here.
class MainView(View):
    template_name = None
    def get(self, request):
        return render(request, 'main.html')

class idListView(View):
    def get(self, request):
        data = Person.objects.all()
        return render(request, 'testing.html', {'data': data})


    