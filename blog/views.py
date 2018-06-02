from django.shortcuts import render, get_object_or_404
from .models import Order, RateList
from django.utils import timezone
from .forms import OrderForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
# Create your views here.


def order_list(request):
	orders = Order.objects.filter(order_date__lte=timezone.now()).order_by('order_date')
	return render(request,'blog/order_list.html',{'orders': orders})

def order_detail(request,pk):
	order = get_object_or_404(Order, pk =pk)
	return render(request, 'blog/order_detail.html',{'order': order})

def order_new(request):
	if request.method == "POST":
		form = OrderForm(request.POST)
		if form.is_valid():
			order = form.save(commit=False)
			order.customer = request.user
			order.order_date = timezone.now()
			order.save()
			return redirect('order_detail', pk=order.pk)
	else:
		form = OrderForm()
	return render(request, 'blog/order_edit.html',{'form': form})	        


def order_edit(request, pk):
    order = get_object_or_404(Order, pk=pk)
    if request.method == "POST":
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            order = form.save(commit=False)
            order.customer = request.user
            order.save()
            return redirect('order_detail', pk=order.pk)
    else:
        form = OrderForm(instance=order)
    return render(request, 'blog/order_edit.html', {'form': form})


@login_required
def order_remove(request, pk):
    order = get_object_or_404(Order, pk=pk)
    order.delete()
    orders = Order.objects.filter(order_date__lte=timezone.now()).order_by('order_date')
    return redirect('order_list')

def rate_list(request):
	rates = RateList.objects.order_by('cloth_name')
	return render(request, 'blog/rate_list.html',{'rates':rates})