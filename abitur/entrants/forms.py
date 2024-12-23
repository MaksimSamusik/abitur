from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.forms import widgets
from .models import Application


class RegisterUserForm(UserCreationForm):
    reg_validator = RegexValidator(
        regex=r'^[a-zA-Z]+$',
        message='Логин может содержать только английские буквы.',
        code='invalid_login'
    )

    username = forms.CharField(
        validators=[reg_validator],
        help_text='Логин может содержать только английские буквы.',
        widget=forms.TextInput(),
        label='Логин'
    )
    email = forms.EmailField(label='Email', widget=forms.TextInput())
    password1 = forms.CharField(label='Пароль', widget=forms.TextInput(attrs={'type': 'password'}))
    password2 = forms.CharField(label='Повторите пароль', widget=forms.TextInput(attrs={'type': 'password'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    login_validator = RegexValidator(
        regex=r'^[a-zA-Z]+$',
        message='Логин может содержать только английские буквы.',
        code='invalid_login'
    )

    username = forms.CharField(
        validators=[login_validator],
        help_text='Логин может содержать только английские буквы.',
        widget=forms.TextInput(),
        label='Логин'
    )
    password = forms.CharField(label='Пароль', widget=forms.TextInput(attrs={'type': 'password'}))


class ApplicationForm(forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['dorm'].empty_label = "Не выбрано"
        self.fields['type_of_place'].empty_label = "Не выбрано"
        self.fields['foreign_language'].empty_label = "Не выбрано"
        self.fields['overall_rating'].label = "Ваш общий балл"
        self.fields['user'].initial = user
        self.fields['user'].widget.attrs['disabled'] = 'disabled'
        self.fields['user'].label = 'Имя пользователя'
        self.fields['user'].widget.attrs['readonly'] = 'readonly'
        self.fields['email'].initial = user.email
        self.fields['email'].widget.attrs['disabled'] = 'disabled'
        self.fields['email'].widget.attrs['disabled'] = 'readonly'

    class Meta:
        model = Application
        fields = '__all__'
        widgets = {
            'overall_rating': widgets.NumberInput(attrs={'readonly': 'readonly'}),
        }
