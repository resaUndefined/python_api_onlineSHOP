# Generated by Django 2.1.2 on 2018-10-24 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produk', '0011_auto_20181015_1136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('cart', 'Cart'), ('checkout', 'Checkout'), ('paid', 'Terbayar'), ('delivered', 'Terkirim')], default='cart', max_length=15),
        ),
        migrations.AlterField(
            model_name='produk',
            name='gambar',
            field=models.ImageField(blank=True, null=True, upload_to='post_image/'),
        ),
    ]
