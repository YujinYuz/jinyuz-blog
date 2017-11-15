# -*- coding: utf-8 -*-

from django.views import generic
from blog.models import Post
from jyz.utils import github

class IndexView(generic.ListView):
    template_name = 'blogsite/index.html'
    context_object_name = 'latest_blog_posts'

    def get_queryset(self):
        return Post.objects.get_recent_posts()

    def get_context_data(self, *args, **kwargs):
        context = super(IndexView, self).get_context_data(*args, **kwargs)
        context['post'] = Post.objects.get_my_intro()
        return context


class AboutView(generic.TemplateView):
    template_name = 'blogsite/about.html'

    def get_context_data(self, *args, **kwargs):
        context = super(AboutView, self).get_context_data(*args, **kwargs)
        context['repos'] = github.load_user_repositories(username='yujinyuz', forked=False)
        context['post'] = Post.objects.get_pinned_posts()

        return context

class ContactView(generic.TemplateView):
    template_name = 'blogsite/contact.html'
