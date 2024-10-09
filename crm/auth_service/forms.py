from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm


from auth_service.models import User


class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'last_name',
            'first_name',
            'second_name',
            'email',
            'phone_number',
            'fiz_tin',
            'profile_image',
            'password1', 
            'password2',
        ]
