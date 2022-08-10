from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import (
    View,
)

from .forms import (
    OrderForm
)
from cart.models import Cart
from product.models import Product
from .services.order_calculator import (
    OrderCalculator,
)
from .services.order_controller import (
    OrderController,
)


class OrderAllProductCart(View):
    """
    Оформление заказа на все товары в корзине
    """
    def get(self, request, *args, **kwargs):

        cart = Cart.objects.filter(user_name=request.user).first()

        form_order = OrderForm(
            initial={
                "user_name": request.user,
                "products_in_order": cart.products_in_cart.all()
            }
        )

        form_order.fields[
            'products_in_order'
        ].queryset = cart.products_in_cart.all()

        context = {
            'form': form_order,
        }

        return render(
            request, 'order/order_product.html', context
        )

    def post(self, request, *args, **kwargs):
        form = OrderForm(request.POST or None)
        cart = Cart.objects.filter(user_name=request.user).first()

        if form.is_valid():
            order = form.save()
            order_calc = OrderCalculator()
            order_calc.starting_order_calc(order)
            order.save()
            order_conttroller = OrderController()
            order_conttroller.replacing_in_order_with_True(
                order, cart
            )
            order_conttroller.subtracting_qty_product_from_availability(
                order, Product
            )
            messages.success(
                request, 'Вы успешно сделали заказ'
            )
            return redirect('home')

        else:
            messages.error(
                request, 'Ваш заказ не принят'
            )
            return redirect('home')


class OrderOneProductInCart(View):
    """
    Заказ одного продукта из корзины
    """
    def get(self, request, *args, **kwargs):
        cart = Cart.objects.filter(user_name=request.user).first()
        form_order = OrderForm(
            initial={
                "user_name": request.user,
                "products_in_order": cart.products_in_cart.get(
                    pk=kwargs.get('pk')
                )
            }
        )

        form_order.fields[
            'products_in_order'
        ].queryset = cart.products_in_cart.filter(
            pk=kwargs.get('pk')
        )

        context = {
            'form': form_order,
        }

        return render(
            request, 'order/order_one_product.html', context
        )

    def post(self, request, *args, **kwargs):
        form = OrderForm(request.POST or None)
        cart = Cart.objects.filter(user_name=request.user).first()

        if form.is_valid():
            order = form.save()
            order_calc = OrderCalculator()
            order_calc.starting_order_calc(order)
            order.save()
            order_conttroller = OrderController()
            order_conttroller.replacing_in_order_with_True(
                order, cart
            )
            order_conttroller.subtracting_qty_product_from_availability(
                order, Product
            )
            messages.success(
                request, 'Вы успешно сделали заказ'
            )
            return redirect('home')

        else:
            messages.error(
                request, 'Ваш заказ не принят'
            )
            return redirect('home')
