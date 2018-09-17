from django.contrib import admin
from .models import Kategori, Produk
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

admin.site.site_header = 'Toko Online Administrator'
admin.site.register(Kategori,KategoriAdmin)
admin.site.register(Produk,ProdukAdmin)
