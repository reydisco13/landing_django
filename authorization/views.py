from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import *
from .models import *
# Create your views here.


class MyprojectLoginView(LoginView):
    template_name = 'authorization/login.html'
    form_class = AuthUserForm
    success_url = reverse_lazy('login_page')

    def get_success_url(self):
        return self.success_url


class RegisterUserView(CreateView):
    model = User
    template_name = 'authorization/register_page.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('login_page')
    success_msg = 'Пользователь успешно создан'

    def form_valid(self, form):
        form_valid = super().form_valid(form)
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]
        aut_user = authenticate(username=username, password=password)
        login(self.request, aut_user)
        return form_valid


class MyProjectLogout(LogoutView):
    next_page = reverse_lazy('home')


def auth_users(request):
    logged_users = [user.user for user in LoggedUser.objects.all()]
    return render(request, 'authorization/test.html', {'logged_users': logged_users},)
