from django.db import models

class ShippingMethod(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    delivery_time = models.CharField(max_length=50)

class Checkout(models.Model):
    cart = models.OneToOneField('cart.Cart', on_delete=models.CASCADE)
    shipping_method = models.ForeignKey(ShippingMethod, on_delete=models.PROTECT)
    shipping_address = models.JSONField()  # lub osobny model
    payment_method = models.CharField(max_length=50)