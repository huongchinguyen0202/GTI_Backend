from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import refresh_jwt_token
from rest_framework_jwt.views import verify_jwt_token

urlpatterns = [
    path('auth/refresh/', refresh_jwt_token, name='auth_refresh'),
    path('auth/verify/', verify_jwt_token, name='auth_verify'),
    path('auth/auth/', obtain_jwt_token, name='auth_auth'),
]
