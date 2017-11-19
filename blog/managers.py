from django.db import models


class PostManager(models.Manager):

    def get_queryset(self):
        return super(PostManager, self).get_queryset()

    def get_my_intro(self):
        queryset = self.get_queryset().get(kind='intro', status='public')
        return queryset

    def get_pinned_post(self):
        queryset = self.get_queryset().get(kind='pinned_post', status='public')
        return queryset

    def get_all_posts(self):
        queryset = self.get_queryset().filter(status='public')
        return queryset
