from django.test import TestCase, Client
from django.urls import reverse, resolve
from django.contrib.auth.models import User

# Create your tests here.

class LoginTesting(TestCase):

    def setUp(self):
        self.client = Client()
        self.login_url = reverse('account.login')