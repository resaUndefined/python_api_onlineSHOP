from rest_framework import serializers
from produk.models import Order_Detail


class Order_DetailSerializer(serializers.ModelSerializer):
	class Meta:
		model = Order_Detail
		fields = '__all__'