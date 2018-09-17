from django.urls import path,include
from rest_framework_swagger.views import get_swagger_view


schema_view = get_swagger_view(title='Toko Online API')

urlpatterns = [
	path('kategori/', include('api.kategori.urls')),
	path('produk/', include('api.produk.urls')),
    path('docs/',schema_view),
]