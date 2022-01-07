from django.urls import path
from rest_framework_simplejwt import views as jwt_views
# from dj_rest_auth.registration.views import VerifyEmailView

from .views import (
    UserRegistrationView,
    UserLoginView,
    verification_otpAPIView,
    ChangePasswordView,
    # emailget
    forgotPasswordView,
    forgotverification_otp,
    taskapi,
    updatetaskapi,
    deletetaskapi

)

urlpatterns = [
    path('token/obtain/', jwt_views.TokenObtainPairView.as_view(), name='token_create'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('api/register', UserRegistrationView.as_view(), name='register'),
    path('api/login/', UserLoginView.as_view(), name='login'),
    path('api/otp', verification_otpAPIView.as_view(), name='OTPverified'),
    path('api/changePassword/', ChangePasswordView.as_view(), name='getEmail'),
    path('api/forgotpassword', forgotPasswordView.as_view(), name='forgetotp'),
    path('api/Otp_forgot/', forgotverification_otp.as_view(), name='auth_change_password'),
    path('api/taskapi/', taskapi.as_view(), name='taskapi'),
    path('api/Updatetaskapi/<int:id>/', updatetaskapi.as_view(), name='updatetaskapi'),
    path('api/deletetaskapi/<int:id>/', deletetaskapi.as_view(), name='deletetaskapi'),

]
