from django.test import TestCase
from ..models import UserAccount
from ..serializers import RegisterSerializer

class RegisterSerializerTest(TestCase):
    def test_valid_serializer(self):
        user_data = {
            "username": "username1",
            "password": "password@1234",
            "first_name": "firstname",
            "last_name": "lastname",
            "email": "test@test.com",
            "phone_number": "111111111",
        }

        serializer = RegisterSerializer(data=user_data)
        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.validated_data['email'], "test@test.com")
        