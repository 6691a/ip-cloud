from django import forms


class WhiteListCreateForm(forms.ModelForm):
    class Meta:
        model = "WhiteList"
        fields = ("name", "ip", "mac", "description", "is_active")
