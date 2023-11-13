from django.urls import path
from .views import decode_vin

urlpatterns = [
    path('decode/', decode_vin, name='decode_vin'),
]
