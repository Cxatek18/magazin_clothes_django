import django_filters


class ProductFilter(django_filters.FilterSet):
    """
    Фильтры товаров
    """

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
