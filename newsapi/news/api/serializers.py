from rest_framework import serializers
from news.models import Article , Journal
from datetime import datetime , timezone
from django.utils.timesince import timesince




class ArticleSerializer(serializers.ModelSerializer):

    time_since_publication = serializers.SerializerMethodField()
    # author = serializers.StringRelatedField()
    # author = JournalSerializer(read_only=True)

    class Meta:
        model = Article
        exclude = ("id",)
        # fields = "__all__" #we want all the field
        # fields = ("title","description") #include field
    def get_time_since_publication(self,object):
        publication_date = object.publication_data
        now = datetime.now(timezone.utc)
        time_delta = timesince(publication_date , now)
        return time_delta
    
    #     ### validate ก่อน function ชื่ออะไรก็ได้
    def validate(self, data):
        """ ไม่ให้ title กับ des เหมือนกัน """
        """ check description and title are different """
        if data["title"] == data["description"]:
            raise serializers.ValidationError("Title and Description must be difference")
            return data        
        

    def validate_title(self,value):
        if len(value)<30:
            raise serializers.ValidationError("The title has to be at least 30 Chars")
            return value

class JournalSerializer(serializers.ModelSerializer):
    articles = ArticleSerializer(read_only=True,many=True)

    class Meta:
        model = Journal
        fields = "__all__"

# class ArticleSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     author = serializers.CharField()
#     title = serializers.CharField()
#     body = serializers.CharField()
#     location = serializers.CharField()
#     publication_data = serializers.DateTimeField()
#     active = serializers.BooleanField()
#     created_at = serializers.DateTimeField(read_only=True)
#     updated_at = serializers.DateTimeField(read_only=True)

#     def create(self, validated_data):
#         print(validated_data)
#         return Article.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         instance.author = validated_data.get('author',instance.author)
#         instance.title = validated_data.get('title',instance.title)
#         instance.description = validated_data.get('description',instance.description)
#         instance.body = validated_data.get('body',instance.body)
#         instance.location = validated_data.get('location',instance.location)
#         instance.publication_data = validated_data.get('publication_data',instance.publication_data)
#         instance.active = validated_data.get('active',instance.active)

#         instance.save()
#         return instance
    

#     ### validate ก่อน function ชื่ออะไรก็ได้
#     def validate(self, data):
#         """ ไม่ให้ title กับ des เหมือนกัน """
#         """ check description and title are different """
#         if data["title"] == data["description"]:
#             raise serializers.ValidationError("Title and Description must be difference")
#             return data        
        

#     def validate_title(self,value):
#         if len(value)<60:
#             raise serializers.ValidationError("The title has to be at least 60 Chars")
#             return value

# serializer.data
# JSONRENDERER >> to send json
# JSONparser >> to retrive json

