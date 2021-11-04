from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import SignUpForm

User = get_user_model()


class SignUpView(CreateView):
    model = User
    form_class = SignUpForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
