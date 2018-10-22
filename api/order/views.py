from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from api.order.serializers import OrderSerializer
from produk.models import Order
from rest_framework import permissions
from api.permissions import IsAdminOrReadOnly


class OrderList(generics.ListCreateAPIView):
	queryset = Order.objects.all()
	serializer_class = OrderSerializer
	permission_classes = (permissions.IsAuthenticated,)
	filter_backends = (DjangoFilterBackend,)
	filter_fields = ('user',)


# class OrderDetail(generics.RetrieveUpdateDestroyAPIView):

# 	queryset = Order.objects.all()
# 	serializer_class = OrderSerializer
# 	permission_classes = (permissions.IsAuthenticated,)