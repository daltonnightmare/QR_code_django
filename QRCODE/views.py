from django.shortcuts import render
import qrcode
from django.views.generic import TemplateView, View, ListView
from QRCODE.models import *
from django.conf import settings
import os
# Create your views here.

class accueil(TemplateView):
    template_name = 'QRCODE/index.html'

    def post(self, request, *args, **kwargs):
        qrtext = request.POST.get('qrtext')
        try:
            qrdesc = request.POST.get('qrdesc')
        except:
            qrdesc = ''
        QRCODE_models = QR_code
        Code = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        
        Code.add_data(qrtext)
        Code.make(fit=True)
        image = Code.make_image(fill_color='black', back_color= 'pink')
        media_dirs = os.path.join(settings.MEDIA_ROOT, 'QR_Images')

        if not os.path.exists(media_dirs):
            os.makedirs(media_dirs)
        filename= f'{qrtext}.png'
        filepath = os.path.join(media_dirs, filename)
        image.save(filepath)

        t=QR_code.objects.create(phrase=qrtext, code='QR_Images/' + filename, description = qrdesc)
        t.save()
        QRCODE_ALL = QR_code.objects.all()
        return self.render_to_response(self.get_context_data(qrtexte=qrtext,qr=QRCODE_ALL))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['qrtext'] = kwargs.get('qrtexte',)
        context['qr'] = kwargs.get('QRCODE_ALL')
        return context
    

class ListeQR(ListView):
    model = QR_code
    context_object_name = 'qr'
    template_name='QRCODE/tableau.html'
    pass
    