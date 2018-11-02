from django.db import models
from django.contrib.auth.models import User


# Create your models here.
STATUS_CHOICES = (
    ('cart', 'Cart'),
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
    gambar = models.ImageField(upload_to='post_image/',blank=True, null=True)
    harga = models.DecimalField(max_digits=15, decimal_places=2)
    qty = models.IntegerField(blank=True, default=0)
    kategori = models.ForeignKey('Kategori', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Produk'

    def __str__(self):
        return self.nama


class Order(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_order")
    no_hape = models.CharField(max_length=15, null=True)
    alamat = models.TextField(default='Jogja')
    ongkosKirim = models.DecimalField(
        max_digits=15, decimal_places=2, default=0)
    Date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES,
                              default='cart')
    sub_total = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    total = models.DecimalField(max_digits=15, decimal_places=2, default=0)

    class Meta:
        verbose_name_plural = 'Order'

    def __str__(self):
        return self.user.username

    # def setSubTotal(self):
    #     sub = 0
    #     OR = Order.objects.all()
    #     for orr in OR:
    #         od = orr.barang_order.all()
    #         for OD in od:
    #             print(sub)
    #             print(OD.subtotal)
    #             sub+=int(OD.subtotal)
    #     self.sub_total = sub
    #     print(sub)
    #     return sub


class Order_Detail(models.Model):
    order = models.ForeignKey(
        'Order', on_delete=models.CASCADE, related_name="barang_order")
    produk = models.ForeignKey(
        'Produk', on_delete=models.CASCADE, related_name="barang_order")
    qty = models.IntegerField(blank=True, default=1)
    harga = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    catatan = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Order Detail'
        unique_together = (("order", "produk"),)

    def __str__(self):
        return self.produk.nama

    # fungsi untuk kalkulasi sub total
    def subtotal(self):
        return self.harga * self.qty
