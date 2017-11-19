from django.conf.urls import url
from .views import IndexView, DetailView, CategoryView

app_name = 'blog'

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^(?P<slug>[\w-]+)/$', DetailView.as_view(), name='detail'),
    url(r'^category/(?P<slug>[a-zA-Z0-9-]+)/$',
        CategoryView.as_view(), name='category'),
]
