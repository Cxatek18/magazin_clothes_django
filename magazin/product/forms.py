from django import forms
from .models import (
    Product,
    ProductImage,
)


class ProductForm(forms.ModelForm):
    """
    Форма для продукта
    """

    class Meta:
        model = Product
        fields = [
            'product_name', 'category', 'brand_product',
            'description', 'full_price', 'discounted_price',
            'quantity', 'status',
        ]

        widgets = {
            'product_name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(
                attrs={'class': 'form-control', 'rows': 5}
            ),
            'category': forms.Select(attrs={'class': 'form-control'},),
            'brand_product': forms.Select(attrs={'class': 'form-control'},),
            'full_price': forms.TextInput(attrs={'class': 'form-control'},),
            'discounted_price': forms.TextInput(
                attrs={'class': 'form-control'}
            ),
            'status': forms.Select(attrs={'class': 'form-control'},),
        }


class ProductImageForm(forms.ModelForm):
    """
    Форма для фото продукта
    """

    class Meta:
        model = ProductImage
        fields = [
            'image', 'products',
        ]

        widgets = {
            'products': forms.HiddenInput(),
        }

    def __init__(self, *args, **kwargs):
        super(ProductImageForm, self).__init__(*args, **kwargs)
        self.fields['products'].required = False
        self.fields['image'].required = 'product/system_img/default.jpg'
