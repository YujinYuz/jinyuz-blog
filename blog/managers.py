from django.db import models


class PostManager(models.Manager):

    def get_queryset(self):
        return super(PostManager, self).get_queryset()

    def get_recent_posts(self):
        queryset = self.get_queryset().filter(
            kind='post').filter(status='public').order_by('-created_at')[:5]

        return queryset

    def get_pinned_posts(self):
        queryset = self.get_queryset().filter(kind='pinned_post'
                                              ).filter(status='public')

        return queryset

    def get_all_posts(self):
        queryset = self.get_queryset().filter(status='public')

        return queryset
