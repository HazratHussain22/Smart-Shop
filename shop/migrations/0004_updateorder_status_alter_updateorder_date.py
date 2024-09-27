# Generated by Django 5.1 on 2024-09-25 05:54

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_rename_order_id_updateorder_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='updateorder',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('processed', 'Processed'), ('shipped', 'Shipped'), ('delivered', 'Delivered'), ('cancelled', 'Cancelled')], default='pending', max_length=50),
        ),
        migrations.AlterField(
            model_name='updateorder',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
