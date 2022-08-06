from django.conf import settings

import requests


class MessageProductSenderTelegram():
    """
    Класс отправщика покупок в один клик в телеграмм
    """
    def send_message_buy_one_click(self, form):

        msg = f'\
            #ПокупкаОдинКлик\n\nПродукт: \
{form.cleaned_data["product_name"]}\n\n\
Цена: {form.cleaned_data["full_price"]}\n\n\
Скидка: {form.cleaned_data["discounted_price"]}'

        for color in form.cleaned_data["colors"]:
            str_color = f"\n\nЦвет: {color}"
            msg += str_color

        for size in form.cleaned_data["product_size"]:
            str_size = f"\n\nРазмер: {size}"
            msg += str_size

        msg += f'\n\nТелефон: {form.cleaned_data["phone_user"]}'

        if msg:
            bot_api_key = settings.TELEGRAM_BOT_API_KEY
            channel_name = settings.TELEGRAM_BOT_CHANEL_NAME
            url = f'https://api.telegram.org/bot{bot_api_key}/sendMessage'

            params = {
                'chat_id': channel_name,
                'text': msg
            }

            requests.get(url, params=params).json()

            return True
        else:
            return False
