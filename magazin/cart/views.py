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


class AddProductInCart(View):
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


class ListProductInCart(View):
    """
    Список продуктов в корзине
    """
    def get(self, request, *args, **kwargs):
        cart = Cart.objects.get(user_name=f"{request.user.id}")
        context = {
            'cart_info': cart,
            'title_head': 'Список продуктов в корзине'
        }

        return render(
            request, 'cart_templates/list_product_in_cart.html', context
        )


class DeleteProductFromCart(View):
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
        cart_product.delete()
        messages.success(
            request,
            'Вы успешно удалил товар из корзины'
        )
        return redirect('home')
