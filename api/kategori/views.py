from rest_framework import generics
from api.kategori.serializers import KategoriSerializer
from produk.models import Kategori


class KategoriList(generics.ListAPIView):
	queryset = Kategori.objects.all()
	serializer_class = KategoriSerializer