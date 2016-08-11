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
    email = forms.CharField()
    captcha = NoReCaptchaField()
    password = forms.CharField(widget=forms.PasswordInput)
    username = forms.CharField()

    class Meta:
        model = User
        fields = ['username', 'password','email']


class RoastForm(forms.ModelForm):
    # message = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = Roast
        fields = ('text',)

    def __init__(self, *args, **kwargs):
        super(RoastForm, self).__init__(*args, **kwargs)
        self.fields['text'].error_messages = {'required': 'text field is requried'}


class ContactForm(forms.Form):

    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea)

    # # the new bit we're adding
    # def __init__(self, *args, **kwargs):
    #     super(ContactForm, self).__init__(*args, **kwargs)
    #     self.fields['from_email'].label = "Your name:"
    #     self.fields['subject'].label = "Your email:"
    #     self.fields['message'].label = "What do you want to say?"



