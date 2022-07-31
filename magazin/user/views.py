from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import (
    View,
)

from .forms import (
    UserRegisterForm,
)
from .services.user_controller import (
    UserController,
)


class UserRegister(View):
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

                    new_user.set_password(form.cleaned_data['password1'])
                    new_user.ip_address = UserController.get_ip_address_user(
                        request
                    )
                    new_user.save()
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
