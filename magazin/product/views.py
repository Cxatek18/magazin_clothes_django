from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    View,
    DeleteView,
    CreateView
)
from .models import (
    Product,
    Category,
    ProductBrand,
    ProductImage,
)
from .forms import (
    ProductForm,
    ProductImageForm,
    BrandProductCreateForm
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
    """
    Вывод списка продуктов для управления.
    (Управление продуктами)
    """

    model = Product
    context_object_name = 'products'
    template_name = 'product/admin_templates/product_management.html'
    extra_context = {
        'list_all_brand': ProductBrand.objects.all(),
    }

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_head'] = 'Управление продуктами'
        return context


class CategoriesView(ListView):
    """
    Вывод списка всех категорий на главной странице
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


class BrandsView(ListView):
    """
    Вывод списка всех брендов на главной странице
    """

    model = ProductBrand
    context_object_name = 'products'
    template_name = 'product/index.html'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_head'] = ProductBrand.objects.get(
                                pk=self.kwargs['brand_id']
                            )
        return context

    def get_queryset(self):
        return Product.objects.filter(
            brand_product_id=self.kwargs['brand_id'],
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


class UpdateProductView(View):
    def get(self, request, *args, **kwargs):

        """
        Выставление информации о продукте в форму
        """

        product = Product.objects.get(
            id=kwargs.get('pk')
        )
        product_image = ProductImage.objects.get(
            products_id=kwargs.get('pk')
        )

        context = ProductController.putting_product_info_in_form(
            product, ProductForm, ProductImageForm, product_image
        )

        return render(
            request, 'product/admin_templates/update_product.html', context
        )

    def post(self, request, *args, **kwargs):
        """
        Обновление продукта
        """

        form_product = ProductForm(request.POST or None)
        form_product_image = ProductImageForm(request.POST, request.FILES)
        product = Product.objects.get(
            id=kwargs.get('pk')
        )
        product_image = ProductImage.objects.get(
            products_id=kwargs.get('pk')
        )
        prod_controller = ProductController()
        if prod_controller.update_product(
            form_product, form_product_image,
            product, product_image
        ) is False:
            return redirect('update_product', product.id)
        else:
            return redirect('home')


class DeleteProductView(DeleteView):
    """
    Удаление определённого продукта
    """

    model = Product
    slug_url_kwarg = 'product_slug'
    success_url = '/'
    template_name = 'product/admin_templates/delete_product.html'
    raise_exception = True


class AddingProductPhoto(View):

    def get(self, request, *args, **kwargs):
        """
        Выставление нужного продукта в форму добавления
        фото к определённому продукту
        """

        product = Product.objects.get(
            slug=kwargs.get('product_slug')
        )

        context = ProductController.product_submission_to_form_product_img(
            product, ProductImageForm,
        )

        return render(
            request, 'product/admin_templates/add_photo_product.html', context
        )

    def post(self, request, *args, **kwargs):
        """
        Добавление фото к определённому продукту
        """

        form_product_image = ProductImageForm(request.POST, request.FILES)
        product = Product.objects.get(
            slug=kwargs.get('product_slug')
        )

        prod_controller = ProductController()
        if prod_controller.add_photo_product(
            form_product_image, product
        ) is False:
            return redirect('add_photo_product', kwargs.get('product_slug'))
        else:
            prod_controller.delete_default_photo_when_adding_photo(
                product.prodimg.all()
            )
            return redirect('home')


class CreateBrand(CreateView):
    """
    Создание бренда
    """

    model = ProductBrand
    template_name = 'product/admin_templates/create_brand.html'
    form_class = BrandProductCreateForm
    context_object_name = 'prod_brand'
    extra_context = {
        'title_head': 'Добавление бренда',
        'list_all_brand': ProductBrand.objects.all(),
    }
    success_url = reverse_lazy('home')
    raise_exception = True
