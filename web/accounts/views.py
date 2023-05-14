from django.urls import reverse_lazy
from django.views.generic import *
from .form import CreateUserForm


class RegisterView(CreateView):
    template_name = 'registration/signup.html'
    form_class = CreateUserForm
    success_url = reverse_lazy('login')

