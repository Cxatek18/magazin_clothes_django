from django.shortcuts import render, redirect
from django.views.generic import (
    ListView,
    DetailView,
    View,
    # TemplateView,
)
from .models import (
    Product,
    Category,
)
from .forms import (
    ProductForm,
    ProductImageForm,
)
from .services.product_controller import (
    ProductController,
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


class ProductManagementView(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'product/admin_templates/product_management.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_head'] = 'Управление продуктами'
        return context

    # def get_queryset(self):
    #     return Product.objects.filter(status="Have")


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


class ProductCreateView(View):

    def get(self, request, *args, **kwargs):
        """
        Получение всех форм для создания продукта
        """
        form_class_product = ProductForm
        form_class_product_image = ProductImageForm

        context = {
            'form_class_product': form_class_product,
            'form_class_product_image': form_class_product_image,
        }

        return render(
            request, 'product/admin_templates/product_create.html', context
        )

    def post(self, request, *args, **kwargs):
        """
        Создание продукта
        """
        form_product = ProductForm(request.POST or None)
        form_product_image = ProductImageForm(request.POST, request.FILES)
        prod_controller = ProductController()
        if prod_controller.creating_product(
            form_product, form_product_image
        ) is False:
            return redirect('create_product')
        else:
            return redirect('home')
