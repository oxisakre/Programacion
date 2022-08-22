import csv
from unicodedata import name


# python3 manage.py runscript s_load

from gview.models import Person, Gender, Identification


def run():
    fhand = open('data/load.csv')
    reader = csv.reader(fhand)
    next(reader)  

    Person.objects.all().delete()
    Gender.objects.all().delete()
    Identification.objects.all().delete()
    

    for row in reader:
        print(row)

        p, created = Person.objects.get_or_create(name=row[0])
        g, created = Gender.objects.get_or_create(name=row[1])
        

        #r = Membership.LEARNER
        #if row[1] == 'I':
            #r = Membership.INSTRUCTOR
        #m = Membership(role=r, person=p, course=c)
        
        i = Identification(person = p, genre = g, birthdate = row[2])
        i.save()