from django.shortcuts import render,redirect
from .models import signup
from django.contrib.auth import logout


# Create your views here.

def login(request):
    if request.method=='POST':
        key=request.POST['key']
        pwd=request.POST['pwd']
        try:
            if '@' in key:
                ob=signup.objects.get(email=key,password=pwd)
            else:
                ob=signup.objects.get(mob=key,password=pwd)
            request.session['name']=ob.name
            request.session['pin']=ob.pin
            request.session['email']=ob.email
            return redirect('home')
        except Exception as e:
            return render(request,'Login_index.html',{'msg':'Invalid email or password'})
    return render(request,'Login_index.html')

def register(request):
    if request.method=='POST':
        name=request.POST['name']
        coun=request.POST['country']
        mobile=request.POST['mob']
        pin=request.POST['pin']
        email=request.POST['email']
        pwd=request.POST['password']
        try:
            ob=signup.objects.create(name=name,country=coun,mob=mobile,pin=pin,email=email,password=pwd)
            ob.save()
            return redirect('login')
        except Exception:
            return render(request,'Register_index.html',{'msg':'Error'})
    return render(request,'Register_index.html')

def update_view(request):
    email = request.session.get('email')
    ob=signup.objects.get(email=email)
    if request.method=='POST':
        name=request.POST['name']
        coun=request.POST['country']
        mobile=request.POST['mob']
        pin=request.POST['pin']
        email=request.POST['email']
        pwd=request.POST['password']

        ob.name=name
        ob.country=coun
        ob.mob=mobile
        ob.pin=pin
        ob.email=email
        ob.password=pwd
        ob.save()
        request.session['name']=ob.name
        request.session['pin']=ob.pin
        request.session['email']=ob.email
        # These upper lines change the data if the data is render to the home page after update.
        return redirect('home')

    return render(request,'update_index.html',{'ob':ob})


def logout_view(request):
    request.session.flush()  # Clear session
    return redirect('home')
