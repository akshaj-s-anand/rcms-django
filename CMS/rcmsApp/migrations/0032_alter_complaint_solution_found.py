# Generated by Django 4.2.3 on 2024-02-01 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rcmsApp', '0031_alter_complaint_bill_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='solution_found',
            field=models.CharField(blank=True, default='', help_text='How was the issue solved', max_length=200, null=True),
        ),
    ]