from django.urls import path, include
from api.decoder.views import DecodeVinAPIView
from api.users.views import LoginUserView

urlpatterns = [
    path('login/', LoginUserView.as_view(), name='login'),
    path('decode-vin/', DecodeVinAPIView.as_view(), name='decode_vin_api'),
]
