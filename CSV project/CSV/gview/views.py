from gview.models import Person,Birthdate,Genre,Identification

from django.views import View
from django.shortcuts import render

# Create your views here.

class PersonListView(View):
    