from django import forms

from .models import Order

class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ('name', 'clothing','price','order_date','completion_date','done')