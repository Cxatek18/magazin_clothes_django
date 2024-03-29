from django import template
from product.models import (
    Category,
    ProductBrand,
    ProductStock,
)

register = template.Library()


@register.simple_tag()
def my_url(value, field_name, urlencode=None):
    url = '?{}={}'.format(field_name, value)

    if urlencode:
        querystring = urlencode.split('&')
        filtered_querystring = filter(
            lambda p: p.split('=')[0] != field_name, querystring
        )
        encoded_querystring = '&'.join(filtered_querystring)
        url = '{}&{}'.format(url, encoded_querystring)

    return url


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


@register.inclusion_tag('product/list_product_by_stocks.html')
def show_stocks_product():
    stocks = ProductStock.objects.all()
    return {'stocks': stocks}
