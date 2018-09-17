from django.urls import path
from api.kategori.views import KategoriList


urlpatterns = [
	path('', KategoriList.as_view(), name='kategori-list'),
]