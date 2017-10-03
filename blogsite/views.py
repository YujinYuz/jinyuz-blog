# -*- coding: utf-8 -*-

from django.views import generic
from blog.models import Post


class IndexView(generic.ListView):
    template_name = 'blogsite/index.html'
    context_object_name = 'latest_blog_posts'

    def get_queryset(self):
        return Post.objects.order_by('-created_at')[:5]


class AboutView(generic.TemplateView):
    template_name = 'blogsite/about.html'
