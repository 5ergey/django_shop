from django.shortcuts import render
from django.urls import path
from user.views import views_account


urlpatterns = [
    path("profile/", views_account.ProfileView.as_view(), name="account_profile"),
    path("orders/", views_account.OrderHistoryView.as_view(), name="account_orders"),
]
