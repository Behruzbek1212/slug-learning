from django.db import models

class Post(models.Model):
    nomi = models.CharField(max_length=225)
    slug = models.SlugField(null=False, unique=True)
    date = models.DateTimeField(auto_now_add=True)
    rasm = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        return self.nomi