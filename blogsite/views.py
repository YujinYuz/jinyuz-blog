# -*- coding: utf-8 -*-

from django.views import generic
from blog.models import Post


class IndexView(generic.ListView):
    template_name = 'blogsite/index.html'
    context_object_name = 'latest_blog_posts'

    def get_queryset(self):
        return Post.objects.get_recent_posts()

    def get_context_data(self, *args, **kwargs):
        context = super(IndexView, self).get_context_data(*args, **kwargs)
        context['pinned_posts'] = Post.objects.get_pinned_posts()
        return context


class AboutView(generic.TemplateView):
    template_name = 'blogsite/about.html'
