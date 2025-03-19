from django.shortcuts import render
from django.http import JsonResponse
from home.models import menContent

def cart(request):
    return render(request,'cart.html')

def add_to_cart(request):
    if request.method=='POST':
        id=request.POST.get('id')
        catagory=request.POST.get('catagory')
        
        if "cart" not in request.session:
            request.session['cart']=[]
        cart=request.session['cart']
        found=False

        for item in cart:
            if item['id']==id:
                item['quantity']+=1
                found=True
                break
        if not found:
            if catagory=="menContent":
                prod=menContent.objects.filter(id=id).values(
                    "id","image_url","men_title","total","discount","dis_price"
                ).first()

           
    return JsonResponse({'message':'complete'},status=200)