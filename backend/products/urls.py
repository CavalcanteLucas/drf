from django.urls import path

from . import views

urlpatterns = [
    path('', views.ProductsMixinView.as_view(), name='product-list-create'),
    path('<int:pk>/update/', views.ProductUpdateAPIView.as_view(), name='product-update'),
    path('<int:pk>/delete/', views.ProductDeleteAPIView.as_view(), name='product-delete'),
    path('<int:pk>/', views.ProductsMixinView.as_view(), name='product-detail'),
]
