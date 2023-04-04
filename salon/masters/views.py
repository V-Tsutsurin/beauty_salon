from django.shortcuts import render, get_object_or_404
from .models import Master


def masters(request):
    master = Master.objects.order_by('name')
    return render(request, 'masters/masters.html', {'masters': master})
