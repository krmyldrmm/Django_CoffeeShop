from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("products/", views.products, name='products'),
    path("signup/", views.SignUpView.as_view(), name='signup'),
]