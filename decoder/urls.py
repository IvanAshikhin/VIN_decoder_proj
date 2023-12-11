from django.urls import path

from decoder import views

urlpatterns = [
    path("search-statistics/", views.car_dashboard_view, name="car_search_statistics"),
    path("new_decode/<int:user_id>/", views.decode_vin_view, name="new_decode_vin"),
]
