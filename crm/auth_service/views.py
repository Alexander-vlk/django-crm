from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic.edit import CreateView

from auth_service.forms import UserLoginForm, UserRegisterForm


class UserLoginView(UserPassesTestMixin, LoginView):
    authentication_form = UserLoginForm

    template_name = 'auth/login.html'

    next_page = reverse_lazy('app:index')

    def test_func(self):
        return not self.request.user.is_authenticated


class UserRegisterView(UserPassesTestMixin, CreateView):
    form_class = UserRegisterForm

    template_name = 'auth/register.html'

    success_url = reverse_lazy('app:index')
    
    def form_valid(self, form):
        user = form.save()

        login(self.request, user)
        return super().form_valid(form)  
    
    def test_func(self):
        return not self.request.user.is_authenticated


@login_required
@require_POST
def logout_user(request):
    LOGOUT_REDIRECT_URL = reverse('app:index')
    logout(request)
    return redirect(LOGOUT_REDIRECT_URL)
