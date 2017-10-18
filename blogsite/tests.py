# -*- coding: utf-8 -*-
from django.test import TestCase, RequestFactory
from django.core.urlresolvers import reverse
from django.contrib.staticfiles.testing import LiveServerTestCase
from selenium import webdriver


class TestHomePage(TestCase):

    def setUp(self):
        self.response = self.client.get(reverse('index'))

    def test_uses_index_template(self):
        self.assertTemplateUsed(self.response, "blogsite/index.html")

    def test_uses_base_template(self):
        self.assertTemplateUsed(self.response, "base.html")


class TestNewVisitorHomePage(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def get_full_url(self, namespace):
        return self.live_server_url + reverse(namespace)

    def test_home_title(self):
        self.browser.get(self.get_full_url('index'))
        self.assertIn("idiot genius", self.browser.title)

    def test_brand_title(self):
        self.browser.get(self.get_full_url('index'))
        brand_title = self.browser.find_element_by_class_name('brand-title')
        self.assertIn("yujinyuz", brand_title.text)

class TestAboutPage(TestCase):

    def setUp(self):
        self.response = self.client.get(reverse('about'))

    def test_uses_about_template(self):
        self.assertTemplateUsed(self.response, "blogsite/about.html")

    def test_uses_base_template(self):
        self.assertTemplateUsed(self.response, "base.html")

    def test_about_contains_github_repositories(self):
        self.assertIn("GitHub Repositories", self.response.content.decode('utf-8'))

class TestNewVisitorAboutPage(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def get_full_url(self, namespace):
        return self.live_server_url + reverse(namespace)

    def test_about_title(self):
        self.browser.get(self.get_full_url('about'))
        self.assertIn("About", self.browser.title)

class TestBlogPage(TestCase):

    def setUp(self):
        self.response = self.client.get(reverse('blog:index'))

    def test_uses_blog_template(self):
        self.assertTemplateUsed(self.response, "blog/blog_index.html")
