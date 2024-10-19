from django.urls import path
from .views import *
app_name = 'authentification'
urlpatterns = [
    path('login/', login_user, name='login'),
    path('logout/', LOGOUT.as_view(), name='logout'),
    path('register/', REGISTER.as_view(), name='register')
]