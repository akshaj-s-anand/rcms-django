# Generated by Django 4.2.3 on 2024-01-31 02:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rcmsApp', '0021_complaint_test'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='complaint',
            name='test',
        ),
    ]
