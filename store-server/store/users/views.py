
from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth, messages
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from users.models import User
from users.forms import UserLoginForm, UserRegistrationForms, UserProfileForm
from products.models import Basket
from common.views import TitleMixin

#
# class UserLoginView(TitleMixin, LoginRequiredMixin, LoginView):
#     template_name = 'users/login.html'
#     form_class = UserLoginForm
#
#     success_url = reverse_lazy('users:login')
#     title = 'Volsi - Авторизация'




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

class UserRegistrationView(TitleMixin, SuccessMessageMixin, CreateView):
    model = User
    form_class = UserRegistrationForms
    template_name = 'users/registration.html'
    success_url = reverse_lazy('users:login')
    success_message = 'Вы успешно зарегистрировались!'
    title = 'Volsi - Регистрация'


class UserProfileView(TitleMixin, UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = 'users/profile.html'
    title = 'Volsi - Личный кабинет'

    def get_success_url(self):
        return reverse_lazy('users:profile', args=(self.object.id,))

    def get_context_data(self, **kwargs):
        context = super(UserProfileView, self).get_context_data()
        context['productBaskets'] = Basket.objects.filter(user=self.object)
        return context

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))


# @csrf_exempt
# def registration(request):
#     if request.method == 'POST':
#         form = UserRegistrationForms(data=request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Вы успешно зарегистрировались!')
#             return HttpResponseRedirect(reverse('users:login'))
#     else:
#         form = UserRegistrationForms()
#     context = {'form': form}
#
#     return render(request, 'users/registration.html', context)





# @login_required
# @csrf_exempt
# def profile(request):
#     if request.method == 'POST':
#         form = UserProfileForm(instance=request.user,  data=request.POST, files=request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('users:profile'))
#         else:
#             print(form.errors)
#     else:
#         form = UserProfileForm(instance=request.user)
#
#     context = {
#         'title': 'Store - Профиль',
#         'form': form,
#         'productBaskets': Basket.objects.filter(user=request.user),
#
#     }
#     return render(request, 'users/profile.html', context)

