from django import forms
from nocaptcha_recaptcha.fields import NoReCaptchaField

from django.contrib.auth.models import User
from .models import Choice

class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = '__all__'

class UserForm(forms.ModelForm):
    captcha = NoReCaptchaField()
    password = forms.CharField(widget=forms.PasswordInput)
    username = forms.CharField()


    class Meta:
        model = User
        fields = ['username', 'password']





