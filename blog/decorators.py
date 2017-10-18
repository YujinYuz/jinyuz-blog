from django.core.exceptions import PermissionDenied
from blog.models import Post

def public_post_only(function):
    def wrap(request, *args, **kwargs):
        post = Post.objects.get(slug=kwargs['slug'])
        if post.status == 'public':
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied

    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap
