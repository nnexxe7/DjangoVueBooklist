from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import json

@csrf_exempt
@require_POST
def login_view(request):
    data = json.loads(request.body)
    username = data.get('username')
    password = data.get('password')
    user = authenticate(request, username=username, password=password)

    if user:
        login(request, user)
        return JsonResponse({'message': 'Zalogowano pomyślnie'})
    else:
        return JsonResponse({'message': 'Błąd logowania'}, status=400)

@csrf_exempt
@require_POST
def register_view(request):
    data = json.loads(request.body)
    username = data.get('username')
    password = data.get('password')
    email = data.get('email')

    if not User.objects.filter(username=username).exists():
        User.objects.create_user(username=username, password=password, email=email)
        return JsonResponse({'message': 'Zarejestrowano pomyślnie'})
    else:
        return JsonResponse({'message': 'Nazwa użytkownika już istnieje'}, status=400)
