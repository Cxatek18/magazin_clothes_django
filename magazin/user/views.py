from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from django.views.generic import (
    View,
    DetailView,
    UpdateView,
)

from .models import (
    User,
)
from .forms import (
    UserRegisterForm,
    UserLoginForm,
    ContactFormTelegram,
    UserInfoUpdateForm,
)
from .services.user_controller import (
    UserController,
)
from .services.send_message_telegram import (
    MessageSenderTelegram,
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
                    messages.success(request, 'Вы успешно зарегестрировались')
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


class UserLogoutView(View):
    """
    Выход из аккаунта
    """
    def get(self, request):
        logout(request)
        messages.success(request, 'Вы вышли из системы')
        return redirect('home')


class UserDetailView(DetailView):
    """
    Вывод данных пользователя в личном кабинете
    """
    model = User
    template_name = 'user/personal_account_user.html'
    context_object_name = 'user_info'
    extra_context = {
        'title_head': 'Личный кабинет',
    }
    raise_exception = True


class SendMessageToTelegramm(View):
    def get(self, request, *args, **kwargs):
        """
        Получение формы для связи
        (по телеграму)
        """
        context = {
            'form': ContactFormTelegram,
            'title_head': 'Обратная связь'
        }

        return render(
            request, 'user/contact_with_me.html',  context
        )

    def post(self, request, *args, **kwargs):
        """
        Отправка сообщения в телеграм
        """
        if request.method == 'POST':
            form = ContactFormTelegram(request.POST)
            if form.is_valid():
                message_sener = MessageSenderTelegram()

                if message_sener.send_message_contact_with_me(form) is True:
                    messages.success(request, 'Письмо успешно отправлено')
                    return redirect('contact_with_me')
                else:
                    messages.error(request, 'Ошибка отправки')
                    return redirect('contact_with_me')
            else:
                messages.error(request, 'Ошибка отправки')
                return redirect('contact_with_me')
        else:
            form = ContactFormTelegram()
        return render(request, 'user/contact_with_me.html', {'form': form})


class UserUpdateInfoView(UpdateView):
    """
    Обновление инофрмации пользователя
    """
    model = User
    template_name = 'user/update_info_user.html'
    form_class = UserInfoUpdateForm
    context_object_name = 'user_item'
    success_url = reverse_lazy('home')
    raise_exception = True
