from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

User = get_user_model()


# The example why we are using built in django classes
# class SignUpForm(forms.ModelForm):
#     re_password = forms.CharField()

#     class Meta:
#         model = User
#         # fields = ["username", "password1", "password2"]
#         fields = ["username", "password", "re_password"]

#     def clean(self):
#         if self.data['password'] != self.data['re_password']:
#             raise ValueError("Passwords are not match")

#         import ipdb; ipdb.set_trace(context=10)


#     def save():
#         ...


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            "username",
        ]
