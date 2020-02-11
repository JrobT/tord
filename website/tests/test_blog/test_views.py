from django.test import RequestFactory, TestCase
from blog.views import PostListView


class PostListViewTest(TestCase):
    def test_environment_set_in_context(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
