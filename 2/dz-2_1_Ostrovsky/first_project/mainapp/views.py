from django.shortcuts import render, render_to_response
def main(request):
    return render(request, 'index.html')

def job(request):
    jobs_list = [
        {'name':'Управляющая компания "Аптечная сеть 36,6', 'period':'2007 - 2009', 'position':'ведущий бизнес-аналитик, начальник отдела бизнес-анализа и стандартизации'},
        {'name':'ООО "Еврологистика"', 'period':'2009 - 2011','position':'системный архитектор, начальник отдела контроля качества бизнес-процессов'},
        {'name':'Фонд просвещения "МЕТА"', 'period':'2011 - 2013', 'position':'главный специалист по бизнес-процессам, руководитель управления стратегического развития'},
        {'name':'Открытое правительство Москвы', 'period':'2013 - 2013', 'position':'начальник отдела методологии'},
        {'name':'Российская академия народного хозяйства и государственной службы', 'period':'2013 - 2015','position': 'ведущий эксперт'},
        {'name':'ООО "Прогресс софт"', 'period':'2015 - по наст. время','position':'ведущий аналитик'}
    ]
    return render(request, 'job.html', {'jobs_list':jobs_list})

def edu(request):
    return render(request, 'edu.html')

# Create your views here.
