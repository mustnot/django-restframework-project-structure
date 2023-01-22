import pytest
from django.contrib.auth import get_user_model

User = get_user_model()


@pytest.mark.django_db
class TestUserModel:
    def test_create_user_with_email_successful(self):
        assert User.objects.count() == 0

        email = "user@test.com"
        password = "testpassword1234"

        User.objects.create_user(email=email, password=password)

        assert User.objects.count() == 1
