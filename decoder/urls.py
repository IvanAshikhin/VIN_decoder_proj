from django.urls import path

from decoder import views
from decoder.views import (
    paypal_donate_payment_view,
    payment_failed_view,
    payment_success_view,
)

urlpatterns = [
    path("search-statistics/", views.car_dashboard_view, name="car_search_statistics"),
    path("new_decode/<int:user_id>/", views.decode_vin_view, name="new_decode_vin"),
    path("payment/", paypal_donate_payment_view, name="payment_view"),
    path("payment-decline/", payment_failed_view, name="payment_cancel"),
    path("payment-success/", payment_success_view, name="payment_success"),
]
