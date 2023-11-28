from django.urls import path
from api.decoder.views import DecodeVinAPIView
from api.users.views import RegisterUserView, UserListAPIView, LoginUserView

urlpatterns = [
    path("users/", UserListAPIView.as_view(), name="user-list"),
    # path('login/', LoginUserView.as_view(), name='login'),
    path("register/", RegisterUserView.as_view(), name="register"),
    path("decode-vin/", DecodeVinAPIView.as_view(), name="decode_vin_api"),
]
