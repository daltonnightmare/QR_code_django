from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.messages import Message

# Create your views here.

def login_user(request, *args, **kwargs):
    if request.method == 'POST':
        username = request.POST.get('usernameget')
        password = request.POST.get('passwordget')
        utilisateur = authenticate(username=username, password=password)
        print(utilisateur)
        if utilisateur is not None:
            login(request, utilisateur)
            return redirect('QRCODE:accueil')
        else:
            return render(request, 'authentification/login.html')
    return render(request, 'authentification/login.html')
        
        


class LOGOUT(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'authentification/logout.html')
    def post(self, request, *args, **kwargs):
        logout(request)
        return redirect('authentification:login')
        
class REGISTER(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'authentification/register.html')
    def post(self, request, *args, **kwargs):
        
        username = request.POST.get('username')
        mail = request.POST.get('mail')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 == password2:
            user = User.objects.create(username=username, email=mail, password=password1)
            user.save()
            return redirect('authentification:login')
        else:
            return render(request, 'authentification/register.html')
        
    
def COMPTE(request):
    return render(request, 'authentification/compte/compte.html')

def PASSWORDCHANGE(request):
    return render(request, 'authentification/compte/changer_password.html')

def UPDATEPROFILE(request):
    user = get_object_or_404(User, username=request.user.username)
    if request.method == 'POST':
        username = request.POST.get('username')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')

        user.username = username
        user.first_name = firstname
        user.last_name = lastname
        user.email = email 
        user.save()
        return redirect('authentification:compte')
    return render(request, 'authentification/compte/modifier_profil.html', context={'user':user})