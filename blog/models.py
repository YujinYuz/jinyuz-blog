from django.db import models
from ckeditor.fields import RichTextField
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from .managers import PostManager


class Post(models.Model):
    POST_KIND = (
        ('post', 'Post'),
        ('intro', 'Introduction'),
        ('pinned_post', 'Pinned Post'),
        ('draft', 'Draft'),
    )

    POST_STATUS = (
        ('public', 'Public'),
        ('private', 'Private'),
    )

    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    kind = models.CharField(max_length=100, choices=POST_KIND, default='draft')
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    body = RichTextField()
    tags = models.CharField(max_length=255, blank=True)
    status = models.CharField(
        max_length=100, choices=POST_STATUS, default='public')
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = PostManager()

    def __str__(self):
        return "{title}".format(title=self.title)

    def url(self):
        return reverse('blog:detail', args=[self.slug])


class Category(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return "{title}".format(title=self.title)

    def url(self):
        return reverse('blog:category', args=[self.slug])


class Author(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return "{fullname}".format(fullname=self.user.get_full_name())
