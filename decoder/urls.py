from django.urls import path

from decoder import views

urlpatterns = [
    path('new_decode/<int:user_id>/', views.new_decode_vin, name='new_decode_vin'),
]
