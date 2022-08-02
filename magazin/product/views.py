from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    View,
    DeleteView,
    CreateView,
    UpdateView,
    TemplateView,
)

from .models import (
    Product,
    Category,
    ProductBrand,
    ProductImage,
    ProductSize,
    FavoriteUserProduct,
)
from .forms import (
    ProductForm,
    ProductImageForm,
    BrandProductCreateForm,
    ProductImageUpdateForm,
    ProductUpdateImageForm,
)
from .services.product_controller import (
    ProductController,
)
from .filters import (
    ProductFilter,
)
from .utils import (
    ProductMixin,
)
from .permissions import (
    UserAccessMixin,
)


def handling_error_404(request, exception):
    """
    Кастомная страница для ошибки 404
    """
    return render(request, 'product/error_template/404_page.html', status=404)


def handling_error_403(request, exception):
    """
    Кастомная страница для ошибки 403
    """
    return render(request, 'product/error_template/403_page.html', status=403)


def handling_error_400(request, exception):
    """
    Кастомная страница для ошибки 400
    """
    return render(request, 'product/error_template/400_page.html', status=400)


class HomeProductView(ProductMixin, ListView):
    """
    Вывод списка всех продуктов на главной странице
    """
    model = Product
    template_name = 'product/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # фильтр товаров - self.get_filter_product(ProductFilter)
        # пагинатор товара - self.pagination_product
        context = {
            'filter': self.get_filter_product(ProductFilter),
            'product_page_obj': self.pagination_product(
                self.request, self.get_filter_product(ProductFilter)
            )
        }
        return context


class ProductManagementView(UserAccessMixin, ListView):
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


class CategoriesView(ProductMixin, ListView):
    """
    Вывод списка всех категорий на главной странице
    """
    model = Product
    context_object_name = 'products'
    template_name = 'product/index.html'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        # фильтр товаров - self.get_filter_product(ProductFilter)
        # пагинатор товара - self.pagination_product
        context = {
            'title_head': self.get_title_head_product(Category, 'category_id'),
            'filter': self.get_filter_product(ProductFilter),
            'product_page_obj': self.pagination_product(
                self.request, self.get_filter_product(ProductFilter)
            )
        }
        return context

    def get_queryset(self):
        return Product.objects.filter(
            category_id=self.kwargs['category_id'],
        )


class BrandsView(ProductMixin, ListView):
    """
    Вывод списка всех брендов на главной странице
    """
    model = ProductBrand
    context_object_name = 'products'
    template_name = 'product/index.html'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        # фильтр товаров - self.get_filter_product(ProductFilter)
        # пагинатор товара - self.pagination_product
        context = {
            'title_head': self.get_title_head_product(
                ProductBrand, 'brand_id'
            ),
            'filter': self.get_filter_product(ProductFilter),
            'product_page_obj': self.pagination_product(
                self.request, self.get_filter_product(ProductFilter)
            )
        }
        return context

    def get_queryset(self):
        return Product.objects.filter(
            brand_product_id=self.kwargs['brand_id'],
        )


class SizeProductView(ProductMixin, ListView):
    """
    Вывод списка всех товаров по размеру
    """
    model = Product
    context_object_name = 'products'
    template_name = 'product/index.html'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        # фильтр товаров - self.get_filter_product(ProductFilter)
        # пагинатор товара - self.pagination_product
        context = {
            'title_head': self.get_title_head_product(ProductSize, 'size_id'),
            'filter': self.get_filter_product(ProductFilter),
            'product_page_obj': self.pagination_product(
                self.request, self.get_filter_product(ProductFilter)
            )
        }
        return context

    def get_queryset(self):
        return Product.objects.filter(
            product_size__id=self.kwargs['size_id'],
        )


class ProductDetailView(DetailView):
    """
    Вывод ифнормации о отдельном продукте на отдельной странице
    """
    model = Product
    template_name = 'product/detail_product.html'
    slug_url_kwarg = 'product_slug'
    context_object_name = 'product'


class ProductCreateView(UserAccessMixin, View):

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


class UpdateProductView(UserAccessMixin, View):
    def get(self, request, *args, **kwargs):

        """
        Выставление информации о продукте в форму
        """
        product = Product.objects.get(
            id=kwargs.get('pk')
        )
        product_image = ProductImage.objects.filter(
            products_id=kwargs.get('pk')
        )

        context = ProductController.putting_product_info_in_form(
            product, ProductForm, ProductUpdateImageForm, product_image[0]
        )

        return render(
            request, 'product/admin_templates/update_product.html', context
        )

    def post(self, request, *args, **kwargs):
        """
        Обновление продукта
        """
        form_product = ProductForm(request.POST or None)
        form_product_image = ProductUpdateImageForm(
            request.POST, request.FILES
        )
        product = Product.objects.get(
            id=kwargs.get('pk')
        )
        product_image = ProductImage.objects.filter(
            products_id=kwargs.get('pk')
        )
        prod_controller = ProductController()
        if prod_controller.update_product(
            form_product, form_product_image,
            product, product_image[0]
        ) is False:
            return redirect('update_product', product.id)
        else:
            return redirect('home')


class DeleteProductView(UserAccessMixin, DeleteView):
    """
    Удаление определённого продукта
    """
    model = Product
    slug_url_kwarg = 'product_slug'
    success_url = '/'
    template_name = 'product/admin_templates/delete_product.html'
    raise_exception = True


class AddingProductPhoto(UserAccessMixin, View):

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
            prod_controller.delete_default_photo_when_adding_photo(
                product.prodimg.all()
            )
            return redirect('add_photo_product', kwargs.get('product_slug'))
        else:
            return redirect('home')


class CreateBrand(UserAccessMixin, CreateView):
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


class ListProductImageView(UserAccessMixin, View):
    """
    Вывод списка всех картинок товара
    """
    def get(self, request, *args, **kwargs):
        product = Product.objects.get(
            slug=kwargs.get('product_slug')
        )

        context = {
            "photos": product.prodimg.all()
        }

        return render(
            request, 'product/admin_templates/list_photo_product.html', context
        )


class UpdateProductImageView(UserAccessMixin, UpdateView):
    """
    Обновление определённого фото
    определённого продукта
    """
    model = ProductImage
    template_name = 'product/admin_templates/uprdate_photo_product.html'
    form_class = ProductImageUpdateForm
    context_object_name = 'photo'
    raise_exception = True
    success_url = reverse_lazy('home')


class AddProductToFavorite(View):
    """
    Добавление продукта в избранное
    """
    def post(self, request, *args, **kwargs):
        user = request.user
        prod_controller = ProductController()
        prod_controller.add_product_to_favorite(
            request, user, Product, FavoriteUserProduct,
        )
        return redirect('home')


class DeliveryAndPaymentView(TemplateView):
    """
    Страница доставки и оплаты
    """
    template_name = 'product/delevery_and_payment.html'
    extra_context = {'title_head': 'Доставка и оплата'}


class ExchangeAndRefundView(TemplateView):
    """
    Страница обмена и возврата
    """
    template_name = 'product/exchange_and_refund.html'
    extra_context = {'title_head': 'Обмен и возврат'}


class Page404Error(TemplateView):
    """
    Страница обмена и возврата
    """
    template_name = 'product/error_template/404_page.html'
    status = 404
    extra_context = {'title_head': 'Обмен и возврат'}


class FavoriteUserProductsView(TemplateView):
    """
    Страница вывода продуктов добавленых в избранное
    """
    template_name = 'product/favorite_product_user.html'
    extra_context = {'title_head': 'Избранные продукты'}
