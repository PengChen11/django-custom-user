from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import CustomUser
# Create your tests here.

class CustomUsersTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            email = 'tester@email.com',
            password = 'pass'
        )


    def test_string_representation(self):
        user = CustomUser(email='tester@email.com')
        self.assertEqual(str(user), user.email)


    def test_custom_user(self):
        self.assertEqual(f'{self.user.email}', 'tester@email.com')


    def test_Home_View(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')


    def test_Sign_Up_View(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'email')
        self.assertTemplateUsed(response,'signup.html')


    def test_login_view(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/login.html')

