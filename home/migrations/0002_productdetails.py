# Generated by Django 4.2.14 on 2024-07-15 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('brand', models.CharField(max_length=50)),
                ('category', models.CharField(choices=[('Solar Products', 'Solar Products'), ('Battery', 'Battery'), ('UPS/Inverter', 'UPS/Inverter'), ('Solar Water Heater', 'Solar Water Heater')], max_length=50)),
                ('recommended_uses_for_product', models.CharField(max_length=50)),
                ('power_source', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='product_images/')),
            ],
        ),
    ]
