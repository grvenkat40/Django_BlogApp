from django.db import models
from django.utils.text import slugify 



class Category(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name



class post(models.Model):
    post_id = models.IntegerField(max_length=100)
    title = models.CharField(max_length=100)
    Author = models.CharField(max_length=50)
    content = models.TextField()
    img_url = models.URLField(null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    slug=models.SlugField(unique=True,null=True,blank=True)
    category=models.ForeignKey(Category, on_delete=models.CASCADE)

    def save(self,*args,**kwargs):
        self.slug=slugify(self.title)
        super().save(*args,**kwargs)

    def __str__(self):
        return f'{self.title},{self.Author}'
    

class Feedback(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    feedback=models.TextField(max_length=1000)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
