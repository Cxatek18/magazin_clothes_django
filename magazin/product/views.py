from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
)
from .models import (
    Product,
    Category,
)


class HomeProductView(ListView):
    """
    Вывод списка всех продуктов на главной странице
    """
    model = Product
    context_object_name = 'products'
    template_name = 'product/index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_head'] = 'Главная страница'
        return context

    def get_queryset(self):
        return Product.objects.filter(status="Have")


class CategoriesView(ListView):
    """
    Вывод списка всех каттегорий на главной странице
    """
    model = Product
    context_object_name = 'products'
    template_name = 'product/index.html'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_head'] = Category.objects.get(
                                pk=self.kwargs['category_id']
                            )
        return context

    def get_queryset(self):
        return Product.objects.filter(
            category_id=self.kwargs['category_id'],
        )


class ProductDetailView(DetailView):
    """
    Вывод ифнормации о отдельном продукте на отдельной странице
    """
    model = Product
    template_name = 'product/detail_product.html'
    slug_url_kwarg = 'product_slug'
    context_object_name = 'product'
