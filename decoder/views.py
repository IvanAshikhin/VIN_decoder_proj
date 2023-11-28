from django.http import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render

from .forms import VinDecodeForm
from .functions import get_car


def decode_vin_view(request: HttpRequest, user_id: int) -> HttpResponse:
    form = VinDecodeForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        vin_code = form.cleaned_data["vin_code"]
        car = get_car(vin_code)
        return render(
            request,
            "success_template.html",
            {"vin_code": vin_code, "car": car, "user_id": user_id},
        )
    return render(
        request, "decode_vin_template.html", {"form": form, "user_id": user_id}
    )
