from django.shortcuts import render, get_object_or_404
from .models import Discount


def index(request):
    discount = Discount.objects.order_by('-date')
    return render(request, 'discount/index.html', {'discounts': discount})


def detail(request, discount_id):
    discount = get_object_or_404(Discount, pk=discount_id)
    return render(request, 'discount/discoubt_page.html', {'discount': discount})
