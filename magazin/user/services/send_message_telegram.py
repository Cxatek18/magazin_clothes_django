from django.conf import settings

import requests


class MessageSenderTelegram():
    """
    Класс отправщика сообщений в телеграм
    """
    def send_message_contact_with_me(self, form):
        msg = f'\
            #Обращение\n\nТема: {form.cleaned_data["subject"]}\n\n\
Текст: {form.cleaned_data["text"]}\n\n\
Cвязь: {form.cleaned_data["connection"]}'
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
