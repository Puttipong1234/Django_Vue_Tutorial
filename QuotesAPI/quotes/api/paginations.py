from rest_framework.pagination import PageNumberPagination

class SmallSetPagination(PageNumberPagination):
    page_size = 2 #maximum showing in 1 page