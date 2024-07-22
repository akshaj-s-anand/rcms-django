from django.db import models

# Create your models here.
class Enquiry(models.Model):
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=10)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class ProductDetails(models.Model):
    PRODUCT_LIST = [
        ('Solar Products', 'Solar Products'),
        ('Battery', 'Battery'),
        ('UPS/Inverter', 'UPS/Inverter'),
        ('Solar Water Heater', 'Solar Water Heater'),
    ]
    
    name = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    category = models.CharField(max_length=50, choices=PRODUCT_LIST)
    recommended_uses_for_product = models.CharField(max_length=50)
    power_source = models.CharField(max_length=50)
    image = models.ImageField(upload_to='product_images/')
    def __str__(self):
        return self.name
    
class Contact(models.Model):
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)
    message = models.TextField()
    
    def __str__(self):
        return self.name