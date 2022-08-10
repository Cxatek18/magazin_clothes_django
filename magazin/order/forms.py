from django import forms

from .models import (
    Order,
)


class OrderForm(forms.ModelForm):
    """
    Форма для оформления заказа
    """
    class Meta:
        model = Order
        fields = [
            'user_name', 'first_name', 'last_name',
            'phone_number', 'address', 'products_in_order',
            'buying_type', 'comment',
        ]

        widgets = {
            'user_name': forms.HiddenInput(),
            'first_name': forms.TextInput(
                attrs={'class': 'form-control'}
            ),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.NumberInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'},),
            'products_in_order': forms.SelectMultiple(
                attrs={
                    'class': 'form-control', 'size': 5,
                    'label': 'Товары которые вы заказываете:',
                },
            ),
            'buying_type': forms.Select(
                attrs={'class': 'form-control'}
            ),
            'comment': forms.Textarea(
                attrs={'class': 'form-control', 'rows': 5},
            )
        }
