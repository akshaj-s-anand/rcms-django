# models.py
from datetime import datetime
from django.db import models

class Item(models.Model):
    item_name = models.CharField(max_length=255, unique=True, null=True, blank=True)

    def __str__(self):
        return f"{self.item_name}"

class Brand(models.Model):
    brand_name = models.CharField(max_length=255, unique=False, null=True, blank=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.brand_name


class Model(models.Model):
    model_name = models.CharField(max_length=255, unique=False, null=True, blank=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, null=True, blank=True)
    brand = models.ForeignKey(Brand, on_delete = models.CASCADE, null = True, blank = True)
    def __str__(self):
        return self.model_name
    
class Customer(models.Model):
    name = models.CharField(max_length=255, unique=True)
    phone_number = models.CharField(max_length=15, unique=True)
    email_id = models.EmailField(blank=True, null=True)
    address = models.TextField(blank=True, null=True, default='', help_text='Enter the address here')

    def __str__(self):
        return self.name

    def related_complaints(self):
        return Complaint.objects.filter(customer=self)
    
class Engineer(models.Model):
    name = models.CharField(max_length=255, unique=False, null=True, blank=True)
    phone_number = models.CharField(max_length=15, unique=True)
    def __str__(self):
        return self.name
    
class Complaint(models.Model):
    STATUS_CHOICES = (
        ('Open', 'Open'),
        ('Close', 'Close'),
        ('Temporarily Closed', 'Temporarily Closed'),
    )

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, blank=True, null=True, default='')
    pub_date = models.DateTimeField("date published", default=datetime.now)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, blank=True, null=True, default='')
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, blank=True, null=True, default='')
    model = models.ForeignKey(Model, on_delete=models.CASCADE, blank=True, null=True, default='')
    complaint = models.CharField(max_length=20, blank=True, null=True, default='', help_text='Enter the issue faced')
    actual_complaint = models.CharField(max_length=100, blank=True, null=True, default='', help_text='Real issue')
    solution_found = models.CharField(max_length=200, blank=True, null=True, default='', help_text='How was the issue solved')
    assigned_engineer = models.ForeignKey(Engineer, on_delete=models.CASCADE, blank=True, null=True, default='')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Open')
    bill_amount = models.CharField(max_length = 5, null=True, blank=True, default=0)

    def __str__(self):
        engineer_name = self.assigned_engineer.name if self.assigned_engineer else "Unassigned"
        return f"Complaint {self.id} assigned to {engineer_name} - Status: {self.status}"
