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
    person = Person(name='Островский Василий', text='Здравствуйте! Эта персональная страница была разработана мной в рамках учебного курса Django. Меня зовут Островский Василий Александрович. Я родился в Москве, заниматься программированим начал в школе и продолжаю до сих пор. В настоящее время изучаю основы веб-разработки с использованием Python 3.6 и Django 1.10. ', birthdate=date(1980, 1, 15))
    person.save()
    return render(request, 'index.html', {'text': person.text, 'name': person.name, 'birthdate': person.birthdate})


def job(request):
    jobs_list = Work.objects.all()

    return render(request, 'job.html', {'jobs_list': jobs_list})

def edu(request):
    path = os.path.join(BASE_DIR, 'files', 'education.csv')
    Education.objects.all().delete()
    with open(path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            edu_place = line.split(';')
            edu = Education(name=edu_place[0], period=edu_place[1], spec=edu_place[2], link=edu_place[3])
            edu.save()
    edu_list = Education.objects.all()
    return render(request, 'edu.html', {'edu_list': edu_list})

def hobby(request):
    path = os.path.join(BASE_DIR, 'files', 'hobby.csv')
    Hobby.objects.all().delete()
    with open(path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            hobbies = line.split(';')
            print(hobbies)
            hobby = Hobby(name=hobbies[0], img=hobbies[1])
            hobby.save()
    hobby_list = Hobby.objects.all()
    return render(request, 'hobby.html', {'hobbies': hobby_list})



