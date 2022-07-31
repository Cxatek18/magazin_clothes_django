from django import forms
from django.contrib.auth.forms import (
    UserCreationForm,
    AuthenticationForm,
)

from .models import (
    User,
)


class UserRegisterForm(UserCreationForm):
    """
    Форма для регистарции пользователя
    """
    username = forms.CharField(
        label='Имя пользователя',
        widget=forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'autocomplete': 'off'
                }
            ),
        help_text='Имя пользователя не должно превыщать 120 символов'
    )
    password1 = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'autocomplete': 'off',
            }
        ),
    )
    password2 = forms.CharField(
        label='Подтверждение пароля',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'autocomplete': 'off',
            }
        ),
    )
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={'class': 'form-control'}),
    )

    class Meta:
        model = User
        fields = (
            'username', 'email', 'password1',
            'password2',
        )


class UserLoginForm(AuthenticationForm):
    """
    Форма для авторизации пользователя
    """
    username = forms.CharField(
        label='Логин',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'autocomplete': 'off'
            }
        ),
    )
    password = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )


class ContactFormTelegram(forms.Form):
    """
    Форма для связи со мной
    (связь реализована через телеграм)
    """
    CONTACT_SUBJECT = [
        ('Tech_problem', 'Техническая проблема'),
        ('Order', 'Заказ'),
        ('Payment', 'Оплата'),
        ('Cooperation', 'Сотруднечество'),
        ('Certificates', 'Сертефикаты'),
        ('Another_reason', 'Другая причина'),
    ]

    subject = forms.CharField(
        label='Тема письма',
        widget=forms.Select(
            attrs={'class': 'form-control'},
            choices=CONTACT_SUBJECT
        )
    )
    text = forms.CharField(
        label='Текст письма',
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5})
    )
    connection = forms.CharField(
        label='Как с вами связаться',
        help_text='Ссылка на вашу соцсеть для связи или ваша почта',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
