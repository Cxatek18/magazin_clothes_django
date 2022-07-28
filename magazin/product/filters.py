import django_filters
from .models import (
    ProductColor,
)


class ProductFilter(django_filters.FilterSet):
    """
    Фильтры товаров
    """

    CHOICES_GENDER = (
        ('Male', 'Мужчины'),
        ('Female', 'Женщины'),
        ('Unisex', 'Унисекс'),
    )

    product_name = django_filters.CharFilter(
        field_name='product_name',
        lookup_expr='icontains',
        label='Название товара',
    )

    price__gt = django_filters.NumberFilter(
        field_name='price_now', lookup_expr='gt',
        label='Цена товара от',
    )

    price__lt = django_filters.NumberFilter(
        field_name='price_now', lookup_expr='lt',
        label='Цена товара до',
    )

    gender = django_filters.ChoiceFilter(
        field_name='gender',
        choices=CHOICES_GENDER,
        label='Пол',
        empty_label='Не выбранно',
    )

    colors = django_filters.ModelMultipleChoiceFilter(
        field_name='colors__color',
        to_field_name='color',
        queryset=ProductColor.objects.all(),
        label='Цвет',
    )
