from django.test import TestCase
from ..models import UserAccount
from .. import constants


class UserAccountModelTest(TestCase):

    def setUp(self):
        self.user_data = {
            "username": "testuser",
            "email": "test@example.com",
            "password": "password123",
            "first_name": "Test",
            "last_name": "User",
            "phone_number": "1234567890",
        }

    def test_create_user_success(self):
        user = UserAccount.objects.create_user(**self.user_data)
        self.assertEqual(user.username, self.user_data["username"])
        self.assertEqual(user.email, self.user_data["email"])
        self.assertFalse(user.is_staff)
        self.assertTrue(user.is_active)
        self.assertNotEqual(user.password, self.user_data["password"])
        self.assertTrue(user.check_password(self.user_data["password"]))

    def test_email_normalization(self):
        mixed_case_email = "TestEmail@Example.COM"
        user = UserAccount.objects.create_user(
            username="normemailuser",
            email=mixed_case_email,
            password="testpass123",
            first_name="Norm",
            last_name="Email",
            phone_number="2223334444"
        )

        local_part, domain_part = mixed_case_email.split('@')
        expected_email = local_part + '@' + domain_part.lower()
        self.assertEqual(user.email, expected_email)

    def test_create_user_without_email_raises_error(self):
        with self.assertRaisesMessage(ValueError, constants.ERROR_MESSAGES["USER_EMAIL_REQUIRED"]):
            UserAccount.objects.create_user(
                username="testuser2",
                email=None,
                password="password2"
            )

    def test_create_superuser_sets_flags(self):
        superuser = UserAccount.objects.create_superuser(
            username="admin",
            email="admin@example.com",
            password="adminpassword"
        )
        self.assertTrue(superuser.is_staff)
        self.assertTrue(superuser.is_active)
        self.assertTrue(superuser.is_superuser)
        self.assertTrue(superuser.check_password("adminpassword"))

    def test_str_method_returns_username(self):
        user = UserAccount.objects.create_user(
            username="stringmethodtest",
            email="str@example.com",
            password="stringpass123",
            first_name="Str",
            last_name="Test",
            phone_number="9999999999",
        )
        self.assertEqual(str(user), "stringmethodtest")
