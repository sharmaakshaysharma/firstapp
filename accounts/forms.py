from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm


class RegisterForm(UserCreationForm):
    email = forms.EmailField(
        max_length=100,
        required=True,
        help_text='Enter Email Address',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
    )
    first_name = forms.CharField(
        max_length=100,
        required=True,
        help_text='Enter First Name',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
    )
    last_name = forms.CharField(
        max_length=100,
        help_text='Enter Last Name',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
    )
    username = forms.CharField(
        max_length=200,
        required=True,
        help_text='Enter Username',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
    )
    password1 = forms.CharField(
        help_text='Enter Password',
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
    )
    password2 = forms.CharField(
        required=True,
        help_text='Enter Password Again',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password Again'}),
    )
    check = forms.BooleanField(required=True)

    class Meta:
        model = User
        fields = [
            'username', 'email', 'first_name', 'last_name', 'password1', 'password2', 'check',
        ]

    def save(self, commit=True):
        user = super().save(commit=False)  
        user.email = self.cleaned_data.get('email')
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')

        if commit:
            user.save()  # Save the User instance
        return user
    


class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=150,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'})
    )
    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})
    )