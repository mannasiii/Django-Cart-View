# from cart import views
# from django.urls import path, include

# app_name = 'cart'

# urlpatterns = [
#     # Other URL patterns
#     # path('cart/', cart_view, name='cart'),
#     path('cart/', views.cart_view, name='cart_view'),
# ]
# cart/urls.py

from django.urls import path
from . import views

app_name = 'cart'
urlpatterns = [
    path('add/', views.add_to_cart, name='add_to_cart'),
    path('remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('', views.cart_view, name='cart_view'),
]