from .models import Post, Category
from django.views import generic


class IndexView(generic.ListView):
    template_name = 'blog/blog_index.html'
    context_object_name = 'recent_posts'

    def get_queryset(self):
        return Post.objects.get_recent_posts()


class DetailView(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'


class CategoryView(generic.DetailView):
    template_name = 'blog/category_list.html'
    model = Category

    def get_context_data(self, **kwargs):
        context = super(CategoryView, self).get_context_data(**kwargs)
        context['category_posts'] = Post.objects.filter(category=context['category'])
        return context
