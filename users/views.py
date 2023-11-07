from django.contrib.auth import login
from rest_framework.decorators import api_view
from rest_framework_simplejwt.tokens import RefreshToken
from django.shortcuts import render, redirect
from django.core.cache import cache
from api.users.serializers import LoginSerializer


def login_form_view(request):
    return render(request, 'login.html')


@api_view(['GET', 'POST'])
def login_user(request):
    if request.method == 'POST':
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data
            if request.user.is_authenticated:
                cache.delete(user.email + '_failed_login_attempts')
            login(request, user)
            refresh = RefreshToken.for_user(user)
            request.session['access_token'] = str(refresh.access_token)
            request.session['refresh_token'] = str(refresh)
            return redirect('tokens', user_id=user.id)

    return render(request, 'login.html')


@api_view(['GET'])
def tokens(request, user_id):
    access_token = request.session.get('access_token')
    refresh_token = request.session.get('refresh_token')

    context = {
        'access_token': access_token,
        'refresh_token': refresh_token
    }
    return render(request, 'main.html', context)
