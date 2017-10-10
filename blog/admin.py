from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from blog.models import Post, Category, Author

admin.site.unregister(User)


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


class AuthorInline(admin.StackedInline):
    model = Author


class AuthorAdmin(UserAdmin):
    inlines = [AuthorInline]


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(User, AuthorAdmin)
