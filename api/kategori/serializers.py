from rest_framework import serializers
from produk.models import Kategori


class KategoriSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kategori
        fields = ('nama',)