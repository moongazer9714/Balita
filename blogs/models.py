from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=222, blank=True)

    # slug = models.SlugField(max_length=222, unique=True)

    def __str__(self):
        return self.title


class CategoryByZone(models.Model):
    title = models.CharField(max_length=222, blank=True)

    # slug = models.SlugField(max_length=222, unique=True)

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(max_length=222, blank=True)

    # slug = models.SlugField(max_length=222, unique=True)

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=222, blank=True)
    slug = models.SlugField(max_length=222, unique=True)
    body = RichTextUploadingField()
    image = models.ImageField(upload_to='media/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(default=0)
    tag = models.ManyToManyField(Tag, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    categorybyzone = models.ForeignKey(CategoryByZone, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comment')
    name = models.CharField(max_length=222, blank=True)
    email = models.EmailField()
    website = models.CharField(max_length=222, blank=True)
    message = models.CharField(max_length=222, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=50, blank=True)
    image = models.ImageField(upload_to='media/', blank=True)
    description = RichTextUploadingField()

    def __str__(self):
        return self.name
