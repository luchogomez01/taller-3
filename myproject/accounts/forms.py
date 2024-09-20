from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm

class EmailAuthenticationForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        if email and password:
            self.user_cache = authenticate(email=email, password=password)
            if self.user_cache is None:
                raise forms.ValidationError("Correo o contraseña incorrectos.")
        return self.cleaned_data

    def get_user(self):
        return self.user_cache