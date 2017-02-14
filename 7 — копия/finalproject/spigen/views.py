from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth
from django.http import Http404
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from spigen.forms import MyRegistrationForm
from spigen.models import Category

# Create your views here.
def main(request):
    categories = Category.objects.all()
    return render(request, 'index.html', {'categories':categories})

def login(request):
    if request.method == 'POST':
        print("POST datd =", request.POST)
        username = request.POST.get('login')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user:
            auth.login(request, user)
            return HttpResponseRedirect("/")
        else:
            return render(request, "index.html", {'username': username, 'errors': True})
    raise Http404

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/")

def registration_low(request):
    if request.method == 'POST':
        errors = {}
        username = request.POST.get('name')
        email = request.POST.get('email')
        confirm_email = request.POST.get('confirm_email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        if email != confirm_email:
            errors['email'] = 'Не совпадают адреса e-mail'
        if password != password:
            errors['password'] = 'Не совпадают пароли'
        user = User(username=username, email=email)
        user.set_password(password)
        try:
            user.validate_unique()
        except ValidationError as er:
            errors.update(er.message_dict)
        if errors:
            print(errors)
            return render(request, 'registration_low.html', {'reg_errors': errors})
        user.save()
        return HttpResponseRedirect("/")
    return render(request, 'registration_low.html')

def registration_form(request):
    if request.method == 'POST':
        form = MyRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        context = {'form':form}
        return render(request, 'registration_form.html', context)
    context = {'form':MyRegistrationForm()}
    return render(request, 'registration_form.html', context)

def catalog(request, category):
    print(category)
    return HttpResponseRedirect('/')