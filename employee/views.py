from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
# Create your views here.

# def index(request):
#     return HttpResponse("<h1>Hello World</h1>")
#
# def login(request):
#      return render(request,"login.html")
#
# def registration(request):
#     return HttpResponse("<h1>Registration</h1>")
#
# def signup(request):
#     return HttpResponse("<h1>SIGNUP</h2>")
#
# def home(request):
#     return render(request,"home.html")

class IndexView(View):
    def get(self,request):
        return render(request,"login.html")
    def post(self,request):
        print(request.POST.get("u_name"))
        print(request.POST.get("pwd"))
        return render(request,"login.html")


class HomeView(View):
    def get(self,request):
        return render(request,"home.html")

class RegistrationView(View):
    def get(self,request):
        return render(request,"register.html")
    def post(self,request):
        print(request.POST.get("f_name"))
        print(request.POST.get("l_name"))
        print(request.POST.get("u_name"))
        print(request.POST.get("pwd1"))
        print(request.POST.get("pw2"))
        print(request.POST.get("e_mail"))
        return render(request,"register.html")
