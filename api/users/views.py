from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from api.users.serializers import LoginSerializer, RegistrationSerializer
from users.models import User
import logging

logger = logging.getLogger('main')


class UserAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        logging.error('Error here')
        return User.objects.all()

    def get(self, request, *args, **kwargs):
        users = self.get_queryset()
        serializer = RegistrationSerializer(users, many=True)
        return Response(serializer.data)


class LoginUserView(APIView):
    permission_classes = [AllowAny]
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data

        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)
        refresh_token = str(refresh)

        response_data = {
            'access_token': access_token,
            'refresh_token': refresh_token,
        }

        return Response(data=response_data, status=status.HTTP_200_OK)


class RegisterUserView(APIView):
    permission_classes = [AllowAny]
    serializer_class = RegistrationSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(status=status.HTTP_201_CREATED)
