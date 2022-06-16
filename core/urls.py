from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='home'),
    path('shop/', views.catalog, name='catalog'),
    path('product/', views.product_single, name='product-single')
]