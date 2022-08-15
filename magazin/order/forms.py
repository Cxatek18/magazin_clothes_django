from django import forms

from .models import (
    Order,
)


class OrderForm(forms.ModelForm):
    """
    Форма для оформления заказа
    """

    coupon_code = forms.CharField(
        label='Код купона',
        widget=forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
        help_text='Можно посмотреть в разделе "Купоны"',
        required=False,
    )

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
                },
            ),
            'buying_type': forms.Select(
                attrs={'class': 'form-control'}
            ),
            'comment': forms.Textarea(
                attrs={'class': 'form-control', 'rows': 5},
            )
        }


class UpdateUserOrderForm(forms.ModelForm):
    """
    Форма для обновления заказа с стороны пользователя
    """
    class Meta:
        model = Order
        fields = [
            'first_name', 'last_name',
            'phone_number', 'address',
            'buying_type', 'comment',
        ]

        widgets = {
            'first_name': forms.TextInput(
                attrs={'class': 'form-control'}
            ),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.NumberInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'},),
            'buying_type': forms.Select(
                attrs={'class': 'form-control'}
            ),
            'comment': forms.Textarea(
                attrs={'class': 'form-control', 'rows': 5},
            )
        }


class UpdateAdminOrderForm(forms.ModelForm):
    """
    Форма для обновления заказа с стороны админа
    """
    class Meta:
        model = Order
        fields = [
            'first_name', 'last_name',
            'phone_number', 'address',
            'buying_type', 'comment',
            'status_order',
        ]

        widgets = {
            'first_name': forms.TextInput(
                attrs={'class': 'form-control'}
            ),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.NumberInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'},),
            'buying_type': forms.Select(
                attrs={'class': 'form-control'}
            ),
            'comment': forms.Textarea(
                attrs={'class': 'form-control', 'rows': 5},
            ),
            'status_order': forms.Select(
                attrs={'class': 'form-control'}
            ),
        }
