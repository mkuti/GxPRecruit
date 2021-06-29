from django.db import models


# Create your models here.
class Job(models.Model):
    title = models.CharField(max_length=254, default='')
    description = models.TextField()
    contract = models.CharField(max_length=40, default='')
    location = models.CharField(max_length=40, default='')
    schedule = models.CharField(max_length=40, default='')
    url = models.CharField(max_length=40, default='')

    def __str__(self):
        return self.title
