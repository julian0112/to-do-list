from django.db import models
from lists.models import Lists

# Create your models here.
class Tasks(models.Model):
    desc = models.TextField(blank=False)
    list = models.ForeignKey(Lists, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.desc
    
