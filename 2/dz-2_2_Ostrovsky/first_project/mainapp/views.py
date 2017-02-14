from django.shortcuts import render, render_to_response
from datetime import date


def main(request):
    text = 'Здравствуйте! Эта персональная страница была разработана мной в рамках учебного курса Django. Меня зовут Островский Василий Александрович. Я родился в Москве, заниматься программированим начал в школе и продолжаю до сих пор. В настоящее время изучаю основы веб-разработки с использованием Python 3.6 и Django 1.10. '
    name = 'Островский Василий'
    birthdate = date(1980, 1, 15)
    return render(request, 'index.html', {'text': text, 'name': name, 'birthdate': birthdate})


def job(request):
    jobs_list = [
        {'name': 'ООО "Прогресс софт"', 'period': '2015 - по наст. время', 'position': 'ведущий аналитик',
         'link': 'http://progresspoint.ru/'},
        {'name': 'Российская академия народного хозяйства и государственной службы', 'period': '2013 - 2015',
         'position': 'ведущий эксперт', 'link': 'http://www.ranepa.ru/'},
        {'name': 'Открытое правительство Москвы', 'period': '2013 - 2013', 'position': 'начальник отдела методологии',
         'link': 'http://mos.ru/'},
        {'name': 'Фонд просвещения "МЕТА"', 'period': '2011 - 2013',
         'position': 'главный специалист по бизнес-процессам, руководитель управления стратегического развития',
         'link': 'http://fpmeta.org/'},
        {'name': 'ООО "Еврологистика"', 'period': '2009 - 2011',
         'position': 'системный архитектор, начальник отдела контроля качества бизнес-процессов',
         'link': 'http://eurologic.ru/'},
        {'name': 'Управляющая компания "Аптечная сеть 36,6', 'period': '2007 - 2009',
         'position': 'ведущий бизнес-аналитик, начальник отдела бизнес-анализа и стандартизации',
         'link': 'http://pharmacychain366.ru/'}

    ]
    return render(request, 'job.html', {'jobs_list': jobs_list})


def edu(request):
    edu_list = [
        {'name': 'Московская международная школа бизнеса "МИРБИС"', 'period': '2006 - 2007',
         'spec': 'специальность - Системный анализ и управление проектами', 'link': 'http://www.mirbis.ru/'},
        {'name': 'Институт криптографии, связи и информатики', 'period': '1997 - 2002',
         'spec': 'специальность - Радиоэлектронные системы защиты информации', 'link': 'http://www.academy.fsb.ru/'},
        {'name': 'Школа № 843 г.Москвы', 'period': '1995 - 1997'},
        {'name': 'Школа № 14 г.Москвы', 'period': '1987 - 1995'}
    ]

    return render(request, 'edu.html', {'edu_list': edu_list})


def hobby(request):
    hobbies = [
        {'name': 'кино', 'img': 'glyphicon glyphicon-film'},
        {'name': 'музыка', 'img': 'glyphicon glyphicon-headphones'},
        {'name': 'фотография', 'img': 'glyphicon glyphicon-camera'},
        {'name': 'путешествия', 'img': 'glyphicon glyphicon-plane'},
        {'name': 'обучение', 'img': 'glyphicon glyphicon-education'},
        {'name': 'программирование', 'img': 'glyphicon glyphicon-floppy-disk'}

    ]
    return render(request, 'hobby.html', {'hobbies': hobbies})
