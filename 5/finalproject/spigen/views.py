from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth
from django.http import Http404

# Create your views here.
def main(request):
    return render(request, 'index.html')

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