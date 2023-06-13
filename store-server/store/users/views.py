from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth, messages
from django.urls import reverse



from users.models import User
from users.forms import UserLoginForm, UserRegistrationForms, UserProfileForm
from products.models import Basket

@csrf_exempt
def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username=request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))
    else:
        form = UserLoginForm()

    context = {'form': form}
    return render(request, 'users/login.html', context)

@csrf_exempt
def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForms(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно зарегистрировались!')
            return HttpResponseRedirect(reverse('users:login'))
    else:
        form = UserRegistrationForms()
    context = {'form': form}

    return render(request, 'users/registration.html', context)

@login_required
@csrf_exempt
def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(instance=request.user,  data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:profile'))
        else:
            print(form.errors)
    else:
        form = UserProfileForm(instance=request.user)




    context = {
        'title': 'Store - Профиль',
        'form': form,
        'productBaskets': Basket.objects.filter(user=request.user),

    }
    return render(request, 'users/profile.html', context)

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))







