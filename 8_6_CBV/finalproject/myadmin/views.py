from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.contrib.auth.models import User
from spigen.forms import MyRegistrationForm
from django.http import Http404, JsonResponse
from django.template import loader
from django.template.context_processors import csrf
from django.contrib.auth.decorators import user_passes_test
from spigen.models import Category, Item
from spigen.forms import Category_form, Item_form


# Create your views here.
@user_passes_test(lambda u: u.is_superuser)
def admin_page(request):
    users = User.objects.all()
    user_form = MyRegistrationForm()
    return render(request, 'admin.html', {"users":users, 'form':user_form})

def delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.delete()
    return HttpResponseRedirect("/admin")

def create_user(request, user_id=None):
    """
    Создает Пользователя(User)
    Или редактирует существующего, если указан  user_id
    """
    if request.is_ajax():
        if not user_id:
            user = MyRegistrationForm(request.POST)
        else:
            user = get_object_or_404(User, id=user_id)
            user = MyRegistrationForm(request.POST or None, instance=user)
        if user.is_valid():
            user.save()
            users = User.objects.all()
            html = loader.render_to_string('inc-users_list.html', {'users': users}, request=request)
            data = {'errors': False, 'html': html}
            return JsonResponse(data)
        else:
            errors = user.errors.as_json()
            return JsonResponse({'errors': errors})

    raise Http404

def get_user_form(request, user_id):
    if request.is_ajax():
        user = get_object_or_404(User, id=user_id)
        user_form = MyRegistrationForm(instance=user)
        context = {'form':user_form, 'id':user_id}
        context.update(csrf(request))
        html = loader.render_to_string('inc-registration_form.html', context)
        data = {'errors':False, 'html':html}
        return JsonResponse(data)
    raise Http404

@user_passes_test(lambda u: u.is_superuser)
def admin_cat(request):
    categories = Category.objects.all()
    cat_form = Category_form()
    return render(request, 'admin_cat.html', {'categories':categories, 'form':cat_form})

def admin_cat_create(request, cat_id=None):
    """
    Создает Категорию (Category)
    Или редактирует существующюю, если указан  cat_id
    """
    if request.is_ajax():
        if not cat_id:
            cat = Category_form(request.POST)
        else:
            cat = get_object_or_404(Category, id=cat_id)
            cat = Category_form(request.POST or None, instance=cat)
        if cat.is_valid():
            cat.save()
            categories = Category.objects.all()
            html = loader.render_to_string('inc-categories_list.html', {'categories': categories}, request=request)
            data = {'errors': False, 'html': html}
            return JsonResponse(data)
        else:
            errors = cat.errors.as_json()
            return JsonResponse({'errors': errors})

    raise Http404




def admin_cat_delete(request, id):
    category = get_object_or_404(Category, id=id)
    category.delete()
    return HttpResponseRedirect('/admin/cat/')
'''
def admin_cat_update(request, id):
    cat = get_object_or_404(Category,id=id)
    if request.method == 'POST':
        form = Category_form(request.POST, instance=cat)
        if form.is_valid():
            cat.save()
            return HttpResponseRedirect('/admin/cat/')
        context = {'form':form}
        return render(request, 'admin_cat_update.html', context)
    context = {'form':Category_form(instance=cat)}
    return render(request, 'admin_cat_update.html', context)

def admin_cat_detail(request, id):
    cat = get_object_or_404(Category, id=id)
    return render(request, 'admin_cat_detail.html', {'cat':cat})
'''
def get_cat_info(request, cat_id):
    if request.is_ajax():
        cat = get_object_or_404(Category, id=cat_id)
        cat_form = Category_form(instance=cat)
        context = {'form':cat_form, 'id':cat_id}
        context.update(csrf(request))
        html = loader.render_to_string('inc-registration_form.html', context)
        data = {'errors':False, 'html':html}
        return JsonResponse(data)
    raise Http404

def cat_delete(request, cat_id):
    cat = get_object_or_404(Category, id=cat_id)
    cat.delete()
    return HttpResponseRedirect("/admin/cat")

@user_passes_test(lambda u: u.is_superuser)
def admin_item(request):
    items = []
    item_form = Item_form()
    categories = Category.objects.all()
    return render(request, 'admin_item.html', {'items':items, 'form':item_form, 'categories':categories})

def admin_item_create(request, item_id=None):
    """
    Создает Товар (Item)
    Или редактирует существующий, если указан  item_id
    """
    if request.is_ajax():
        if not item_id:
            item = Item_form(request.POST, request.FILES)
        else:
            item = get_object_or_404(Item, id=item_id)
            item = Item_form(request.POST or None, instance=item)
        if item.is_valid():
            item.save()
            items = Item.objects.all()
            html = loader.render_to_string('inc-items_list.html', {'items': items}, request=request)
            data = {'errors': False, 'html': html}
            return JsonResponse(data)
        else:
            errors = item.errors.as_json()
            return JsonResponse({'errors': errors})

    raise Http404

def admin_item_delete(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    item.delete()
    return HttpResponseRedirect('/admin/item')


def get_item_info(request, item_id):
    print("-----------------------------------------------")
    print(item_id)
    print("-----------------------------------------------")
    if request.is_ajax():
        item = get_object_or_404(Item, id=item_id)
        item_form = Item_form(instance=item)
        context = {'form':item_form, 'id':item_id}
        context.update(csrf(request))
        html = loader.render_to_string('inc-registration_form.html', context)
        data = {'errors':False, 'html':html}
        return JsonResponse(data)
    raise Http404


def get_item_by_cat(request, cat_id):
    if request.is_ajax():
        items = Item.objects.filter(category_id=cat_id)
        print(len(items))
        context = {'items':items}
        context.update(csrf(request))
        html = loader.render_to_string('inc-items_list.html', context)
        data = {'errors': False, 'html': html}
        return JsonResponse(data)
    raise Http404


