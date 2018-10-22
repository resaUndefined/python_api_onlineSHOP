from django.urls import path,re_path
from api.order_detail.views import Order_DetailList
# ,Order_DetailDetail


urlpatterns = [
	path('', Order_DetailList.as_view(), name='Detail-Order-list'),
    # re_path(r'^(?P<pk>[0-9]+)/$', Order_DetailDetail.as_view(), name='Detail-Order-detail'),
]