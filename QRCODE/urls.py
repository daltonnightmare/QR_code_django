from django.urls import path 
from QRCODE.views import *
app_name = 'QRCODE'
urlpatterns = [
    path('', accueil.as_view(), name='accueil'),
    path('liste/', ListeQR.as_view(), name='liste')
]