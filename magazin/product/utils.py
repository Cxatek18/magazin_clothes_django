from django.core.paginator import Paginator


class ProductMixin():
    """
    Класс миксин для продукта
    """

    def get_filter_product(self, filter_product):
        filter_prod = filter_product(
            self.request.GET, queryset=self.get_queryset().filter(
                status="Have",
            )
        )
        return filter_prod

    def get_title_head_product(self, object_cls, search_element):
        title_head = object_cls.objects.get(
            pk=self.kwargs[search_element]
        )
        return title_head

    def pagination_product(self, request, filtered_products):

        paginated_filtered_products = Paginator(
            filtered_products.qs, 1
        )
        page_number = request.GET.get('page')
        product_page_obj = paginated_filtered_products.get_page(page_number)

        return product_page_obj
