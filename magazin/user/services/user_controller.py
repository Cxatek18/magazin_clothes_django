class UserController():
    """
    Класс контроллера юзера
    """
    @staticmethod
    def get_ip_address_user(request):
        """
        Получение ip адресса пользователя
        """
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip_user = x_forwarded_for.split(',')[0]
        else:
            ip_user = request.META.get('REMOTE_ADDR')

        return ip_user
