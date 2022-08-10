from django.db.models.signals import (
    m2m_changed,
)
from django.dispatch import receiver

from .models import (
    Cart,
)
from .services.cart_calculator import CartCalculator


@receiver(m2m_changed, sender=Cart.products_in_cart.through)
def cart_m2m_changed_save_signal(sender, instance, action, *args, **kwargs):
    """
    Сигнал отслеживания изменения ManyToMany поля
    и проводящий расчёты в корзине
    """
    if action == 'post_add' or action == 'post_remove':
        cart_calculator = CartCalculator()
        cart_calculator.cart_calculation(instance)
        instance.save()
