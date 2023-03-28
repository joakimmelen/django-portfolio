from django.http import JsonResponse
from django.views import View
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.contrib.auth.views import LoginView
import json


class RegisterView(View):
    def post(self, request):
        print(request)
        data = json.loads(request.body)
        username = data.get("username")
        password = data.get("password")
        email = data.get("email")

        if User.objects.filter(username=username).exists():
            print("Username already exists")
            return JsonResponse({"error": "Username already exists"}, status=400)

        user = User.objects.create_user(
            username=username, password=password, email=email
        )
        print("User created successfully")
        return JsonResponse(
            {
                "message": "User created successfully",
                "user": {"username": user.username, "email": user.email},
            },
            status=201,
        )
        
@csrf_exempt
class CustomLoginView(LoginView):
    def post(self, request, *args):
        data = json.loads(request.body)
        request.POST = request.POST.copy()
        request.POST['username'] = data.get("username")
        request.POST['password'] = data.get("password")
        return super().post(request, *args)


def check_user_status(request):
    print(request.user.is_authenticated)
    if request.user.is_authenticated:
        return JsonResponse({"is_authenticated": True, "is_superuser": request.user.is_superuser})
    else:
        return JsonResponse({"is_authenticated": False})
