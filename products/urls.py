from django.urls import path
from . import views

urlpatterns = [
    path('', views.products, name="products"),
    path('products/create/', views.createProduct, name="create-product"),
    path('products/<str:pk>/edit', views.updateProduct, name="update-product"),
    path('products/<str:pk>/delete', views.deleteProduct, name="delete-product"),

    path('products/<str:pk>', views.product, name="product"),
]
