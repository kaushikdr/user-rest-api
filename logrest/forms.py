from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import ugettext_lazy as _
from django import forms

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1')

    def save(self, commit = True):
        user = super(SignUpForm, self).save(commit = False)
        user._meta.get_field('email')._unique = True
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if email and User.objects.filter(email=email).exclude(username=username).count():
            raise forms.ValidationError(u'Email addresses must be unique.Already exists!')
        return email

class LoginForm(forms.Form):
    username = forms.CharField(required = True)
    password = forms.CharField(widget=forms.PasswordInput(),required = True)
