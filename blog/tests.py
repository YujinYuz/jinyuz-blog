from django.test import TestCase
from .models import Post, Category, Author
from django.contrib.auth.models import User
from django.shortcuts import reverse


class BlogTestCase(TestCase):

    def setUp(self):
        self.category = Category.objects.create(title="Test Category", slug="test-category")
        self.user = User.objects.create_superuser(username='test_user', email='test_user@testmail.com', password='fake_password')
        self.author = Author.objects.create(user=self.user, image='test_image.jpeg')

        Post.objects.create(
            category=self.category,
            author=self.author,
            kind='post',
            title="Test Post 1",
            slug="test-post-1",
            body="<p>This is a test post.</p>",
            tags="test, post, tags",
            status="public")

        Post.objects.create(
            category=self.category,
            author=self.author,
            kind='post',
            title="Test Post 2",
            slug="test-post-2",
            body="<p>This is a test post.</p>",
            tags="test, post, tags",
            status="public")

        Post.objects.create(
            category=self.category,
            author=self.author,
            kind='post',
            title="Test Post 3",
            slug="test-post-3",
            body="<p>This is a test post.</p>",
            tags="test, post, tags",
            status="private")

        Post.objects.create(
            category=self.category,
            author=self.author,
            kind='pinned_post',
            title="Test Pinned Post 1",
            slug="test-pinned-post-1",
            body="<p>This is a test pinned post.</p>",
            tags="test, post, tags",
            status="public")

        Post.objects.create(
            category=self.category,
            author=self.author,
            kind='pinned_post',
            title="Test Pinned Post 2",
            slug="test-pinned-post-2",
            body="<p>This is a test pinned post.</p>",
            tags="test, post, tags",
            status="public")

    def test_user_name(self):
        self.assertIn(self.user.username, "test_user")

    def test_blog_posts(self):
        post1 = Post.objects.get(pk=1)
        post2 = Post.objects.get(pk=2)
        post3 = Post.objects.get(pk=3)

        self.assertEqual(post1.title, "Test Post 1")
        self.assertEqual(post2.title, "Test Post 2")
        self.assertEqual(post3.title, "Test Post 3")

        self.assertEqual(post1.slug, "test-post-1")
        self.assertEqual(post2.slug, "test-post-2")
        self.assertEqual(post3.slug, "test-post-3")

    def test_blog_recent_posts(self):
        recent_posts = Post.objects.get_recent_posts()
        self.assertEqual(len(recent_posts), 2)

    def test_blog_pinned_posts(self):
        pinned_post = Post.objects.get_pinned_posts()
        self.assertEqual(len(pinned_post), 2)

    def test_blog_public_posts(self):
        public_posts = Post.objects.get_all_posts()
        self.assertEqual(len(public_posts), 4)

    def test_blog_private_posts(self):
        post = Post.objects.get(pk=3)
        response = self.client.get(reverse('blog:detail', args=[post.slug,]))
        self.assertEqual(response.status_code, 403)
