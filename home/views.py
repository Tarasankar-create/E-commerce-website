from django.shortcuts import render,redirect
from .models import Catagories,homeSlider,homeContSlider1,homeContSlider2,menContent,menSlider,womenSlider,womenContent,kidSlider,kidContent,decorSlider,decorContent,beautySlider,beautyContent,electronicsSlider,electronicsContent,mobileSlider,mobileContent

# Create your views here.

def home(request):
    homeslider=homeSlider.objects.all()
    homeCont1=homeContSlider1.objects.all()
    homeCont2=homeContSlider2.objects.all()
    name=request.session.get('name')
    pin=request.session.get('pin')
    if request.method =='POST':
        sdata = request.POST.get('sdata', '').strip()
        try:
            if sdata!=None:
                mdata=menContent.objects.filter(men_title__icontains=sdata)
                wmdata=womenContent.objects.filter(w_title__icontains=sdata)
                kdata=kidContent.objects.filter(k_title__icontains=sdata)
                ddata=decorContent.objects.filter(d_title__icontains=sdata)
                bdata=beautyContent.objects.filter(b_title__icontains=sdata)
                edata=electronicsContent.objects.filter(e_title__icontains=sdata)
                mbdata=mobileContent.objects.filter(m_title__icontains=sdata)
    
                if mdata.exists():
                    return redirect('menFashion')
                elif wmdata.exists():
                    return redirect('womenFashion')
                elif kdata.exists():
                    return redirect('kidFashion')
                elif ddata.exists():
                    return redirect('decor')
                elif bdata.exists():
                    return redirect('beauty')
                elif edata.exists():
                    return redirect('electronics')
                elif mbdata.exists():
                    return redirect('mobile')
                else:
                   data={
                    'slider':homeslider,
                    'cont1':homeCont1,
                    'cont2':homeCont2,
                    'name':name,
                    'pin':pin,
                    'msg':'No data found'
                    }
                return render(request,'Home_index.html',data)
        except Exception:
            return render(request,'Home_index.html')
    data={
        'slider':homeslider,
        'cont1':homeCont1,
        'cont2':homeCont2,
        'name':name,
        'pin':pin
    }
    return render(request,'Home_index.html',data)

def menFashion(request):
    mendata=menContent.objects.all()
    menslider=menSlider.objects.all()
    data={
        'mendata':mendata,
        'menSlider':menslider
    }
    return render(request,'Men_index.html',data) 

def womenFashion(request):
    wslide=womenSlider.objects.all()
    wdata=womenContent.objects.all()
    data={
        'wslide':wslide,
        'wdata':wdata
    }
    return render(request,'Women_index.html',data) 

def kidFashion(request):
    kslide=kidSlider.objects.all()
    kdata=kidContent.objects.all()
    data={
        'kslide':kslide,
        'kdata':kdata
    }
    return render(request,'Kid_index.html',data) 

def beauty(request):
    bslide=beautySlider.objects.all()
    bdata=beautyContent.objects.all()
    data={
        'bslide':bslide,
        'bdata':bdata
    }
    return render(request,'Beauty_index.html',data) 

def decor(request):
    dslide=decorSlider.objects.all()
    ddata=decorContent.objects.all()
    data={
        'dslide':dslide,
        'ddata':ddata
    }
    return render(request,'Decor_index.html',data) 

def electronics(request):
    eslide=electronicsSlider.objects.all()
    edata=electronicsContent.objects.all()
    data={
        'eslide':eslide,
        'edata':edata
    }
    return render(request,'Electronics_index.html',data) 

def mobile(request):
    mslide=mobileSlider.objects.all()
    mdata=mobileContent.objects.all()
    data={
        'mslide':mslide,
        'mdata':mdata
    }
    return render(request,'Mobile_index.html',data) 