class OrderController():
    """
    Класс контролер для заказа.
    """
    def replacing_in_order_with_True(self, order, cart):
        """
        Замена статуса in_order на True
        товара в корзине
        """
        for prod in order.products_in_order.all():
            if prod in cart.products_in_cart.all():
                prod.in_order = True
                prod.save()
                cart.final_price_cart -= prod.final_price
                cart.total_discount_price -= prod.final_total_discount
                cart.total_not_discount_price -= prod.final_price_not_discount
                cart.total_products -= prod.count_product
        cart.save()
        return True

    def subtracting_qty_product_from_availability(self, order, product_cls):
        """
        Уменьшение количетсва продукта в наличии
        если был переведён в статус заказа
        """
        for prod in order.products_in_order.all():
            prod_main = product_cls.objects.get(pk=prod.product_name_id)
            prod_main.quantity -= prod.count_product
            prod_main.save()
