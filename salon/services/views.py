from django.shortcuts import render
from .models import Servicec

def services(request):
    sevices_list = Servicec.objects.order_by('title')
    return render(request, 'services/services.html', {'services': sevices_list})
