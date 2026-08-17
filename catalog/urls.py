from django.urls import path
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie
from .views import (
    HomeListView,
    ProductDetailView,
    ContactsView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView,
    CategoryProductsView,
    CategoryListView,
    CategoryCreateView
)

app_name = 'catalog'

urlpatterns = [
    path('', HomeListView.as_view(), name='home'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('product/<int:pk>/', vary_on_cookie(cache_page(60 * 5)(ProductDetailView.as_view())), name='product_detail'),
    path('create/', ProductCreateView.as_view(), name='product_create'),
    path('<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('category/<int:category_id>/', CategoryProductsView.as_view(), name='category_products'),
    path('categories/', CategoryListView.as_view(), name='category_list'),
    path('category/create/', CategoryCreateView.as_view(), name='category_create'),
]
