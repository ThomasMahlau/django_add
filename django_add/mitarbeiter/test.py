import os
from django import setup

from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import resolve, reverse
from decimal import Decimal
import datetime

from .models import *
from .views import *

class MitarbeiterModelTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username="testuser",
            password="testpassword123",
        )
        self.mitarbeiter = Mitarbeiter.objects.create(
            benutzer=self.user,
            geburtsdatum="2000-01-01",
            einstellungsdatum="2022-01-01",
            telefonnummer="1234567890",
        )
        
    def test_user_content(self):
        self.assertEqual(f"{self.mitarbeiter.benutzer.username}", "testuser")
        
    def test_mitarbeiter_content(self):
        self.assertEqual(f"{self.mitarbeiter.benutzer}", "testuser")
        self.assertEqual(f"{self.mitarbeiter.geburtsdatum}", "2000-01-01")
        self.assertEqual(f"{self.mitarbeiter.einstellungsdatum}", "2022-01-01")
        self.assertEqual(f"{self.mitarbeiter.telefonnummer}", "1234567890")
        
    def test_mitarbeiter_view(self):
        self.client.login(username="testuser", password="testpassword123")
        response = self.client.get(reverse("mitarbeiter_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "testuser")
        self.assertTemplateUsed(response, "mitarbeiter_list.html")
