class ProductController():
    """
    Класс контролер для продуктов.
    """

    @staticmethod
    def putting_product_info_in_form(prod, form_prod, form_img_prod, img_prod):

        """
        Подставляем данные продукта в форму
        """
        form_product = form_prod(
            initial={
                "product_name": prod.product_name,
                "category": prod.category,
                "brand_product": prod.brand_product,
                "description": prod.description,
                "full_price": prod.full_price,
                "discounted_price": prod.discounted_price,
                "quantity": prod.quantity,
                "status": prod.status,
            }
        )

        form_product_image = form_img_prod(
            initial={
                "image": img_prod.image,
                "products": prod,
            }
        )

        context = {
            'form_product': form_product,
            'form_product_image': form_product_image,
            'product': prod,
        }

        return context

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
            product_obj.brand_product = form_product.cleaned_data[
                'brand_product'
            ]
            product_obj.description = form_product.cleaned_data['description']
            product_obj.full_price = form_product.cleaned_data['full_price']
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

    def update_product(self, form_product, form_img_prod, product, prod_img):
        """
        Метод обновления продукта.
        для начала получаем форму в которой
        стоит информация о продукте,
        затем обновляем продукт с новой информацией.
        """
        if form_product.is_valid():
            product.product_name = form_product.cleaned_data[
                'product_name'
            ]
            product.category = form_product.cleaned_data['category']
            product.brand_product = form_product.cleaned_data[
                'brand_product'
            ]
            product.description = form_product.cleaned_data['description']
            product.full_price = form_product.cleaned_data['full_price']
            product.discounted_price = form_product.cleaned_data[
                'discounted_price'
            ]
            product.quantity = form_product.cleaned_data['quantity']
            product.status = form_product.cleaned_data['status']
            product.save()

            if form_img_prod.is_valid():
                if form_img_prod.cleaned_data['image'] is not None:
                    prod_img.image = form_img_prod.cleaned_data[
                        'image'
                    ]
                else:
                    prod_img.image = prod_img.image
                prod_img.products = product
                prod_img.save()
            else:
                return False

        else:
            return False
        return True
