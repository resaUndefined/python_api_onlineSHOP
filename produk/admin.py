from django.contrib import admin
from .models import Kategori, Produk, Order
# Register your models here.

class KategoriAdmin(admin.ModelAdmin):
	list_display = ('nama',)


class ProdukAdmin(admin.ModelAdmin):
	list_display = ('nama','get_category','merk','harga','qty',)

	def get_category(self,obj):
		if obj.kategori:
			return obj.kategori.nama
		else:
			return u''
		
		get_category.short_description = 'Kategori'
		get_category.admin_order_field = 'kategori__nama'


class OrderAdmin(admin.ModelAdmin):
	list_display = ('get_user','get_produk','qty','Date','status',)

	def get_user(self, obj):
		return obj.user.username
	get_user.short_description = 'User'
	get_user.admin_order_field = 'User__username'

	def get_produk(self, obj):
		return obj.produk
	get_produk.short_description = 'Produk'
	get_produk.admin_order_field = 'Produk__nama'


admin.site.site_header = 'Toko Online Administrator'
admin.site.register(Kategori,KategoriAdmin)
admin.site.register(Produk,ProdukAdmin)
admin.site.register(Order,OrderAdmin)
