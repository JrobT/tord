from django.test import RequestFactory, TestCase
from blog.views import PostListView


class PostListViewTest(TestCase):
    def test_index_status(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
