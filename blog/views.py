from .models import Post, Category
from .decorators import public_post_only
from django.views import generic
from django.utils.decorators import method_decorator

class IndexView(generic.ListView):
    template_name = 'blog/blog_index.html'
    context_object_name = 'posts'
    paginate_by = 5
    queryset = Post.objects.all()

@method_decorator(public_post_only, name='dispatch')
class DetailView(generic.DetailView):
    template_name = 'blog/post_detail.html'
    model = Post


class CategoryView(generic.DetailView):
    template_name = 'blog/category_list.html'
    model = Category
