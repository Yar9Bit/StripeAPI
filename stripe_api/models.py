from django.db import models


# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=16)
    description = models.CharField(max_length=128)
    price = models.IntegerField(default=0)

    CURRENCY_PAYMENT = [
        ('USD', 'USD'),
        ('RUB', 'RUB'),
    ]

    currency = models.CharField(choices=CURRENCY_PAYMENT, max_length=16)

    def __str__(self):
        return self.name

    def get_display_price(self):
        return "{0:.2f}".format(self.price / 100)
