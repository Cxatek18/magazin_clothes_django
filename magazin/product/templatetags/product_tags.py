from django import template
from product.models import (
    Category,
    ProductBrand,
)

register = template.Library()


@register.inclusion_tag('product/list_categories.html')
def show_categories():
    categories = Category.objects.all()
    return {'categories': categories}


@register.inclusion_tag('product/list_brand.html')
def show_brand_product():
    brand = ProductBrand.objects.all()
    return {'brands': brand}


@register.inclusion_tag('product/list_categories_size.html')
def show_categories_size():
    categories = Category.objects.all()
    return {'category_sizes': categories}
