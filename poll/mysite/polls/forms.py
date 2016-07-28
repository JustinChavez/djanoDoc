from django import forms
from django.contrib.auth.models import User
from nocaptcha_recaptcha.fields import NoReCaptchaField
from .models import Choice

class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = '__all__'

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    captcha = NoReCaptchaField

    class Meta:
        model = User
        fields = ['username', 'password']
