import csv
from unicodedata import name
from CSV.gview.models import Birthdate, Genre, Identification

# python3 manage.py runscript s_load

from gview.models import Person, Birthdate, Genre


def run():
    fhand = open('data/load.csv')
    reader = csv.reader(fhand)
    next(reader)  

    Person.objects.all().delete()
    Genre.objects.all().delete()
    Birthdate.objects.all().delete()
    

    for row in reader:
        print(row)

        p, created = Person.objects.get_or_create(name=row[0])
        g, created = Genre.objects.get_or_create(name=row[1])
        b, created = Birthdate.objects.get_or_create(name=row[2])

        #r = Membership.LEARNER
        #if row[1] == 'I':
            #r = Membership.INSTRUCTOR
        #m = Membership(role=r, person=p, course=c)
        
        i = Identification(person = p, genre = g, birthdate = b)
        i.save()