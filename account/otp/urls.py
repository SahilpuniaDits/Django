from django.urls import path

from .views import (
    SignUpView,
    EmailConformationView,
    UserLoginView
    # PasswordResetApiView,
    # LogOutView,
)


urlpatterns = [
    path(
        'signup/',
        SignUpView.as_view(),
        name='signup',
    ),
    path(
        'email-conformation/<str:activation_key>/',
        EmailConformationView.as_view(),
        name='email_conformation'
    ),
    path('login/', 
        UserLoginView.as_view(),
        name='login_view'
    ),
]