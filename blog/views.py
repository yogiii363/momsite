from django.shortcuts import render
from .models import Order
from django.utils import timezone
# Create your views here.
def order_list(request):
	orders = Order.objects.filter(order_date__lte=timezone.now()).order_by('order_date')
	return render(request,'blog/order_list.html',{'orders': orders})