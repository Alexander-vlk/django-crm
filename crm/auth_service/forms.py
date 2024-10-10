from django import forms
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.contrib.auth.forms import AuthenticationForm


from auth_service.models import User


FIELD_STYLE_CLASS = "w-full px-5 py-1 text-gray-700 bg-gray-200 rounded" 


class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': FIELD_STYLE_CLASS,
            'placeholder': 'Имя пользователя',
        })
        self.fields['password'].widget.attrs.update({
            'class': FIELD_STYLE_CLASS,
            'placeholder': 'Пароль',
        })



class UserRegisterForm(forms.ModelForm):
    fio = forms.CharField(
        max_length=200,
        widget=forms.TextInput(
        attrs={
                'class': FIELD_STYLE_CLASS,
                'placeholder': 'ФИО',
                }
            ),
        label='ФИО',
        validators=[UnicodeUsernameValidator]
        )
    password_1 = forms.CharField(
        min_length=8,
        max_length=50,
        widget=forms.PasswordInput(
             attrs={
                    'class': FIELD_STYLE_CLASS,
                    'placeholder': 'Пароль',
                }
            ),
            label='Пароль',
        )
    password_2 = forms.CharField(
        min_length=8,
        max_length=50,
        widget=forms.PasswordInput(
             attrs={
                    'class': FIELD_STYLE_CLASS,
                    'placeholder': 'Пароль (еще раз)',
                }
            ),
        label='Пароль (еще раз)',
        )
    
    class Meta:
        model = User
        fields = [
            'fio',
            'username',
            'email',
            'phone_number',
            'fiz_tin',
            'password_1',
            'password_2',
            'is_shop_owner',
            'is_supplier',
        ]
        widgets = {
            'username': forms.TextInput(
                attrs={
                    'class': FIELD_STYLE_CLASS,
                    'placeholder': 'Имя пользователя'
                }
            ),
            'email': forms.TextInput(
                attrs={
                    'class': FIELD_STYLE_CLASS,
                    'placeholder': 'Электронная почта',
                }
            ),
            'phone_number': forms.TextInput(
                attrs={
                    'class': FIELD_STYLE_CLASS,
                    'placeholder': 'Номер телефона',
                }
            ),
            'fiz_tin': forms.TextInput(
                attrs={
                    'class': FIELD_STYLE_CLASS,
                    'placeholder': 'ИНН физ. лица',
                }
            ),
            'is_shop_employee': forms.CheckboxInput(
                attrs={
                    'class': '',
                    'name': 'is_shop_employee',
                }
            ),
            'is_supplier': forms.CheckboxInput(
                attrs={
                    'class': '',
                    'name': 'is_supplier',
                }
            ),
        }

    def clean(self):
        cleaned_data = super().clean()

        fio = cleaned_data.get('fio')
        COUNT_OF_WORDS_IN_FIO = 3

        password_1 = cleaned_data.get('password_1')
        password_2 = cleaned_data.get('password_2')

        if len(fio.split()) != COUNT_OF_WORDS_IN_FIO:
            raise forms.ValidationError('Неправильный формат ввода ФИО')

        if password_1 != password_2:
            raise forms.ValidationError('Пароли не совпадают')
        
        return cleaned_data

    def save(self, commit=True):
        obj = super().save(commit=False)

        obj.password = self.cleaned_data.get('password_1')

        splitted_fio = self.cleaned_data.get('fio').split()

        obj.last_name = splitted_fio[0]
        obj.first_name = splitted_fio[1]
        obj.second_name = splitted_fio[2]

        if commit:
            obj.save()

        return obj
    