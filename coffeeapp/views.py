from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView


# Create your views here.

def index(request):
    return render(request, 'coffeeapp/home.html')


@login_required(login_url='/signup')
def products(request):
    return render(request, 'coffeeapp/products.html')


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
