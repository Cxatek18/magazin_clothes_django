class OrderController():
    """
    Класс контролер для заказа.
    """
    def delete_prod_in_cart(self, order, cart):
        for prod in order.products_in_order.all():
            if prod in cart.products_in_cart.all():
                cart.products_in_cart.remove(prod)
                prod.delete()
        if cart.products_in_cart.all().exists() is False:
            cart.delete()
        return True
