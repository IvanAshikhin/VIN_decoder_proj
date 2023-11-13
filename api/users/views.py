from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.permissions import AllowAny

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from api.users.serializers import LoginSerializer


class LoginUserView(APIView):
    permission_classes = [AllowAny]
    serializer_class = LoginSerializer

    @swagger_auto_schema(
        request_body=LoginSerializer,
        responses={
            200: openapi.Response("Successful login. Returns Bearer token and Refresh token."),
            400: "Bad Request - Invalid input or missing credentials",
        },
        operation_summary="User Login",
        operation_description="Authenticate user and return access and refresh tokens.",
    )
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data

        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)
        refresh_token = str(refresh)

        response = Response(status=status.HTTP_200_OK)
        response['Authorization'] = f'Bearer {access_token}'
        response['X-Refresh-Token'] = refresh_token

        return response
