from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from job.models import JobOffer
from job.api.serializers import JobOfferSerializer

class JobOfferListCreateAPIView(APIView):
    def get(self,request):
        joboffers = JobOffer.objects.filter()
        serializer = JobOfferSerializer(joboffers , many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = JobOfferSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class JobOfferDetailAPIView(APIView):

    def get_object(self,pk):
        joboffers = get_object_or_404(JobOffer,pk=pk)
        return joboffers
    
    def get(self,request,pk):
        joboffers = self.get_object(pk)
        serializer = JobOfferSerializer(joboffers)
        return Response(serializer.data)
    
    def put(self,request,pk):
        joboffers = self.get_object(pk)
        serializer = JobOfferSerializer(joboffers,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk):
        joboffers = self.get_object(pk)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)