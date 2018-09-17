from django.urls import path
from api.produk.views import ProdukList


urlpatterns = [
	path('', ProdukList.as_view(), name='Produk-list'),
]