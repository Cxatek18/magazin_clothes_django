class CartController():
    """
    Класс контролер для корзины
    """
    @staticmethod
    def add_product_in_cart(cart, cart_cls, user, prod_obj, cart_prod_cls):
        if not cart:
            cart = cart_cls.objects.create(user_name=user,)

        cart_products_all_title = cart.products_in_cart.all().values_list(
            'product_name__product_name', flat=True
        )

        if prod_obj.product_name in cart_products_all_title:
            return False

        cart_product, created = cart_prod_cls.objects.get_or_create(
            cart=cart, product_name=prod_obj,
            count_product=1,
        )

        if created:
            cart.products_in_cart.add(cart_product)

        return True
