from django.db.models import Sum


class CartCalculator:
    """
    Класс калькулятора для расчётов в корзине
    """
    @staticmethod
    def final_basket_price(cart):
        final_price_basket = cart.products_in_cart.values_list(
            'final_price', flat=True
        ).aggregate(Sum('final_price'))
        cart.final_price_cart = final_price_basket['final_price__sum']
        return True

    @staticmethod
    def total_products(cart):
        total_products = cart.products_in_cart.values_list(
            'count_product', flat=True
        ).aggregate(Sum('count_product'))
        cart.total_products = total_products['count_product__sum']
        return True

    @staticmethod
    def total_discount_products(cart):
        total_discount = cart.products_in_cart.values_list(
            'final_total_discount', flat=True
        ).aggregate(Sum('final_total_discount'))
        cart.total_discount_price = total_discount[
            'final_total_discount__sum'
        ]
        return True

    @staticmethod
    def total_price_not_discount_products(cart):
        total_price_not_discount = cart.products_in_cart.values_list(
            'final_price_not_discount', flat=True
        ).aggregate(Sum('final_price_not_discount'))
        cart.total_not_discount_price = total_price_not_discount[
            'final_price_not_discount__sum'
        ]
        return True

    def cart_calculation(self, cart):
        self.final_basket_price(cart)
        self.total_products(cart)
        self.total_discount_products(cart)
        self.total_price_not_discount_products(cart)
