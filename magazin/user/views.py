from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout
from django.views.generic import (
    View,
)

from .forms import (
    UserRegisterForm,
    UserLoginForm,
)
from .services.user_controller import (
    UserController,
)


class UserRegisterView(View):
    """
    Регистрация пользователя
    """
    def get(self, request, *args, **kwargs):
        """
        Получение формы для регистрации пользователя
        """
        context = {
            'form_register_user': UserRegisterForm,
            'title_head': 'Регистарция'
        }

        return render(
            request, 'user/register.html',  context
        )

    def post(self, request, *args, **kwargs):
        """
        Регистрация пользователя
        """
        if request.method == 'POST':
            form = UserRegisterForm(request.POST)

            if form.is_valid():

                new_user = form.save(commit=False)
                password_1 = form.cleaned_data['password1']
                password_2 = form.cleaned_data['password2']

                if password_1 == password_2:

                    new_user.ip_address = UserController.get_ip_address_user(
                        request
                    )
                    new_user.save()
                    messages.error(request, 'Вы успешно зарегестрировались')
                    return redirect('home')

                else:
                    messages.error(request, 'Ошибка регистрации')
                    return redirect('register_user')

            else:
                messages.error(request, 'Ошибка регистрации')
                return redirect('register_user')

        else:
            form = UserRegisterForm()
        return render(request, 'user/register.html', {'form': form})


class UserLoginView(View):
    """
    Авторизация пользователя
    """
    def get(self, request, *args, **kwargs):
        """
        Получение формы для авторизации пользователя
        """
        context = {
            'form_login_user': UserLoginForm,
            'title_head': 'Авторизация'
        }

        return render(
            request, 'user/user_login.html',  context
        )

    def post(self, request, *args, **kwargs):
        """
        Метод post для авторизации пользователя
        """
        if request.method == 'POST':
            form = UserLoginForm(request, data=request.POST)
            if form.is_valid():
                user = form.get_user()
                if user:
                    login(request, user)
                    messages.success(request, f'Привет {user.username}')
                    return redirect('home')
                else:
                    messages.error(request, 'Ошибка входа')
                    return render(
                        request, 'user/user_login.html', {'form': form}
                    )
            else:
                messages.error(request, 'Ошибка входа')
        else:
            form = UserLoginForm()
        return render(request, 'user/user_login.html', {'form': form})
