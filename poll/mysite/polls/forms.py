from django import forms
from django.contrib.auth.models import User


from .models import Choice

class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = '__all__'

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password']
# class LoginForm(forms.ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput)
#
#     class Meta:
#         model =User
#         fields = ['username', 'password']
# # class UserForm(forms.ModelForm):
#     password = forms.Charfield(widget=forms.PasswordInput())
#
#     class Meta:
#         model = User
#         fields = ('username', 'email', 'password')
#
# class UserProfileForm(forms.ModelForm):
#     class Meta:
#         model = UserProfileForm
#         fields = ('website', 'picture')