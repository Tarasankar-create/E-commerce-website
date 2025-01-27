from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'Home_index.html')

def login(request):
    return render(request,'Login_index.html')

def register(request):
    return render(request,'Register_index.html')

def menFashion(request):
    return render(request,'Men_index.html') 

def womenFashion(request):
    return render(request,'Women_index.html') 

def kidFashion(request):
    return render(request,'Kid_index.html') 

def beauty(request):
    return render(request,'Beauty_index.html') 

def decor(request):
    return render(request,'Decor_index.html') 

def electronics(request):
    return render(request,'Electronics_index.html') 

def mobile(request):
    return render(request,'Mobile_index.html') 