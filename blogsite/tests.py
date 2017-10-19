# -*- coding: utf-8 -*-
from django.test import TestCase, RequestFactory
from django.core.urlresolvers import reverse


class TestHomePage(TestCase):

    def setUp(self):
        self.response = self.client.get(reverse('index'))

    def test_uses_index_template(self):
        self.assertTemplateUsed(self.response, "blogsite/index.html")

    def test_uses_base_template(self):
        self.assertTemplateUsed(self.response, "base.html")

    def test_home_title(self):
        self.assertIn("idiot genius", self.response.content.decode('utf-8'))

    def test_home_status_code(self):
        self.assertEqual(self.response.status_code, 200)


class TestAboutPage(TestCase):

    def setUp(self):
        self.response = self.client.get(reverse('about'))

    def test_uses_about_template(self):
        self.assertTemplateUsed(self.response, "blogsite/about.html")

    def test_uses_base_template(self):
        self.assertTemplateUsed(self.response, "base.html")

    def test_about_contains_github_repositories(self):
        self.assertIn("GitHub Repositories", self.response.content.decode('utf-8'))

    def test_about_status_code(self):
        self.assertEqual(self.response.status_code, 200)

class TestBlogPage(TestCase):

    def setUp(self):
        self.response = self.client.get(reverse('blog:index'))

    def test_uses_blog_template(self):
        self.assertTemplateUsed(self.response, "blog/blog_index.html")

    def test_blog_status_code(self):
        self.assertEqual(self.response.status_code, 200)
