from django.urls import path
from .views import RegisterView, CustomLoginView, check_user_status

app_name = "accounts"

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", CustomLoginView, name="login"),
    path("status/", check_user_status, name="status"),
]
