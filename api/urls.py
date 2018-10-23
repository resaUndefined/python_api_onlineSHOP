from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view
from rest_framework.authtoken import views
# from .views import login

schema_view = get_swagger_view(title='Toko Online API')

urlpatterns = [
    path('kategori/', include('api.kategori.urls')),
    path('produk/', include('api.produk.urls')),
    path('order/', include('api.order.urls')),
    path('docs/', schema_view),
    path('auth-token/', views.obtain_auth_token),
    # path('login/', login)
]
