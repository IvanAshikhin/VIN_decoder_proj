from django.urls import path
from .views import new_decode_vin

urlpatterns = [
    path('new_decode/<int:user_id>/', new_decode_vin, name='new_decode_vin'),
]
