from django import forms

from login.models import Login

class LoginForm(forms.ModelForm):
    class Meta:
        model = Login
        fields = ["first_name", "surname", "email", "new_password", "date_of_birth", "gender"]

