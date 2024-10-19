from django.db import models

# Create your models here.

class QR_code(models.Model):
    phrase = models.CharField(max_length=255)
    description=models.TextField(null=True, blank=True, default='')
    code = models.ImageField(upload_to='QR_Images')
    date_de_creation = models.DateTimeField(auto_now=True)
    pass