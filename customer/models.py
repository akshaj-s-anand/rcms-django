from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# class Customer(models.Model):
#     name = models.CharField(max_length=255, unique=True)
#     user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
#     phone_number = models.CharField(max_length=15, unique=True)
#     email_id = models.EmailField(blank=True, null=True)
#     address = models.TextField(blank=True, null=True, default='', help_text='Enter the address here')
#     dealer = models.ForeignKey('Dealer', on_delete=models.SET_DEFAULT, default=2)  # Assuming the dealer with ID=1 is Orion

#     def __str__(self):
#         return self.name
    
#     def save(self, *args, **kwargs):
#         if not self.user:
#             user = User.objects.create(username=self.name)
#             self.user = user
#         super().save(*args, **kwargs)

#     def related_complaints(self):
#         return Complaint.objects.filter(customer=self)
