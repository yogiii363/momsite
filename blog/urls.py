from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.order_list, name = 'order_list'),
	url(r'^order/(?P<pk>\d+)/$', views.order_detail, name='order_detail'),
]
