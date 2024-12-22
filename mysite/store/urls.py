from .views import (ProductListViews, ProductDetailViews,
                    ProductCreateViews, ProductUpdateViews, ProductDeleteViews)
from django.urls import path


urlpatterns = [
    path('', ProductListViews.as_view(), name='product_list'),
    path('<int:pk>/', ProductDetailViews.as_view(), name='product_detail'),
    path('create/', ProductCreateViews.as_view(), name='Product_create'),
    path('<int:pk>/update/', ProductUpdateViews.as_view(), name='product_update'),
    path('<int:pk>/delete/', ProductDeleteViews.as_view(), name='product_delete'),

]