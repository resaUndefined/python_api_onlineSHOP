from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from api.order_detail.serializers import Order_DetailSerializer
from produk.models import Order_Detail
from rest_framework import permissions
from api.permissions import IsAdminOrReadOnly


class Order_DetailList(generics.ListCreateAPIView):
	queryset = Order_Detail.objects.all()
	serializer_class = Order_DetailSerializer
	permission_classes = (permissions.IsAuthenticated,)
	filter_backends = (DjangoFilterBackend,)
	filter_fields = ('order',)


# class Order_DetailDetail(generics.RetrieveUpdateDestroyAPIView):

# 	queryset = Order_Detail.objects.all()
# 	serializer_class = Order_DetailSerializer
# 	permission_classes = (permissions.IsAuthenticated,)