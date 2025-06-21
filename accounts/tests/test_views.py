from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.core.management import call_command
from io import StringIO
from .. import constants


class RegisterViewTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        out = StringIO()
        call_command("loaddata", "test_users.json", stdout=out)

    def setUp(self):
        self.url = reverse("user-register")
        self.valid_user = {
            "username": "uniqueuser",
            "email": "uniqueuser@example.com",
            "password": "Password123!",
            "first_name": "Unique",
            "last_name": "User",
            "phone_number": "9999999999",
        }

    def test_register_success(self):
        response = self.client.post(self.url, self.valid_user, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["status"], constants.Status.SUCCESS)
        self.assertEqual(response.data["data"]["username"], "uniqueuser")

    def test_register_password_not_returned(self):
        response = self.client.post(self.url, self.valid_user, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertNotIn("password", response.data["data"])


    def test_register_missing_required_field(self):
        data = self.valid_user.copy()
        data.pop("email")
        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data["status"], constants.Status.FAILURE)

    def test_register_invalid_email_format(self):
        data = self.valid_user.copy()
        data["email"] = "invalid-email"
        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data["status"], constants.Status.FAILURE)
        self.assertIn("email", response.data["data"])

    def test_register_duplicate_username(self):
        data = self.valid_user.copy()
        data["username"] = "testuser1"
        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data["status"], constants.Status.FAILURE.value)
        self.assertIn("username", response.data["data"])
