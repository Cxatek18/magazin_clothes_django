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
                "gender": prod.gender,
                "colors": prod.colors.all(),
                "product_size": prod.product_size.all(),
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

    @staticmethod
    def product_submission_to_form_product_img(prod, form_img_prod):
        """
        Подставление товара для которого будет создано фото
        """
        form_product_image = form_img_prod(
            initial={
                "image": '',
                "products": prod,
            }
        )

        context = {
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
            product_obj.gender = form_product.cleaned_data['gender']
            product_obj.save()
            product_obj.colors.set(
                form_product.cleaned_data['colors']
            )
            product_obj.product_size.set(
                form_product.cleaned_data['product_size']
            )
            form_product.save_m2m()

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
            product.gender = form_product.cleaned_data['gender']
            product.colors.set(
                form_product.cleaned_data['colors']
            )
            product.product_size.set(
                form_product.cleaned_data['product_size']
            )
            product.save()

            if form_img_prod.is_valid():
                default_img_prod = 'product/system_img/default.jpg'
                if form_img_prod.cleaned_data['image'] is not False:
                    if form_img_prod.cleaned_data['image'] != default_img_prod:
                        prod_img.image = form_img_prod.cleaned_data['image']
                    else:
                        prod_img.image = prod_img.image
                else:
                    prod_img.image = default_img_prod
                prod_img.products = product
                prod_img.save()
            else:
                return False
        else:
            return False
        return True

    def add_photo_product(self, form_product_image, prod):
        """
        Метод подставления нужной информации для создания
        фото определённого продукта
        """
        if form_product_image.is_valid():
            product_img_obj = form_product_image.save(commit=False)
            product_img_obj.image = form_product_image.cleaned_data[
                'image'
            ]
            product_img_obj.products = prod
            product_img_obj.save()
            return True
        else:
            return False

    def delete_default_photo_when_adding_photo(self, list_photo):
        """
        При добавлении фото
        если у нас стояло дефолтное фото то мы его находим
        и удаляем и ставим новое которое добавили.
        сделано для того чтоб если у продукта есть хоть какое то фото,
        то нам не надо хранить дефолтное
        """
        if list_photo.count() > 1:
            list_photo.get(image='product/system_img/default.jpg').delete()
            return True

    def add_product_to_favorite(self, request, user, prod_cls, favorite_cls):
        """
        Добавление продукта в избранное
        """
        if request.method == 'POST':
            product_id = request.POST.get('product_id')
            product_obj = prod_cls.objects.get(id=product_id)

            if user in product_obj.favorite_products.all():
                product_obj.favorite_products.remove(user)
            else:
                product_obj.favorite_products.add(user)

            favorite_products, created = favorite_cls.objects.\
                get_or_create(
                    user=user, product_id=product_id
                )

            favorite_products.save()
