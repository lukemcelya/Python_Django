from django import forms
from registration.models import Registration

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = "__all__"
        
class LoginForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ('username', 'password')