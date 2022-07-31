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
