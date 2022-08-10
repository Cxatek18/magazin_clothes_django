class OrderController():
    """
    Класс контролер для заказа.
    """
    def replacing_in_order_with_True(self, order, cart):
        """
        Удаление продукта из корзины если он в заказе,
        и удаление корзины если она пустая
        """
        for prod in order.products_in_order.all():
            if prod in cart.products_in_cart.all():
                prod.in_order = True
                prod.save()
        return True

    def subtracting_qty_product_from_availability(self, order, product_cls):
        for prod in order.products_in_order.all():
            prod_main = product_cls.objects.get(pk=prod.product_name_id)
            prod_main.quantity -= prod.count_product
            prod_main.save()
