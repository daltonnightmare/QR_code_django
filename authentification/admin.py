from django.contrib import admin
from .models import Utilisateurs
# Register your models here.
@admin.register(Utilisateurs)
class UtilisateursAdmin(admin.ModelAdmin):
    list_display = ['utilisateur', 'Qrcode']