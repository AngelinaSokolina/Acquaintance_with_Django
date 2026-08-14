from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Product
from .forms import ProductForm


class HomeListView(ListView):
    model = Product
    template_name = 'home.html'
    context_object_name = 'products'
    ordering = ['name']


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'


class ContactsView(TemplateView):
    template_name = 'contacts.html'


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:home')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'

    def get_queryset(self):
        user = self.request.user
        if user.has_perm('catalog.can_unpublish_product'):
            return Product.objects.all()
        return Product.objects.filter(owner=user)

    def get_success_url(self):
        return reverse_lazy('catalog:product_detail', kwargs={'pk': self.object.pk})


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:home')

    def get_queryset(self):
        user = self.request.user
        if user.has_perm('catalog.can_unpublish_product'):
            return Product.objects.all()
        return Product.objects.filter(owner=user)
