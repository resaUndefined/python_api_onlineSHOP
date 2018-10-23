from django.urls import path, re_path
from api.order.views import OrderList, OrderDetail, OrderBarangList


urlpatterns = [
    path('', OrderList.as_view(), name='Order-list'),
    re_path(r'^(?P<pk>[0-9]+)/$', OrderDetail.as_view(), name='Order-detail'),
    re_path(r'^(?P<pk>[0-9]+)/barang$',
            OrderBarangList.as_view(), name='Order-Barang-List'),
]
