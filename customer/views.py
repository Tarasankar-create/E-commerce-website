from django.shortcuts import render
from django.http import JsonResponse
from home.models import menContent,womenContent,kidContent,beautyContent,decorContent,electronicsContent,mobileContent

def cart(request):
    cart=request.session.get('cart',[])
    return render(request,'cart.html',{"cart":cart})

def add_to_cart(request):
    if request.method == 'POST':
        id=request.POST.get('id')
        catagory=request.POST.get('catagory')
        print("sent data",type(id))
        print("sent data",type(catagory))
        
        if "cart" not in request.session:
            request.session['cart']=[]
        cart=request.session['cart']
        found=False

        for item in cart:
            print("cart data",item['id'])
            print("cart data",type(item['id']))
            print("cart data",type(item['Catagory']))
            print("cart data",item['Catagory'])
            if item['id']==int(id) and item['Catagory']==catagory:
                item['quantity']=item['quantity']+1
                found=True
                print("After update",item['quantity'])
                break
        if not found:
            if catagory=="menContent":
                prod=menContent.objects.filter(id=id).values(
                    "id","image_url","men_title","total","discount","dis_price"
                ).first()
            elif catagory =="womenContent":
                prod=womenContent.objects.filter(id=id).values(
                    "id","image_url","w_title","total","discount","dis_price"
                ).first()
            elif catagory == "kidContent":
                prod=kidContent.objects.filter(id=id).values(
                    "id","image_url","k_title","total","discount","dis_price"
                ).first()
            elif catagory == "beautyContent":
                prod=beautyContent.objects.filter(id=id).values(
                    "id","image_url","b_title","total","discount","dis_price"
                ).first()
            elif catagory == "decorContent":
                prod=decorContent.objects.filter(id=id).values(
                    "id","image_url","d_title","total","discount","dis_price"
                ).first()
            elif catagory == "electronicsContent":
                prod=electronicsContent.objects.filter(id=id).values(
                    "id","image_url","e_title","total","discount","dis_price"
                ).first()
            elif catagory == "mobileContent":
                prod=mobileContent.objects.filter(id=id).values(
                    "id","image_url","m_title","total","discount","dis_price"
                ).first()
            else:
                return JsonResponse({'message':"Invalid content"},status=400)
            
            if prod:
                prod_data={
                    'id':prod['id'],
                    'img':prod['image_url'],
                    'total':prod['total'],
                    'discount':prod['discount'],
                    'dis_price':prod['dis_price'],
                    'quantity':1,
                    'Catagory':catagory
                }
                if catagory=="menContent":
                    prod_data['title']=prod['men_title']
                elif catagory =="womenContent":
                    prod_data['title']=prod['w_title']
                elif catagory == "kidContent":
                    prod_data['title']=prod['k_title']
                elif catagory == "beautyContent":
                    prod_data['title']=prod['b_title']
                elif catagory == "decorContent":
                    prod_data['title']=prod['d_title']  
                elif catagory == "electronicsContent":
                    prod_data['title']=prod['e_title']  
                elif catagory == "mobileContent":
                    prod_data['title']=prod['m_title']   
                else:
                    return JsonResponse({'message':"No title found"},status=400)
                
            
                cart.append(prod_data)
                request.session.modified=True
                return JsonResponse({'message':'Item successfully added'},status=200)      

        request.session['cart']=cart 
        request.session.modified=True
    return JsonResponse({'message':'Item successfully added'},status=200)

def remove_from_cart(request):
    if request.method == 'POST':
        id=request.POST.get('id')
        catagory=request.POST.get('catagory')
        cart=request.session.get('cart',[])
        for item in cart:
            print("Before",item)
            if item['id']==int(id) and item['Catagory']==catagory:
                cart.remove(item)
                break
        request.session['cart']=cart
        request.session.modified=True
    return JsonResponse({'message':'Item removed'},status=200)