from allauth.account.forms import SignupForm as AllauthSignupForm
from django import forms
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget

from .models import Accounts, Gender


class SignupForm(AllauthSignupForm):
    name = forms.CharField(max_length=30)
    gender = forms.ChoiceField(choices=Gender.choices)
    phone = PhoneNumberField(widget=PhoneNumberPrefixWidget())


class ReVerificationForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = Accounts
        fields = ["email"]


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Accounts
        fields = ["name", "gender", "phone"]
