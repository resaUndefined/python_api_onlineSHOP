# Generated by Django 2.1.2 on 2018-10-08 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produk', '0004_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='Date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
