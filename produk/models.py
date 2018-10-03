from django.db import models


# Create your models here.
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