from django.urls import path
from django.contrib.auth import views as auth_views

from django.contrib.auth import views as auth_views

from . import views
from .views import PasswordsChangeView

urlpatterns = [
    path('register/', views.register_user, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    # Change Password
    path("forgot-password/", views.forgot_password, name="forgot_password"),
    path("my-account/", views.account_info, name="account_info"),
    path("password/", PasswordsChangeView.as_view(template_name="change_password.html"), name="password_change"),
    path("password_success/", views.password_success, name="password_success"),
    # Forget Password
    path("reset_password/", auth_views.PasswordResetView.as_view(template_name="password_reset.html"), name="reset_password"),
    path("reset_password_sent/", auth_views.PasswordResetDoneView.as_view(template_name="password_reset_sent.html"), name="password_reset_done"),
    path("reset_password/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_form.html"), name="password_reset_confirm"),
    path("reset_password-complete/", auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_done.html"), name="password_reset_complete"),
    path("my-account/", views.account_info, name="account_info")
]