from gview.models import Person,Gender,Identification

from django.views import View
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'testing.html')

class idListView(View):
    def listview(self, request):
        information = Identification.objects.all()
        return render(request, 'testing.html', {'data': information})
    
    