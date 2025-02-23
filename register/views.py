from django.shortcuts import render,redirect
from .models import signup,login
# Create your views here.
def login(request):
    return render(request,'Login_index.html')

def register(request):
    if request.method=='POST':
        name=request.POST['name']
        coun=request.POST['country']
        mobile=request.POST['mob']
        email=request.POST['email']
        pwd=request.POST['password']
        try:
            ob=signup.objects.create(name=name,country=coun,mob=mobile,email=email,password=pwd)
            ob.save()
            return redirect('login')
        except Exception:
            return render(request,'Register_index.html',{'msg':'Error'})
    return render(request,'Register_index.html')
