from django import template
from product.models import (
    Category,
    ProductBrand,
)

register = template.Library()


@register.simple_tag
def get_categories():
    return Category.objects.all()


@register.inclusion_tag('product/list_categories.html')
def show_categories():
    categories = Category.objects.all()
    return {'categories': categories}


@register.inclusion_tag('product/list_brand.html')
def show_brand_product():
    brand = ProductBrand.objects.all()
    return {'brands': brand}
