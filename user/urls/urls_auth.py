from django.shortcuts import render
from django.urls import path
from user.views import views_auth

urlpatterns = [
    path("auth_registration", views_auth.RegistrationView.as_view(), name="auth_registration"),
    path("auth_login", views_auth.LoginView.as_view(), name="auth_login"),
    path("auth_logout", views_auth.LogoutView.as_view(), name="auth_logout"),
    path("auth_email_verify", views_auth.EmailVerifyView.as_view(), name="auth_email_verify"),
    path("auth_email_resend_verification", views_auth.ResendVerificationView.as_view(), name="auth_email_resend_verification"),
    path("auth_password_reset", views_auth.PasswordResetView.as_view(), name="auth_password_reset"),
    path("auth_password_reset_confirm", views_auth.PasswordResetConfirmView.as_view(), name="auth_password_reset_confirm"),
    path("auth_password_change", views_auth.PasswordChangeView.as_view(), name="auth_password_change"),
]