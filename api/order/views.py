from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from api.order.serializers import (
    OrderGETSerializer,
    OrderPOSTSerializer,
    OrderBarangGETSerializer,
    OrderBarangPOSTSerializer,
    )
from produk.models import Order, Order_Detail
from api.permissions import IsAdminOrReadOnly


class OrderList(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderGETSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('status',)

    def get_queryset(self):
        # untuk menampilkan data order berdasarkan user yang login
        user = self.request.user
        orderUser = Order.objects.filter(user=user)
        return orderUser

        def get_serializer_class(self):
            if self.request.method in permissions.SAFE_METHODS:
                return OrderGETSerializer
            return OrderPOSTSerializer


class OrderDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Order.objects.all()
    serializer_class = OrderGETSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_serializer_class(self):
            if self.request.method in permissions.SAFE_METHODS:
                return OrderGETSerializer
            return OrderPOSTSerializer


class OrderBarangList(generics.ListCreateAPIView):
    queryset = Order_Detail.objects.all()
    serializer_class = OrderBarangGETSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_serializer_class(self):
        if self.request.method in permissions.SAFE_METHODS:
            return OrderBarangGETSerializer
        return OrderBarangPOSTSerializer

    def get_queryset(self):
        # untuk menampilkan data orderBarang berdasarkan id order
        pk = self.kwargs.get('pk')
        orders = Order_Detail.objects.filter(order=pk)
        return orders

    def get_serializer_context(self):
        # untuk mengirimkan context ke serializer
        pk = self.kwargs.get('pk')
        context = super(OrderBarangList, self).get_serializer_context()
        context['order_id'] = pk
        return context


class OrderBarangListDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Order_Detail.objects.all()
    serializer_class = OrderBarangGETSerializer
    permission_classes = (permissions.IsAuthenticated,)
    lookup_url_kwarg = 'barangid'

    def get_serializer_class(self):
            if self.request.method in permissions.SAFE_METHODS:
                return OrderBarangGETSerializer
            return OrderBarangPOSTSerializer