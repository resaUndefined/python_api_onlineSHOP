from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from api.produk.serializers import ProdukSerializer
from produk.models import Produk
from rest_framework import permissions
from api.permissions import IsAdminOrReadOnly


class ProdukList(generics.ListCreateAPIView):
    queryset = Produk.objects.all()
    serializer_class = ProdukSerializer
    permission_classes = (IsAdminOrReadOnly,)
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('kategori',)


class ProdukDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Produk.objects.all()
    serializer_class = ProdukSerializer
    permission_classes = (IsAdminOrReadOnly,)
