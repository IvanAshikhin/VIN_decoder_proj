from django.urls import path
from api.decoder.views import DecodeVinAPIView
from api.users.views import LoginUserView, RegisterUserView

urlpatterns = [
    path('login/', LoginUserView.as_view(), name='login'),
    path('register/', RegisterUserView.as_view(), name='register'),
    path('decode-vin/', DecodeVinAPIView.as_view(), name='decode_vin_api'),
]
