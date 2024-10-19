from django.db import models
from django.contrib.auth.models import User
from QRCODE.models import QR_code
# Create your models here.
class Utilisateurs(models.Model):
    utilisateur = models.OneToOneField(to=User, on_delete=models.CASCADE)
    Qrcode = models.ForeignKey(to=QR_code, on_delete=models.CASCADE)
