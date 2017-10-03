from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User


SOCIAL_IMAGE = (
    ('git', 'GitHub'),
    ('linkedin', 'LinkedIn'),
)


class Post(models.Model):
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    body = models.TextField()
    tags = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

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


class Social(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    social_account_link = models.URLField()
    social_icon = models.CharField(max_length=20, choices=SOCIAL_IMAGE)
