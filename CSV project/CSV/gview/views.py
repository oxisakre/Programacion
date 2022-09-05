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
        return render(request, 'table.html', {'data': data})

class Alphabetically(View):
    def get(self, request):
        names = Person.objects.order_by('name')
        return render(request, 'alphabetical.html', {'names': names,})

class GenderType(View):
    def get(self, request):
        male_no = Person.objects.filter(gender='M').count()
        male_no = int(male_no)
        print('Number of Male Are',male_no)

        female_no = Person.objects.filter(gender='F').count()
        female_no = int(female_no)
        print('Number of Female Are',female_no)
        
        other_no = Person.objects.filter(gender='O').count()
        other_no = int(other_no)
        print('Number of Other Are',other_no)

        gender_list = ['Male', 'Female', 'Other']
        gender_number = [male_no, female_no, other_no]
        
        counting = {'gender_list':gender_list, 'gender_number':gender_number}
        return render(request, 'gendercount.html', counting)
    