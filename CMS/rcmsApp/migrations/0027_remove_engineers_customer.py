# Generated by Django 4.2.3 on 2024-01-31 03:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rcmsApp', '0026_remove_complaint_complaint_raised_on_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='engineers',
            name='customer',
        ),
    ]