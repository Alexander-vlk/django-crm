from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views.decorators.http import require_POST
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView

from auth_service.forms import UserLoginForm


class UserLoginView(LoginView):
    authentication_form = UserLoginForm

    template_name = 'auth/auth.html'

    next_page = reverse_lazy('app:index')


# @require_http_methods(['GET', 'POST'])
# def register(request):
#     template_name = 'auth/auth.html'


@require_POST
def logout_user(request):
    LOGOUT_REDIRECT_URL = reverse('app:index')
    logout(request)
    return redirect(LOGOUT_REDIRECT_URL)
