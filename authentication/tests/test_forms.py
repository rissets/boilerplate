from django.contrib.auth.models import User
from django.test import TestCase

from authentication.forms import UserLoginForm, UserRegistrationForm


class TestForms(TestCase):

    def test_user_registration_form_valid_data(self):
        form = UserRegistrationForm(data={
            'email': 'testuser@mail.com',
            'username': 'testuser',
            'password1': 'qwert12345@@',
            'password2': 'qwert12345@@',
        })

        self.assertTrue(form.is_valid())

    def test_user_registration_form_no_data(self):
        form = UserRegistrationForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 4)

    def test_user_login_form_valid_data(self):
        user = User.objects.create_user(
            username="testuser",
            password="qwert12345@@"
        )

        form = UserLoginForm(data={
            'username': 'testuser',
            'password': 'qwert12345@@',
        })

        self.assertTrue(form.is_valid())

    def test_user_login_form_no_data(self):
        form = UserLoginForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 2)


