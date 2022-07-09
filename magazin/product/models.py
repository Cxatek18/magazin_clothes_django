from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse
from autoslug import AutoSlugField


class Product(models.Model):

    STATUS_PRODUCT = [
        ('Have', 'Есть в наличии'),
        ('Havent', 'Временно отсутвует'),
    ]

    product_name = models.CharField(
        verbose_name='Название товара',
        max_length=255,
    )
    slug = AutoSlugField(
        populate_from='product_name'
    )
    category = models.ForeignKey(
        'Category', verbose_name='Категория',
        on_delete=models.PROTECT,
        related_name='category_product',
    )
    created_at = models.DateTimeField(
        verbose_name='Дата создания',
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        verbose_name='Дата обновления',
        auto_now=True,
    )
    description = models.TextField(
        verbose_name='Описание',
        blank=True,
    )
    price_now = models.IntegerField(
        verbose_name='Цена',
        blank=True,
        null=True,
    )
    discounted_price = models.IntegerField(
        verbose_name='Скидка',
        blank=True,
        null=True,
        validators=[MinValueValidator(0), MaxValueValidator(2147483647)]
    )
    quantity = models.PositiveIntegerField(
        verbose_name='Товаров в наличии',
        default=0,
    )
    status = models.CharField(
        verbose_name='Статус товара',
        choices=STATUS_PRODUCT,
        default='Havent',
        max_length=120,
    )
    photo = models.ManyToManyField(
        'ProductImage',
        verbose_name='Фотографии',
        related_name='product_photos'
    )
    colors = models.ManyToManyField(
        'ProductColor',
        verbose_name='Цвета',
        related_name='product_colors',
        blank=True,
    )

    def __str__(self):
        return self.product_name

    def get_absolute_url(self):
        return reverse('view_product', kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
        if self.discounted_price:
            self.price_now = self.price_now - self.discounted_price
        else:
            self.price_now = self.price_now
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ['-created_at']


class Category(models.Model):
    category_name = models.CharField(
        verbose_name='Категория',
        max_length=120
    )
    slug_category = AutoSlugField(
        populate_from='category_name',
    )

    def get_absolute_url(self):
        return reverse(
            'category', kwargs={'slug_category': self.slug_category}
        )

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class ProductImage(models.Model):
    image = models.ImageField(
        verbose_name='Фото',
        blank=True,
        upload_to='product/%Y/%m/%d/'
    )

    def get_absolute_url(self):
        return reverse('image_url', kwargs={'productimage_id': self.pk})

    def __str__(self):
        return str(self.image)


class ProductColor(models.Model):
    color = models.CharField(
        verbose_name='Цвет',
        max_length=255,
        unique=True,
    )

    def get_absolute_url(self):
        return reverse('color_url', kwargs={'productcolor_id': self.pk})

    def __str__(self):
        return self.color
