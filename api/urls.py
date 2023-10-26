from django.urls import path 
from . import views
urlpatterns = [
    path('product-list/',views.product_list,name='product_list'),
    path('get-product/<str:pk>/',views.update_product,name="update_product")
]
 
