from django.urls import path
from .import views

from django.conf import settings

urlpatterns = [
    path('farmersInfo', views.get_farmers_info, name='farmers_info'),
    path('create', views.create_products, name='create_products'),
    path('<int:pk>/', views.get_products_by_id, name='product_by_id'),
    path('productInfo', views.get_products, name='products'),
]

