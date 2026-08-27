# users/urls.py

from django.urls import path

from .views import EmailVerificationView
from .views import PasswordResetConfirmView
from .views import PasswordResetRequestView
from .views import UserRegistrationView

app_name = "users"

urlpatterns = [
    path("register/", UserRegistrationView.as_view(), name="register"),
    path("verify/<str:token>/", EmailVerificationView.as_view(), name="verify"),
    # Сброс пароля.
    path("password-reset/", PasswordResetRequestView.as_view(), name="password-reset-request"),
    path(
        "password-reset-confirm/<str:uid>/<str:token>/",
        PasswordResetConfirmView.as_view(),
        name="password-reset-confirm",
    ),
]
