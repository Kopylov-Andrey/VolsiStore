from django.shortcuts import render

from users.models import User
from users.forms import UserLoginForm

def login(request):
    return render(request, 'users/login.html')


def registration(request):
    return render(request, 'users/registration.html')