from gview.models import Person

from django.views import View
from django.shortcuts import render

# Create your views here.

class idListView(View):
    def get(self, request):
        data = Person.objects.all()
        return render(request, 'testing.html', {'data': data})


    