from django.core.management.base import BaseCommand, CommandError
from mainapp.models import Work, Hobby, Education, Organization, Person
import json
import os.path

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class Command(BaseCommand):
    help = 'Provides an initial loading data to database'

    def handle(self, *args, **options):
        path = os.path.join(BASE_DIR, 'files', 'Education.json')
        Education.objects.all().delete()
        with open(path, 'r') as file:
            json_list = json.load(file)
            for item in json_list:
                edu = Education(**item)
                edu.save()

        Hobby.objects.all().delete()
        path = os.path.join(BASE_DIR, 'files', 'Hobby.json')
        with open(path, 'r') as file:
            json_list = json.load(file)
            for item in json_list:
                hobby = Hobby(**item)
                hobby.save()

        Organization.objects.all().delete()
        path = os.path.join(BASE_DIR, 'files', 'Organization.json')
        with open(path, 'r') as file:
            json_list = json.load(file)
            for item in json_list:
                organization = Organization(**item)
                organization.save()

        Person.objects.all().delete()
        path = os.path.join(BASE_DIR, 'files', 'Person.json')
        with open(path, 'r') as file:
            json_obj = json.load(file)
            person = Person(**json_obj)
            person.save()

        Work.objects.all().delete()
        path = os.path.join(BASE_DIR, 'files', 'Work.json')
        with open(path, 'r') as file:
            json_list = json.load(file)
            for work in json_list:
                org_name = work["organization"]
                organization = Organization.objects.get(name=org_name)
                work["organization"] = organization
                work = Work(**work)
                work.save()



