from django.urls import path,re_path
from api.produk.views import ProdukList,ProdukDetail


urlpatterns = [
	path('', ProdukList.as_view(), name='Produk-list'),
    re_path(r'^(?P<pk>[0-9]+)/$', ProdukDetail.as_view(), name='produk-detail'),
]