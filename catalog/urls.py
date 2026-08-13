from django.urls import path
from .views import HomeListView, ProductDetailView, ContactsView, ProductCreateView, ProductUpdateView
app_name = 'catalog'

urlpatterns = [
    path('', HomeListView.as_view(), name='home'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('create/', ProductCreateView.as_view(), name='product_create'),
    path('<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
]