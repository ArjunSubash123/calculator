from django.shortcuts import render
from django.views.generic import View
# Create your views here.

class HomeView(View):
    def get(self,request):
        return render(request,'calc-home.html')

class AddView(View):
    def get(self,request):
        return render(request,'add.html')
    def post(self,request):
        n1=request.POST.get("num1")
        n2=request.POST.get("num2")
        result=int(n1)+int(n2)
        print(result)
        return render(request,"add.html",{"res":result})

class SubView(View):
   def get(self,request):
        return render(request,"sub.html")
   def post(self,request):
       n1=request.POST.get("num1")
       n2=request.POST.get("num2")
       result=int(n1)-int(n2)
       return render(request,"sub.html",{"subres":result})

class MulView(View):
   def get(self,request):
        return render(request,"mul.html")
   def post(self,request):
       n1=request.POST.get("num1")
       n2=request.POST.get("num2")
       result=int(n1)*int(n2)
       return render(request,"mul.html",{"mulres":result})

class DivView(View):
   def get(self,request):
        return render(request,"div.html")
   def post(self,request):
       n1=request.POST.get("num1")
       n2=request.POST.get("num2")
       result=int(n1)/int(n2)
       return render(request,"div.html",{"divres":result})

class ModView(View):
   def get(self,request):
        return render(request,"mod.html")
   def post(self,request):
       n1=request.POST.get("num1")
       n2=request.POST.get("num2")
       result=int(n1)%int(n2)
       return render(request,"mod.html",{"modres":result})

class ExpView(View):
   def get(self,request):
        return render(request,"exp.html")
   def post(self,request):
       n1=request.POST.get("num1")
       result=int(n1)**2
       return render(request,"exp.html",{"expres":result})

class FactView(View):
   def get(self,request):
        return render(request,"fact.html")
   def post(self,request):
       n1=int(request.POST.get("num1"))
       result=1
       for i in range(1,n1+1):
         result= result * (i)
       return render(request,"fact.html",{"factres":result})