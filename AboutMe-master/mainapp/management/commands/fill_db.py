from django.core.management.base import BaseCommand
from mainapp.models import Work, Hobby, Study, Organization
from datetime import date


class Command(BaseCommand):
    help = 'Fill DB new data'

    def handle(self, *args, **options):
        organizations = [
            {'name': 'GeekBrains', 'region': 'Москва', 'tax_id': 123456, 'site': 'https://geekbrains.ru/'},
            {'name': 'ЭР-Телеком Холдинг, ЗАО', 'region': 'Пермь', 'tax_id': 666122, 'site': 'http://ertelecom.ru/t/ru/'},
            {'name': 'Прогноз, ЗАО', 'region': 'Пермь', 'tax_id': 666124, 'site': 'http://www.prognoz.ru/'},
        ]
        works = [
            {'organization': 'GeekBrains', 'position': 'Преподаватель курсов Python, Django',
             'duties': 'Проведение учебных курсов по Python, Django', 'period': 2},
            {'organization': 'ЭР-Телеком Холдинг, ЗАО', 'position': 'Программист биллинга',
             'duties': 'Программист биллинга. Отдел работы с юр.лицами. Сбор требований у заказчиков (email, телефон, командировки). Консультация заказчиков. Внедрение и поддержка ПО',
             'period': 6},
            {'organization': 'Прогноз, ЗАО', 'position': 'Программист-разработчик',
             'duties': 'Разработка Bi - приложений (Систем сбора, хранения, анализа данных с использованием многомерных структур (типа ADOMD) для органов государственной власти РФ) Формирование регламентной отчетности. Сбор требований у заказчиков (email, телефон, командировки). Консультация заказчиков. Внедрение и поддержка ПО.',
             'period': 25},
        ]
        hobbies = [
            {'name': 'Путешествия'},
            {'name': 'Музыка'},
        ]
        studies = [
            {
                'name': 'Пермский государственный национальный исследовательский университет',
                'date_start':date(year=2008, month=1, day=1),
                'date_end':date(year=2013, month=1, day=1)
            },
        ]
        Organization.objects.all().delete()
        for organization in organizations:
            organization = Organization(**organization)
            organization.save()

        Work.objects.all().delete()
        for work in works:
            org_name = work["organization"]
            # Получаем организацию по имени
            organization = Organization.objects.get(name=org_name)
            # Заменяем название организации объектом
            work['organization'] = organization
            work = Work(**work)
            work.save()

        Hobby.objects.all().delete()
        for hobby in hobbies:
            hobby = Hobby(**hobby)
            hobby.save()

        Study.objects.all().delete()
        for study in studies:
            study = Study(**study)
            study.save()
