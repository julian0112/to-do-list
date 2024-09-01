from django.db import models

# Create your models here.
class tags(models.Model):
    title = models.CharField(max_length=200)
    desc = models.TextField(blank=True)

    def __str__(self):
        return self.title