from django.shortcuts import render, redirect
from django.contrib import messages

from django.views.generic import (
    View,
)
from product.models import Product
from .models import (
    Cart,
    CartProduct,
)
from .services.cart_controller import (
    CartController
)
from .services.cart_calculator import (
    CartCalculator
)


class AddProductInCartView(View):
    def post(self, request, *args, **kwargs):
        """
        Добавление продукта в корзину.
        """
        user = request.user
        prod_obj = Product.objects.get(
            id=kwargs.get('pk')
        )
        cart = Cart.objects.filter(user_name=user).first()

        add_product_in_cart = CartController.add_product_in_cart(
            cart, Cart, user, prod_obj, CartProduct
        )
        if add_product_in_cart is False:
            messages.error(request, 'Такой товар уже есть в корзине')
            return redirect('home')
        else:
            messages.success(
                request,
                f'Вы успешно добавили товар - \
                    {prod_obj.product_name} в корзину'
            )
            return redirect('home')


class ListProductInCartView(View):
    """
    Список продуктов в корзине
    """
    def get(self, request, *args, **kwargs):
        cart = Cart.objects.filter(user_name=request.user).first()
        if not cart:
            context = {
                'cart_info': False,
                'title_head': 'Список продуктов в корзине'
            }
        else:
            context = {
                'cart_info': cart,
                'title_head': 'Список продуктов в корзине',
            }

        return render(
            request, 'cart_templates/list_product_in_cart.html', context
        )


class DeleteProductFromCartView(View):
    """
    Удаление продукта из корзины.
    """
    def post(self, request, *args, **kwargs):

        user = request.user
        cart = Cart.objects.filter(user_name=user).first()
        cart_product = CartProduct.objects.get(
            pk=kwargs.get('pk')
        )
        cart.products_in_cart.remove(cart_product)
        if cart.products_in_cart.all().exists() is False:
            cart.delete()
        cart_product.delete()
        messages.success(
            request,
            'Вы успешно удалил товар из корзины'
        )
        return redirect('home')


class ChangeQtyProductInCartView(View):
    """
    Изменение количества товара в корзине
    """
    def post(self, request, *args, **kwargs):
        user = request.user
        cart_product = CartProduct.objects.get(
            pk=kwargs.get('pk')
        )
        cart = Cart.objects.filter(user_name=user).first()

        if request.method == 'POST':
            if int(request.POST.get('product_count')) <= 0:
                messages.error(
                    request,
                    'Вы добавляете отрицательное число'
                )
                return redirect('list_product_in_cart')
            else:
                cart_product.count_product = int(
                    request.POST.get('product_count')
                )
                cart_product.save()
                cart_calculator = CartCalculator()
                cart_calculator.cart_calculation(cart)
                cart.save()
                messages.success(
                    request,
                    'Вы успешно поменяли количество товара'
                )
                return redirect('list_product_in_cart')
