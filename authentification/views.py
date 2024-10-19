from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
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
        logout(request)
        return render(request, 'authentification/login.html')
    def post(self, request, *args, **kwargs):
        logout(request)
        return render(request, 'authentification/login.html')
        
class REGISTER(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'authentification/register.html')
    def post(self, request, *args, **kwargs):
        try:
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
            
        except:

            return render(request, 'authentification/register.html')
        

