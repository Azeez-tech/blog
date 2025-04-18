from django.db import models
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField(max_length=3_000_000_000)
    created_at = models.DateTimeField(auto_now_add=True)