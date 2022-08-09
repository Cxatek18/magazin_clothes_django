from django.shortcuts import render
from django.views.generic import (
    View,
)
from .forms import (
    OrderForm
)


class OrderAllProductCart(View):
    """
    Оформление заказа на все товары в корзине
    """
    def get(self, request, *args, **kwargs):

        context = {
            'form': OrderForm,
        }

        return render(
            request, 'order/order_product.html', context
        )
