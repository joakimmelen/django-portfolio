from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = "accounts"

urlpatterns = [
    path("register/", views.RegisterView.as_view(), name="register"),
    path('login/', views.api_login, name='login'),
    path('logout/', views.api_logout, name='logout'),
    path("status/", views.check_user_status, name="status"),
]
