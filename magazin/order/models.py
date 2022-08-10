from django.db import models


class Order(models.Model):
    """
    Модель заказа
    """
    STATUS_NEW = 'new'
    STATUS_IN_PROGRESS = 'in_progress'
    STATUS_READY = 'is_ready'
    STATUS_COMPLITED = 'completed'

    BUY_TYPE_SELF = 'self'
    BUY_TYPE_DELIVERY = 'delivery'

    STATUS_CHOICES = (
        (STATUS_NEW, 'Новый заказ'),
        (STATUS_IN_PROGRESS, 'Заказ в обработке'),
        (STATUS_READY, 'Заказ готов'),
        (STATUS_COMPLITED, 'Заказ выполнен'),
    )

    BUYING_TYPE_CHOICES = (
        (BUY_TYPE_SELF, 'Самовывоз'),
        (BUY_TYPE_DELIVERY, 'Доставка'),
    )

    user_name = models.ForeignKey(
        'user.User', on_delete=models.CASCADE,
        verbose_name='Пользователь сделавший заказ',
        related_name='user_order',
    )
    first_name = models.CharField(
        verbose_name='Имя',
        max_length=255,
    )
    last_name = models.CharField(
        verbose_name='Фамилия',
        max_length=255,
    )
    phone_number = models.CharField(
        verbose_name='Телефон',
        max_length=20,
    )
    address = models.CharField(
        verbose_name='Адрес',
        max_length=1024,
        null=True,
        blank=True,
    )
    products_in_order = models.ManyToManyField(
        'cart.CartProduct',
        verbose_name='Заказаные товары',
        related_name='products_in_order',
    )
    status_order = models.CharField(
        verbose_name='Статус заказа',
        max_length=100,
        choices=STATUS_CHOICES,
        default=STATUS_NEW
    )
    buying_type = models.CharField(
        verbose_name='Тип заказа',
        max_length=100,
        choices=BUYING_TYPE_CHOICES,
        default=BUY_TYPE_SELF,
    )
    comment = models.TextField(
        verbose_name='Комментарий к заказу',
        null=True, blank=True
    )
    total_products = models.IntegerField(
        verbose_name='Общее количество товаров в заказе',
        default=0,
        null=True,
    )
    final_price_order = models.IntegerField(
        verbose_name='Общая сумма всех товаров в заказе',
        default=0,
        null=True,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата заказа'
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата обновления заказа'
    )

    def __str__(self):
        return str(self.first_name)

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'
