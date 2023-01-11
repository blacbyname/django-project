from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=44)
    summary = models.TextField(blank=False,null=False)
    article = models.TextField(blank=False,null=False)
    