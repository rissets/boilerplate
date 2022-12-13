from django.contrib.auth.models import User
from django.test import TestCase


# Create your tests here.

class TestViews(TestCase):

    # @classmethod
    # def setUpTestData(cls):
    #     cls.user = User.objects.create_user(
    #         email='test@gmail.com',
    #         username='testuser',
    #         password='123dfsf45'
    #     )
    def test_login_page_works(self):
        response = self.client.get('/authentication/login')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/authentication/auth-login.html')
        self.assertContains(response, 'Login')

    def test_register_page_works(self):
        response = self.client.get('/authentication/register')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/authentication/auth-register.html')
        self.assertContains(response, 'Register')

    def test_user_signup(self):
        response = self.client.post('/authentication/register', {
            'email': 'test@gmail.com',
            'username': 'testuser',
            'password1': '309u32jsdfiodj',
            'password2': '309u32jsdfiodj'
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/authentication/register-email.txt')

    def test_user_login(self):
        response = self.client.post('/authentication/login', {
            'username': 'testuser',
            'password': '309u32jsdfiodj',
        })
        self.assertEqual(response.status_code, 200)


