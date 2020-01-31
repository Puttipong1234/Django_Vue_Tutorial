from rest_framework import generics

from quotes.models import Quote
from quotes.api.permissions import IsAdminUserOrReadOnly
from quotes.api.serializers import QuoteSerializer
from quotes.api.paginations import SmallSetPagination

class QuoteListCreateAPIView(generics.ListCreateAPIView):
    queryset = Quote.objects.all().order_by("-id")
    serializer_class = QuoteSerializer
    permission_classes = [IsAdminUserOrReadOnly]
    pagination_class = SmallSetPagination
    

class QuoteDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer
    permission_classes = [IsAdminUserOrReadOnly]
    