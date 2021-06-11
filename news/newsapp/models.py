from django.db import models

# Create your models here.


class News(models.Model):
    headline = models.CharField(max_length=100, null=True, blank=True)
    url = models.CharField(max_length=1000, null=True, blank=True)
    article = models.TextField(null=True, blank=True)
    author = models.CharField(max_length=100, null=True, blank=True)
    source = models.CharField(max_length=100, null=True, blank=True)
    date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return str(self.headline)