from django.http import Http404


class UserAccessMixin:
    """
    Класс для доступов к определённым страницам
    """

    def has_permission(self):
        if self.request.user.is_staff:
            return True

    def dispatch(self, request, *args, **kwargs):
        if not self.has_permission():
            raise Http404()
        return super().dispatch(request, *args, **kwargs)
