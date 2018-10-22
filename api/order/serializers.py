from rest_framework import serializers
from produk.models import Order


class OrderSerializer(serializers.ModelSerializer):
	class Meta:
		model = Order
		fields = '__all__'