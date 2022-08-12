from django.db import models


class Stock(models.Model):
    """
    Модель акция
    """
    stock_name = models.CharField(
        verbose_name='Название акции',
        max_length=255,
    )
    products_in_stock = models.ManyToManyField(
        'product.Product',
        verbose_name='Продукты в акции',
        related_name='products_in_stock'
    )
    image_stock = models.ImageField(
        verbose_name='Банер акции',
        blank=True,
        upload_to='stock/%Y/%m/%d/',
        default='product/system_img/default.jpg',
    )

    def __str__(self):
        return self.stock_name

    class Meta:
        verbose_name = 'Stock'
        verbose_name_plural = 'Stocks'
