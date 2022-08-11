from django.db.models.signals import (
    post_save,
)
from django.dispatch import receiver

from cart.models import (
    CartProduct,
    Cart
)
from .models import Order


@receiver(post_save, sender=Order)
def order_post_save_signal(sender, instance, *args, **kwargs):
    """
    Сигнал отслеживания изменения ManyToMany поля
    и проводящий расчёты в корзине
    """
    if instance.status_order == 'completed':
        for prod in instance.products_in_order.all():
            if prod in CartProduct.objects.all():
                prod.delete()
        cart = Cart.objects.all()
        if cart.exists():
            cart.delete()
