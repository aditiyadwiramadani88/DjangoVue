from rest_framework import serializers 
from .models import Article
from django.utils.text import slugify
import random

class ArticleSeriallizer(serializers.Serializer):
        id = serializers.IntegerField(read_only=True)
        title = serializers.CharField(required=True,  max_length=100)
        slug = serializers.CharField(read_only=True)
        content_text = serializers.CharField()
        def slugfi(self, data): 
            return slugify('{}-{}'.format(random.random(), data))
        def create(self, validate_data): 
            return Article.objects.create(**validate_data, slug=self.slugfi(validate_data['title']))
        def  update(self, instance, validated_data):
              instance.title = validated_data.get('title', instance.title)
              instance.content_text = validated_data.get('content_text', instance.content_text)
              instance.save()
              return  instance
