from rest_framework import generics
from rest_framework.exceptions import ValidationError
from rest_framework.generics import get_object_or_404

from rest_framework import mixins

from ebooks.models import Ebook , Review
from ebooks.api.serializers import EbookSerializer , ReviewSerializer

##impoer permission
from rest_framework import permissions
from ebooks.api.permission import IsAdminUserOrReadOnly , IsReviewAuthorOrReadOnly

class EbookListCreateAPIView(generics.ListCreateAPIView):
    queryset = Ebook.objects.all()
    serializer_class = EbookSerializer
    #adding permission
    # permission_classes =  [permissions.IsAuthenticatedOrReadOnly]
    permission_classes =  [IsAdminUserOrReadOnly]

class EbookDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ebook.objects.all()
    serializer_class = EbookSerializer
    #adding permission
    # permission_classes =  [permissions.IsAuthenticatedOrReadOnly]
    permission_classes =  [IsAdminUserOrReadOnly]

class ReviewCreateAPIView(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def perform_create(self,serializer):
        ebook_pk = self.kwargs.get("ebook_pk")
        ebook = get_object_or_404(Ebook,pk=ebook_pk)
        permission_classes =  [IsAuthenticatedOrReadOnly]
        
        review_author = self.request.user ## get current user auth
        
        review_queryset = Review.objects.filter(ebook=ebook,
                                                review_author=review_author) # checking if this user has already rate ebook?
        
        if review_queryset.exist():
            raise ValidationError("You Have Already Reviewed This Ebook!")
        
        serializer.save(ebook=ebook,review_author=review_author)

class ReviewDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsReviewAuthorOrReadOnly] ## adding permission


# class EbookListCreateAPIView(mixins.CreateModelMixin,mixins.ListModelMixin,generics.GenericAPIView):
#     queryset = Ebook.objects.all()

#     serializer_class = EbookSerializer

#     def get(self,request,*args, **kwargs):
#         return self.list(request, *args , **kwargs)
    
#     def post(self,request,*args, **kwargs):
#         return self.create(request, *args , **kwargs)