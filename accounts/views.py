from django.http import JsonResponse
from django.views import View
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json


@method_decorator(csrf_exempt, name="dispatch")
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


@method_decorator(csrf_exempt, name="dispatch")
class LoginView(View):
    def post(self, request):
        print(request)
        data = json.loads(request.body)
        username = data.get("username")
        password = data.get("password")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            print("User logged in successfully")
            return JsonResponse({"message": "Login successful"})
        else:
            print("Invalid credentials trying to log in")
            return JsonResponse({"error": "Invalid credentials"}, status=400)
