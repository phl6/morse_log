"""Defines URL pattern for users"""
from django.conf.urls import url
from django.urls import path, include
from django.contrib.auth.models import User
from django.contrib.auth.views import (
    PasswordResetView, # suggestion: PasswordResetView
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
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
    path(r'/reset_password', PasswordResetView.as_view(), name='reset_password'),
    path(r'/reset_password/done', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path(r'/reset_password/confirm', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path(r'/reset_password/complete', PasswordResetCompleteView.as_view(), name='password_reset_complete'),

]
