from django import forms
from nocaptcha_recaptcha.fields import NoReCaptchaField

from django.contrib.auth.models import User
from .models import Choice, Roast

class ChoiceForm(forms.ModelForm):
    message = forms.CharField(widget=forms.Textarea)
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


class RoastForm(forms.ModelForm):
    # message = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = Roast
        fields = ('text',)




