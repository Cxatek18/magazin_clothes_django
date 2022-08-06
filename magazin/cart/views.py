from django.shortcuts import redirect
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
