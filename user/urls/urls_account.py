from django.shortcuts import render
from django.urls import path
from user.views import views_account


urlpatterns = [
    path("account_profile", views_account.ProfileView.as_view(), name="account_profile"),
    path("account_orders", views_account.OrderHistoryView.as_view(), name="account_orders"),
]
