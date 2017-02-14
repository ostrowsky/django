from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.contrib import auth
from django.http import Http404
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from spigen.forms import MyRegistrationForm
from spigen.models import Category, Item

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

def catalog(request, cat_link):
    cat_link_add = '/cat/' + cat_link + '/'
    cat = get_object_or_404(Category, link=cat_link_add)
    items = Item.objects.filter(category=cat)
    categories = Category.objects.all()
    context = {"items":items, "category":cat, "categories":categories}
    return render(request, 'category.html',context )

def item(request, item_id):
    categories = Category.objects.all()
    item=get_object_or_404(Item, pk=item_id)
    context = {"item":item, "categories":categories}
    return render(request, 'item.html', context)
