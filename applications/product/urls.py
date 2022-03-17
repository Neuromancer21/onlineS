from django.urls import path

from .views import ProductListView, ProductDetailView

urlpatterns = [
    path('', ProductListView.as_view(), name='home-page'),
    path('product-detail/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
]