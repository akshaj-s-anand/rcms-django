# Generated by Django 4.2.3 on 2024-01-31 02:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rcmsApp', '0017_engineers_complaint_assigned_engineer'),
    ]

    operations = [
        migrations.CreateModel(
            name='ComplaintStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='complaint',
            name='status',
            field=models.ForeignKey(blank=True, default='Open', null=True, on_delete=django.db.models.deletion.CASCADE, to='rcmsApp.complaintstatus'),
        ),
    ]
