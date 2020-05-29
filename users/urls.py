"""Defines URL pattern for users"""
from django.conf.urls import url
from django.urls import path, include
from django.contrib.auth.models import User
from django.contrib.auth.views import (
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
)

from . import views


app_name = 'users'

urlpatterns = [
    # Include default auth urls.
    path('', include('django.contrib.auth.urls')),

    # Registration
    path(r'/register/', views.register, name='register'),
    path(r'/profile/', views.view_profile, name='view_profile'),
    path(r'/profile/edit', views.edit_profile, name='edit_profile'),
    path(r'/change_password', views.change_password, name='change_password'),
    # django package to do reset password and reverse reset password
    path(r'/password_reset', PasswordResetView.as_view(), name='password_reset'),
    path(r'/password_reset/done', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path(r'/password_reset/confirm', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path(r'/password_reset/complete', PasswordResetCompleteView.as_view(), name='password_reset_complete'),

]
