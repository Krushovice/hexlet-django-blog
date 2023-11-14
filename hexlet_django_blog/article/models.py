from django.db import models


# Create your models here.
class Article(models.Model):
    name = models.CharField(max_length=200)  # название статьи
    body = models.TextField()  # тело статьи
    timestamp = models.DateTimeField(auto_now_add=True)


class ArticleComment(models.Model):
    content = models.CharField('content', max_length=100)
