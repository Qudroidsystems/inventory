# Generated by Django 5.1.2 on 2024-11-14 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventoryapp', '0003_contactform'),
    ]

    operations = [
        migrations.CreateModel(
            name='NinModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullName', models.CharField(max_length=80)),
                ('nin', models.CharField(max_length=10)),
                ('sor', models.CharField(max_length=50)),
            ],
        ),
    ]