import pytest
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIRequestFactory
from api.users.serializers import RegistrationSerializer
from api.users.views import LoginUserView
from decoder.functions import get_country, get_vin_symbol
from decoder.models import Country

User = get_user_model()


@pytest.mark.django_db
def test_register_user_view(client):
    url = reverse("register")
    data = {
        "email": "test@mail.com",
        "password": "TestPassword123",
    }

    serializer = RegistrationSerializer(data=data)
    assert serializer.is_valid()
    response = client.post(url, serializer.validated_data, format="json", secure=True)
    assert response.status_code == status.HTTP_201_CREATED
    assert User.objects.filter(email="test@mail.com").exists()


@pytest.mark.django_db
def test_login_user_view():
    factory = APIRequestFactory()
    view = LoginUserView.as_view()

    User.objects.create_user(email="test@mail.com", password="TestPass123")
    data_correct = {
        "email": "test@mail.com",
        "password": "TestPass123",
    }
    request_correct = factory.post("/login/", data=data_correct)
    response_correct = view(request_correct)
    assert response_correct.status_code == status.HTTP_200_OK
    assert "access_token" in response_correct.data
    assert "refresh_token" in response_correct.data

    data_incorrect = {
        "email": "incorrect@mail.com",
        "password": "IncorrectPass123",
    }
    request_incorrect = factory.post("/login/", data=data_incorrect)
    response_incorrect = view(request_incorrect)
    assert response_incorrect.status_code == status.HTTP_400_BAD_REQUEST


@pytest.mark.django_db
def test_get_country_existing_country(mocker):
    mocker.patch(get_vin_symbol, return_value="US")
    existing_country = Country.objects.create(code="US", name="United States")
    result = get_country("1FMYU60E41U0U5211")
    assert result == existing_country


@pytest.mark.django_db
def test_get_country_new_country(mocker):
    mocker.patch("your_other_module.get_vin_symbol", return_value="CA")
    result = get_country("your_valid_vin")
    new_country = Country.objects.get(code="CA")
    assert result == new_country
