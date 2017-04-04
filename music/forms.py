from django.contrib.auth.models import User
from django import forms


# A blue print for a user form
class UserForm(forms.ModelForm):
    # Hide the password as it is typed
    password = forms.CharField(widget=forms.PasswordInput)

    # Information about the class it is in
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password'
        ]
