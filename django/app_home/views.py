# https://github.com/mkhorasani/Streamlit-Authenticator
from django.shortcuts import render
from django.contrib.auth import authenticate
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def streamlit_view(request):
    return render(request, "streamlit_template.html")


@csrf_exempt
def authenticate_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            print("Login Success")
            return JsonResponse({'status': 'success', 'username': user.username})
        else:
            print("Login Fail")
            return JsonResponse({'status': 'failure', 'message': 'Invalid credentials'})
    return JsonResponse({'status': 'failure', 'message': 'Only POST method is allowed'})



def get_users(request):
    users = User.objects.all()
    users_dict = {}
    for user in users:
        users_dict[user.username] = {'name': user.get_full_name(), 'password': user.password}
    return JsonResponse(users_dict)

