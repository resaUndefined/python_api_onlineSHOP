from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from api.order.serializers import OrderSerializer, OrderBarangSerializer
from produk.models import Order, Order_Detail
from rest_framework import permissions
from api.permissions import IsAdminOrReadOnly


class OrderList(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('user',)

    def get_queryset(self):
        user = self.request.user
        orderUser = Order.objects.filter(user=user)
        return orderUser


class OrderDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (permissions.IsAuthenticated,)


class OrderBarangList(generics.ListCreateAPIView):
    queryset = Order_Detail.objects.all()
    serializer_class = OrderBarangSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        orders = Order_Detail.objects.filter(order=pk)
        return orders
