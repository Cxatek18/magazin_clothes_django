from django.db.models import Sum


class OrderCalculator():
    """
    Класс расчётов для заказа (калькулятор заказа)
    """
    @staticmethod
    def final_order_price(order):
        final_price_order_sum = order.products_in_order.values_list(
            'final_price', flat=True
        ).aggregate(Sum('final_price'))
        order.final_price_order = final_price_order_sum['final_price__sum']
        return True

    @staticmethod
    def number_of_ordered_items(order):
        order.total_products = order.products_in_order.count()
        return True

    def starting_order_calc(self, order):
        self.final_order_price(order)
        self.number_of_ordered_items(order)
