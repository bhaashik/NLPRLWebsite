from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm,SetPasswordForm,PasswordResetForm
from django.contrib.auth import get_user_model
from django_recaptcha.fields import ReCaptchaField
from django.contrib.auth import authenticate

# from captcha.fields import ReCaptchaField
# from captcha.widgets import ReCaptchaV2Checkbox

from pathlib import Path


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(help_text='A valid email address, please.', required=True)
    terms = forms.BooleanField(required=True, label='I accept the Terms of Service and Privacy Notice')

    class Meta:
        model = get_user_model()
        fields = ['status','first_name', 'last_name', 'email', 'password1', 'password2', 'terms']

    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
    

#
# class UserLoginForm(AuthenticationForm):
#     def __init__(self, *args, **kwargs):
#         super(UserLoginForm, self).__init__(*args, **kwargs)
#         self.username_field=get_user_model()._meta.get_field(get_user_model().USERNAME_FIELD)
#         self.fields['username'].widget = forms.TextInput(attrs={'class':'form-control','placeholder':'Email'})
#         self.fields['username'].label='Email'
#         self.fields['password'].widget = forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'})
    # email = forms.EmailField(widget=forms.TextInput(
    #     attrs={'class': 'form-control', 'placeholder': 'Email'}),
    #     label="Email")
    #
    # password = forms.CharField(widget=forms.PasswordInput(
    #     attrs={'class': 'form-control', 'placeholder': 'Password'}))
    #
    #

#
# from django import forms
# from django.contrib.auth.forms import AuthenticationForm
# from django.contrib.auth import get_user_model
#
# class UserLoginForm(AuthenticationForm):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.username_field = get_user_model()._meta.get_field(get_user_model().USERNAME_FIELD)
#         self.fields['username'].widget = forms.TextInput(
#             attrs={'class': 'form-control', 'placeholder': 'Email'}
#         )
#         self.fields['username'].label = 'Email'
#         self.fields['password'].widget = forms.PasswordInput(
#             attrs={'class': 'form-control', 'placeholder': 'Password'}
#         )
#         # We are NOT explicitly defining the 'email' field here anymore
#
#     def clean(self):
#         username = self.cleaned_data.get('username')
#         password = self.cleaned_data.get('password')
#
#         if username is not None and password:
#             self.user_cache = authenticate(self.request, username=username, password=password)
#             if self.user_cache is None:
#                 raise self.error_messages['invalid_login'](
#                     code='invalid_login',
#                     params={'username': self.username_field.verbose_name},
#                 )
#             else:
#                 self.confirm_login_allowed(self.user_cache)
#
#         return self.cleaned_data


class UserLoginForm(AuthenticationForm):
    username = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'})
    )

    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})
    )


