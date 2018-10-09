from django.db import models

# Create your models here.


class Post(models.Model):
    title=models.CharField(max_length=64)
    content=models.TextField()
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    class Meta:
        ordering=['-created']

