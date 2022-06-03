from django.urls import path
from calculator import views

urlpatterns=[
    path("home",views.HomeView.as_view()),
    path("add",views.AddView.as_view()),
    path("sub",views.SubView.as_view()),
    path("mul",views.MulView.as_view()),
    path("div",views.DivView.as_view()),
    path("mod",views.ModView.as_view()),
    path("exp",views.ExpView.as_view()),
    path("fact",views.FactView.as_view())
]