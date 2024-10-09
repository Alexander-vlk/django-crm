from django.shortcuts import redirect, render
from django.urls import reverse_lazy, reverse
from django.views.decorators.http import require_POST, require_http_methods
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView

from auth_service.forms import UserLoginForm, UserRegisterForm


class UserLoginView(LoginView):
    authentication_form = UserLoginForm

    template_name = 'auth/auth.html'

    next_page = reverse_lazy('app:index')


class UserRegisterView(CreateView):
    form_class = UserRegisterForm

    template_name = 'auth/auth.html'

    success_url = reverse_lazy('app:index')
    
    def form_valid(self, form):
        user = form.save()

        login(self.request, user)
        return super().form_valid(form)
    


@require_POST
def logout_user(request):
    LOGOUT_REDIRECT_URL = reverse('app:index')
    logout(request)
    return redirect(LOGOUT_REDIRECT_URL)
