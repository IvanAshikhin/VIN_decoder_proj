from django.urls import path

from decoder.views import decode_vin

urlpatterns = [
    path('decode-vin/', decode_vin, name='decode_vin'),
]
