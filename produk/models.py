from django.db import models
from django.contrib.auth.models import User


# Create your models here.
STATUS_CHOICES = (
    ('checkout', 'Checkout'),
    ('paid', 'Terbayar'),
    ('delivered', 'Terkirim'),
)

class Kategori(models.Model):
	nama = models.CharField(max_length=30)

	class Meta:
		verbose_name_plural = 'Kategori'

	def __str__(self):
		return self.nama


class Produk(models.Model):
	nama = models.CharField(max_length=125)
	merk = models.CharField(max_length=30, null=True, blank=True)
	gambar = models.ImageField(blank=True, null=True)
	harga = models.DecimalField(max_digits=15, decimal_places=2)
	qty = models.IntegerField(blank=True,default=0)
	kategori = models.ForeignKey('Kategori',on_delete=models.CASCADE)

	class Meta:
		verbose_name_plural = 'Produk'

	def __str__(self):
		return self.nama

class Order(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	ongkosKirim = models.DecimalField(max_digits=15, decimal_places=2,default=0)
	alamat = models.TextField()
	Date = models.DateTimeField(auto_now_add=True)
	produk = models.ForeignKey(Produk,on_delete=models.CASCADE)
	qty = models.IntegerField(blank=True,default=1)
	status = models.CharField(max_length=15,choices=STATUS_CHOICES,
								default='checkout')
	catatan = models.TextField(blank=True,null=True)

	class Meta:
		verbose_name_plural = 'Order'

	def __str__(self):
		return self.user


# class Order_Detail(models.Model):
# 	produk = models.ForeignKey('Produk',on_delete=models.CASCADE)
# 	qty = models.IntegerField(blank=True,default=1)
# 	harga = models.DecimalField(max_digits=15, decimal_places=2)
# 	catatan = models.TextField(blank=True,null=True)

# 	class Meta:
# 		verbose_name_plural = 'Order Detail'

# 	def __str__(self):
# 		return self.produk