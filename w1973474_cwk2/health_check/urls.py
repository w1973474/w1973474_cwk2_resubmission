from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import *
from django.views.generic import RedirectView
from django.urls import reverse_lazy

urlpatterns = [
    path('login/', views.Login, name="login"),
    path('signup/', views.Signup, name="signup"),
    path('dashboard/', views.Dashboard, name="dashboard"),
    path('health-check/', views.HealthCheckVoting, name='health_check_voting'),
    path('users/', views.AdminUserManagement, name='user_management'),
    path('users/delete/<int:user_id>/', views.DeleteUser, name='delete_user'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('accounts/login/', RedirectView.as_view(url=reverse_lazy('login'))),
    path('reset-password/', auth_views.PasswordResetView.as_view(), name="password_reset"),
    path('reset-password/done/', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
]
