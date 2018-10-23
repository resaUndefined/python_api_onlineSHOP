from rest_framework import serializers
from produk.models import Order, Order_Detail


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('no_hape', 'alamat', 'ongkosKirim',
                  'status', 'sub_total', 'total',)

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['user'] = user
        return super(OrderSerializer, self).create(validated_data)


class OrderBarangSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order_Detail
        fields = ('id', 'order', 'produk', 'harga', 'qty')
