from django.shortcuts import render
from django.views.generic import CreateView
from django.views.generic.edit import FormView
from .forms import Userregisterform, Loginform
from .models import Usuario
from django.urls import reverse_lazy,reverse
from django.contrib.auth import authenticate, login
#  Create your views here.

class Userregisterview(FormView):
    template_name = 'usuarios/register.html'
    form_class = Userregisterform

    success_url = '/'

    def form_valid(self, form):
        Usuario.objects.create_user(
            form.cleaned_data['username'],
            form.cleaned_data['email'],
            form.cleaned_data['password1'],
            nombres=form.cleaned_data['nombres'],
            apellidos=form.cleaned_data['apellidos'],
            genero=form.cleaned_data['genero']

        )
        return super(Userregisterview,self).form_valid(form)

class Loginuser(FormView):
    template_name = 'usuarios/login.html'
    form_class = Loginform
    success_url = reverse_lazy('home_app:panel')
    def form_valid(self, form):
        user=authenticate(username=form.cleaned_data['username'],
                          password=form.cleaned_data['password'])

        login(self.request,user)




        return super(Loginuser, self).form_valid(form)
