from django.urls import path, re_path
from api.kategori.views import KategoriList, KategoriDetail


urlpatterns = [
    path('', KategoriList.as_view(), name='kategori-list'),
    re_path(r'^(?P<pk>[0-9]+)/$', KategoriDetail.as_view(),
            name='kategori-detail'),
]
