from django.contrib.auth import login
from django.http import HttpRequest, HttpResponse
from rest_framework.decorators import api_view
from rest_framework_simplejwt.tokens import RefreshToken
from django.shortcuts import render, redirect
from django.core.cache import cache
from api.users.serializers import LoginSerializer


def login_form_view(request: HttpRequest) -> HttpResponse:
    return render(request, "index.html")


@api_view(["GET", "POST"])
def login_user(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data
            if request.user.is_authenticated:
                cache.delete(user.email + "_failed_login_attempts")
            login(request, user)
            refresh = RefreshToken.for_user(user)
            request.session["refresh_token"] = str(refresh)
            access_token = str(refresh.access_token)
            request.session["access_token"] = access_token
            return redirect("new_decode_vin", user_id=user.id)
    return render(request, "index.html")
