from django.db import models
from django.core.urlresolvers import reverse


class Blog(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{title}".format(title=self.title)

    def url(self):
        return reverse('view_blog_post', args=[self.slug])


class Category(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return "{title}".format(title=self.title)

    def url(self):
        return reverse('view_blog_category', args=[self.slug])
