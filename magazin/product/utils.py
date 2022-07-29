class ProductMixin():
    """
    Класс миксин для продукта
    """
    def get_filter_product(self, filter_product):
        filter_prod = filter_product(
            self.request.GET, queryset=self.get_queryset().filter(
                status="Have"
            )
        )
        return filter_prod

    def get_title_head_product(self, object_cls, search_element):
        title_head = object_cls.objects.get(
            pk=self.kwargs[search_element]
        )
        return title_head
