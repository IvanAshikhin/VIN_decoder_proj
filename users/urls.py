from django.urls import path

from users import views


urlpatterns = [
    path('login/', views.login_user, name='login'),
    path('index/<int:user_id>/', views.tokens, name='tokens')
]
