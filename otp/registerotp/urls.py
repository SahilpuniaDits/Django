from django.urls import path
from rest_framework_simplejwt import views as jwt_views
# from dj_rest_auth.registration.views import VerifyEmailView

from .views import (
    UserRegistrationView,
    UserLoginView,
    verification_otpAPIView
    # PasswordResetApiView,
    # ChangePasswordView,
    # idView
)

urlpatterns = [
    path('token/obtain/', jwt_views.TokenObtainPairView.as_view(), name='token_create'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('api/register', UserRegistrationView.as_view(), name='register'),
    path('api/login', UserLoginView.as_view(), name='login'),
    path('api/otp', verification_otpAPIView.as_view(), name='OTPverified'),

    # path('change_password/',ChangePasswordView.as_view(), name='auth_change_password'),
    # path('change_password/',PasswordResetApiView.as_view(), name='auth_change_password'),
    # path('accessid/',idView.as_view(), name='idview'),
]
