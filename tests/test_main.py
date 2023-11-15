import pytest
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIRequestFactory
from api.users.serializers import RegistrationSerializer
from api.users.views import LoginUserView

User = get_user_model()


@pytest.mark.django_db
def test_register_user_view(client):
    url = reverse('register')

    data = {
        "email": "test@mail.com",
        "password": "TestPassword123",
    }

    serializer = RegistrationSerializer(data=data)
    assert serializer.is_valid()
    response = client.post(url, serializer.validated_data, format='json', secure=True)
    assert response.status_code == status.HTTP_201_CREATED
    assert User.objects.filter(email='test@mail.com').exists()


@pytest.mark.django_db
def test_login_user_view():
    factory = APIRequestFactory()
    view = LoginUserView.as_view()

    user = User.objects.create_user(email='test@mail.com', password='TestPass123')
    data_correct = {
        'email': 'test@mail.com',
        'password': 'TestPass123',
    }
    request_correct = factory.post('/login/', data=data_correct)
    response_correct = view(request_correct)
    assert response_correct.status_code == status.HTTP_200_OK
    assert 'access_token' in response_correct.data
    assert 'refresh_token' in response_correct.data

    data_incorrect = {
        'email': 'incorrect@mail.com',
        'password': 'IncorrectPass123',
    }
    request_incorrect = factory.post('/login/', data=data_incorrect)
    response_incorrect = view(request_incorrect)
    assert response_incorrect.status_code == status.HTTP_400_BAD_REQUEST
