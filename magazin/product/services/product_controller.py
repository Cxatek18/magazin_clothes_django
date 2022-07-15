class ProductController():
    """
    Класс контролер для продуктов.
    """

    def creating_product(self, form_product, form_product_image):
        """
        Метод создание продукта.
        проверяем формы на валидность,
        получаем данные из формы и подставляем их для создания
        продукта.
        """
        if form_product.is_valid():
            product_obj = form_product.save(commit=False)
            product_obj.product_name = form_product.cleaned_data[
                'product_name'
            ]
            product_obj.category = form_product.cleaned_data['category']
            product_obj.description = form_product.cleaned_data['description']
            product_obj.price_now = form_product.cleaned_data['price_now']
            product_obj.discounted_price = form_product.cleaned_data[
                'discounted_price'
            ]
            product_obj.quantity = form_product.cleaned_data['quantity']
            product_obj.status = form_product.cleaned_data['status']
            product_obj.save()

            if form_product_image.is_valid():
                product_img_obj = form_product_image.save(commit=False)
                product_img_obj.image = form_product_image.cleaned_data[
                    'image'
                ]
                product_img_obj.products = product_obj
                product_img_obj.save()
            else:
                return False
        else:
            return False
        return True
