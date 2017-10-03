from django.contrib import admin
from blog.models import Post, Category, Author, Social


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


# class AuthorAdmin(admin.ModelAdmin):
#     pass


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Author)
admin.site.register(Social)
