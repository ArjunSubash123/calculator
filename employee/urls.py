from django.urls import path
from employee import views

urlpatterns = [
      # path("index",views.index),
      # path("login",views.login),
      # path("registration",views.registration),
      # path("signup",views.signup),
      # path("home",views.home)
      path("login",views.IndexView.as_view()),
      path("home",views.HomeView.as_view()),
      path("register",views.RegistrationView.as_view())
]
