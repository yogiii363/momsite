from django.db import models
from django.utils import timezone


class Order(models.Model):
    customer = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    name = models.CharField(max_length=200,default='customer')
    clothing = models.CharField(max_length=200)
    price = models.TextField()
    order_date = models.DateTimeField(
            default=timezone.now)
    completion_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.completion_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name	