#coding =  utf-8
from django.shortcuts import render, render_to_response
from datetime import date
from mainapp.models import Work
from mainapp.models import Education
from mainapp.models import Person
from mainapp.models import Hobby
import os

BASE_DIR = os.path.dirname(__file__)

def main(request):
    person = Person.objects.all()[0]
    return render(request, 'index.html', {'text': person.text, 'name': person.name, 'birthdate': person.birthdate})


def job(request):
    jobs_list = Work.objects.all()
    return render(request, 'job.html', {'jobs_list': jobs_list})

def edu(request):
    edu_list = Education.objects.all()
    return render(request, 'edu.html', {'edu_list': edu_list})

def hobby(request):
    hobby_list = Hobby.objects.all()
    return render(request, 'hobby.html', {'hobbies': hobby_list})



