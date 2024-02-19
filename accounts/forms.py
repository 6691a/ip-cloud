from allauth.account.forms import SignupForm as AllauthSignupForm
from django import forms
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget

from .models import Gender


class SignupForm(AllauthSignupForm):
    name = forms.CharField(max_length=30, label="Name")
    gender = forms.ChoiceField(choices=Gender.choices, label="Gender")
    phone = PhoneNumberField(label="Phone", widget=PhoneNumberPrefixWidget())


class ReVerificationForm(forms.Form):
    email = forms.EmailField(label="Email")
