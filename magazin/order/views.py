from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import (
    View,
    DeleteView,
    UpdateView,
)

from cart.models import Cart
from product.models import Product
from user.models import (
    Coupon,
)
from product.permissions import (
    UserAccessMixin
)

from .models import (
    Order,
)
from .forms import (
    OrderForm,
    UpdateUserOrderForm,
    UpdateAdminOrderForm,
)
from .services.order_calculator import (
    OrderCalculator,
)
from .services.order_controller import (
    OrderController,
)


class OrderAllProductCartView(View):
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
            if form.cleaned_data['coupon_code']:
                coupon = Coupon.objects.get(
                    code_сoupon=form.cleaned_data['coupon_code']
                )
                order.final_price_order -= coupon.discount_сoupon
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


class OrderOneProductInCartView(View):
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
            if form.cleaned_data['coupon_code']:
                coupon = Coupon.objects.get(
                    code_сoupon=form.cleaned_data['coupon_code']
                )
                order.final_price_order -= coupon.discount_сoupon
            order.save()
            order_conttroller = OrderController()
            order_conttroller.replacing_in_order_with_True(
                order, cart
            )
            order_conttroller.subtracting_qty_prod_from_availability(
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


class ListOrderView(View):
    """
    Вывод товаров в заказах
    """
    allow_empty = False

    def get(self, request, *args, **kwargs):
        if request.user.is_superuser or request.user.is_moderator:
            context = {
                'orders': Order.objects.all()
            }
            return render(
                request, 'order/list_product_order.html', context
            )
        else:
            context = {
                'orders': Order.objects.filter(
                    user_name=request.user
                )
            }
            return render(
                request, 'order/list_product_order.html', context
            )


class DeleteOrderView(DeleteView):
    """
    Удаление определённого заказа
    """
    model = Order
    success_url = '/'
    template_name = 'order/delete_order.html'
    raise_exception = True


class UpdateOrderUserView(UpdateView):
    """
    Обновление заказа с стороны пользователя
    """
    model = Order
    template_name = 'order/update_order_user.html'
    form_class = UpdateUserOrderForm
    context_object_name = 'order'
    raise_exception = True
    success_url = reverse_lazy('home')


class UpdateOrderAdminView(UserAccessMixin, UpdateView):
    """
    Обновление заказа с стороны админа
    """
    model = Order
    template_name = 'order/admin_template/update_order_admin.html'
    form_class = UpdateAdminOrderForm
    context_object_name = 'order'
    raise_exception = True
    success_url = reverse_lazy('home')
