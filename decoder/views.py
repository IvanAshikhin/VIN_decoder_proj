from django.http import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render
from django.urls import reverse
from paypal.standard.forms import PayPalPaymentsForm

from vin import settings
from .exception import VinException
from .forms import VinDecodeForm
from .functions import get_car
from .models import RequestLog
from .utils import (
    vin_search_count_with_date,
    user_vin_search_count_with_date,
    vin_search_count,
)


def decode_vin_view(request: HttpRequest, user_id: int) -> HttpResponse:
    form = VinDecodeForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        vin_code = form.cleaned_data["vin_code"]
        if len(vin_code) != 17:
            raise VinException("VIN code must have exactly 17 characters.")
        car = get_car(vin_code)
        request_log = RequestLog(vin=vin_code, car=car, user=request.user)
        request_log.save()
        return render(
            request,
            "success_template.html",
            {"vin_code": vin_code, "car": car, "user_id": user_id},
        )
    return render(
        request, "decode_vin_template.html", {"form": form, "user_id": user_id}
    )


def car_dashboard_view(request: HttpRequest) -> HttpResponse:
    cars = vin_search_count()
    users = user_vin_search_count_with_date()
    vin_search_stats = vin_search_count_with_date()
    context = {
        "cars": cars,
        "users": users,
        "vin_search_stats": vin_search_stats,
    }
    return render(request, "dashboard.html", context)


def paypal_donate_payment_view(request: HttpRequest) -> HttpResponse:
    paypal_dict = {
        "business": settings.PAYPAL_RECEIVER_EMAIL,
        "amount": "1.00",
        "item_name": "Донат",
        "currency_code": "USD",
        "notify_url": request.build_absolute_uri(reverse("paypal-ipn")),
        "return_url": request.build_absolute_uri(reverse("payment_success")),
        "cancel_return": request.build_absolute_uri(reverse("payment_cancel")),
    }
    form = PayPalPaymentsForm(initial=paypal_dict)
    return render(request, "payment.html", {"form": form})


def payment_success_view(request: HttpRequest) -> HttpResponse:
    return render(request, "payment-success.html")


def payment_failed_view(request: HttpRequest) -> HttpResponse:
    return render(request, "payment-failed.html")
