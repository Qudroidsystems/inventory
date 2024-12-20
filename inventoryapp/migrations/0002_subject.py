# Generated by Django 5.1.2 on 2024-10-31 13:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventoryapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subjectName', models.CharField(max_length=50)),
                ('subjectcode', models.CharField(max_length=50)),
                ('biodataId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventoryapp.biodata')),
            ],
        ),
    ]
