from django.db import models
from django.utils import timezone
from datetime import date

class Order(models.Model):
    customer = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    name = models.CharField(max_length=200,default='customer')
    clothing = models.TextField()
    price = models.TextField()
    order_date = models.DateField(default=date.today)
    completion_date = models.DateField()
    done = models.BooleanField(default=False)

    def publish(self):
        self.completion_date = date.today
        self.save()

    def __str__(self):
        return self.name


class RateList(models.Model):
	order = models.ForeignKey('blog.Order', related_name='rate')
	cloth_name = models.CharField(max_length=200)
	cloth_rate = models.CharField(max_length=20)
        			        	