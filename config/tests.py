from django.test import TestCase


class TestViews(TestCase):
    def test_home_page_works(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/index.html')
        self.assertContains(response, 'Boilerplate Django')
