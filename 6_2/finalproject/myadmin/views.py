from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.contrib.auth.models import User
from spigen.forms import MyRegistrationForm, UserChangeForm
from django.http import Http404, JsonResponse
from django.template import loader
from django.template.context_processors import csrf
from django.contrib.auth.decorators import user_passes_test


# Create your views here.
def admin_page(request):
    users = User.objects.all()
    user_form = MyRegistrationForm()
    return render(request, 'admin.html', {"users":users, 'form':user_form})

def delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    print(user_id, user)
    user.delete()
    return HttpResponseRedirect("/admin")

def create_user(request, user_id=None):

    if request.is_ajax():
        if not user_id:
            user = User(request.POST)
        else:
            user = get_object_or_404(User, id=user_id)
            user = UserChangeForm(request.POST or None, instance=user)
        if user:
            user.save()
            users = User.objects.all()
            html = loader.render_to_string('admin.html', {'users': users}, request=request)
            data = {'errors':False, 'html':html}
            return JsonResponse(data)
        else:
            errors = user.errors.as_json()
            return JsonResponse({'errors':errors})
    raise Http404

def get_user_form(request, user_id):
    if request.is_ajax():
        user = get_object_or_404(User, id=user_id)
        user_form = MyRegistrationForm(instance=user)
        context = {'form':user_form, 'id':user_id}
        context.update(csrf(request))
        html = loader.render_to_string('admin.html', context)
        data = {'errors':False, 'html':html}
        return JsonResponse(data)
    raise Http404


