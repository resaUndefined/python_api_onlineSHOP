from rest_framework import generics
from api.produk.serializers import ProdukSerializer
from produk.models import Produk


class ProdukList(generics.ListAPIView):
	queryset = Produk.objects.all()
	serializer_class = ProdukSerializer