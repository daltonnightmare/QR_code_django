from django.urls import path
from .views import *
app_name = 'authentification'
urlpatterns = [
    path('login/', login_user, name='login'),
    path('logout/', LOGOUT.as_view(), name='logout'),
    path('register/', REGISTER.as_view(), name='register'), 
    path('compte/', COMPTE, name='compte'),
    path('mot_de_passe/', PASSWORDCHANGE, name='change_password'),
    path('profile/', UPDATEPROFILE, name='modifier_profil'),
]