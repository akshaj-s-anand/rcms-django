from django.db import models
from django.contrib.auth.models import AbstractUser

class Customer(AbstractUser):
    name = models.CharField(max_length=255, default='')
    phone_number = models.CharField(max_length=20, default='', unique=True)
    email = models.EmailField(max_length=255, default='')
    
    # Add your new field with a default value
    new_field = models.CharField(max_length=255, default='default_value')

    # Define the fields that will be used for authentication
    USERNAME_FIELD = 'name'
    REQUIRED_FIELDS = ['phone_number']

    # Set a one-off default for the password field
    password = models.CharField(max_length=128, default='')

    # Specify unique related_name arguments to avoid clashes
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customer_groups',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
    )
    
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customer_user_permissions',
        blank=True,
        help_text='Specific permissions for this user.',
    )

    def save(self, *args, **kwargs):
        # Set the password to be the phone number
        self.set_password(self.phone_number)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name or self.username

    # Override get_username method to return the value of the name field
    def get_username(self):
        return self.name
