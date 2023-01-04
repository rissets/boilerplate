from django.contrib import auth
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from django.test import Client


# Create your tests here.

class TestViews(TestCase):

    def test_login_page_works(self):
        response = self.client.get(reverse('auth-login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/authentication/auth-login.html')
        self.assertContains(response, 'Login')

    def test_register_page_works(self):
        response = self.client.get(reverse('auth-register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/authentication/auth-register.html')
        self.assertContains(response, 'Register')

    def test_user_register_page_submission_works(self):
        post_data = {
            'email': 'user@email.com',
            'username': 'user',
            'password1': 'qwert12345@@',
            'password2': 'qwert12345@@'
        }

        response = self.client.post(reverse('auth-register'), post_data)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(User.objects.filter(username='user').exists())
        self.assertEqual(response.content, b'{"success_message": "Successfully registered please login"}')

    def test_user_login_page_submission_works(self):
        user = User.objects.create_user(
            username="testuser",
            password="qert12345@@"
        )

        post_data = {
            'username': 'testuser',
            'password': 'qert12345@@'
        }

        response = self.client.post(reverse('auth-login'), post_data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b'{"success_message": "Successfully login"}')
        self.assertTrue('username' in self.client.session)
        self.assertTrue(auth.get_user(self.client).is_authenticated)

    def test_recovered_password_page_works(self):
        response = self.client.get(reverse('auth-recoverpw'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/authentication/auth-recoverpw.html')
        self.assertContains(response, 'Recover Password')

    def test_recovered_password_submission_works(self):
        user = User.objects.create_user(
            username="testuser",
            email="testuser@email.com",
            password="qert12345@@"
        )

        post_data = {
            'email': 'testuser@email.com',
        }

        response = self.client.post(reverse('auth-recoverpw'), post_data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('password_reset_done'))

    def test_confirm_mail_page_works(self):
        response = self.client.get(reverse('auth-confirm-mail'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/authentication/auth-confirm-mail.html')
        self.assertContains(response, 'Confirm Mail')

    def test_logout_page_works(self):
        response = self.client.get(reverse('auth-logout'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/authentication/auth-logout-done.html')

