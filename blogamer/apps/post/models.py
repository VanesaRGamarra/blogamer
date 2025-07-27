from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=45)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=45, null=False)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    author = models.CharField(max_length=45, null=False)
    date = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    imagen = models.ImageField(null=True, blank=True, upload_to='post',default='post/post_default.png')

    def __str__(self):
        return self.title