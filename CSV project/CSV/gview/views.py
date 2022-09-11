from re import template
from unittest import result
from gview.models import Person

from django.views import View
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.contrib import messages

# Create your views here.
def main(request):
    context={}

    if request.method == 'POST':
        uploaded_file = request.FILES['load']

        if uploaded_file.name.endswith('.csv'):
            #save the file in data folder
            savefile = FileSystemStorage()

            name = savefile.save(uploaded_file.name, uploaded_file)
            #know where to save the file
            d = os.getcwd() #current directory of the project
            file_directory = d+'\data\\'+name
            return redirect(results)
        else:
            messages.warning(request, 'File was not uploaded. Please use csv file')
    
    return render(request, 'main.html')

def results(request):
    return render(request, 'results.html')

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
    