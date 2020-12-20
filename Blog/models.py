from django.db import models
import random
# Create your models here.



class Article (models.Model):
    title = models.CharField(max_length=20)
    slug = models.TextField()
    content_text=models.TextField()
    def __str__(self): 
         return "{},{},{}".format(self.title, self.slug, self.content_text)

      