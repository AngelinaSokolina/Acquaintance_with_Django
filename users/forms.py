from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ValidationError
from .models import User


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'class': 'form-control'}),
        label='Email',
        error_messages={
            'unique': 'Пользователь с таким Email уже существует.',
            'invalid': 'Введите корректный Email адрес.',
        }
    )

    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label='Пароль',
        error_messages={
            'required': 'Поле "Пароль" обязательно для заполнения.',
        }
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label='Повторите ввод пароля',
        error_messages={
            'required': 'Поле "Повторите ввод пароля" обязательно для заполнения.',
        }
    )

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})

        # Дополнительные сообщения для встроенных валидаций Django
        self.fields['password1'].help_text = None  # убираем подсказки
        self.fields['password2'].help_text = None

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise ValidationError('Пароли не совпадают.')
        return password2

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError('Пользователь с таким Email уже существует.')
        return email


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})

        self.fields['username'].label = 'Email'
        self.fields['password'].label = 'Пароль'

        # Русские сообщения об ошибках
        self.fields['username'].error_messages = {
            'required': 'Поле "Email" обязательно для заполнения.',
        }
        self.fields['password'].error_messages = {
            'required': 'Поле "Пароль" обязательно для заполнения.',
        }