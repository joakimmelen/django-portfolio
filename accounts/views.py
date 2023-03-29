from django.http import JsonResponse
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
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
        
        
def api_login(request):
    print(request)
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return JsonResponse({'detail': 'Login successful'}, status=200)
        else:
            return JsonResponse({'detail': 'Invalid credentials'}, status=400)
    else:
        return JsonResponse({'detail': 'Invalid request method'}, status=405)
    

def api_logout(request):
    if request.user.is_authenticated:
        logout(request)
        return JsonResponse({'detail': 'Logout successful'}, status=status.HTTP_200_OK)
    else:
        return JsonResponse({'detail': 'User not logged in'}, status=status.HTTP_400_BAD_REQUEST)
    
    
def check_user_status(request):
    print(request.user.is_authenticated)
    if request.user.is_authenticated:
        return JsonResponse({"is_authenticated": True, "is_superuser": request.user.is_superuser})
    else:
        return JsonResponse({"is_authenticated": False})
