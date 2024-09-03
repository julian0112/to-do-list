from django.db import models
from tags.models import tags

# Create your models here.
class Lists(models.Model):
    title = models.CharField(max_length=200)
    tags = models.ManyToManyField(tags)
    
    def __str__(self):
        return self.title
    