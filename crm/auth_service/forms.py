from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django import forms


from auth_service.models import User


class UserLoginForm(AuthenticationForm):
    FIELD_STYLE_CLASS = "w-full px-5 py-1 text-gray-700 bg-gray-200 rounded" 

    class Meta:
        model = User
        fields = ['username', 'password']

    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': self.FIELD_STYLE_CLASS,
            'placeholder': 'Имя пользователя',
        })
        self.fields['password'].widget.attrs.update({
            'class': self.FIELD_STYLE_CLASS,
            'placeholder': 'Паролль',
        })



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
