# Generated by Django 4.2.3 on 2024-02-07 09:01

import django.core.validators
from django.db import migrations, models
import rcmsApp.models


class Migration(migrations.Migration):

    dependencies = [
        ('rcmsApp', '0039_alter_products_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='img/uploads/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'], message='Only JPEG, JPG or png files are allowed.'), rcmsApp.models.validate_image_size]),
        ),
    ]
