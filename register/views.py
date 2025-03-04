from django.shortcuts import render,redirect
from .models import signup
from django.contrib.auth import logout


# Create your views here.
def login(request):
    if request.method=='POST':
        key=request.POST['key']
        pwd=request.POST['pwd']
        try:
            ob=signup.objects.get(email=key,password=pwd)
            request.session['name']=ob.name
            return redirect('home')
        except Exception as e:
            return render(request,'Login_index.html',{'msg':'Invalid email or password'})
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


def logout_view(request):
    print("Session data before logout:", request.session.items())  # Print session data before flushing
    request.session.flush()  # Clear session
    print("Session data after logout:", request.session.items())  # Print session data after flushing
    return redirect('home')
