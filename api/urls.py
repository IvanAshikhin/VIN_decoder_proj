from django.urls import path, include

from api.decoder.views import DecodeVinAPIView

urlpatterns = [
    path("decoder/", include('decoder.urls')),
    path("users/", include('users.urls')),
    path('decode-vin/', DecodeVinAPIView.as_view(), name='decode_vin_api'),
]
