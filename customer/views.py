from django.shortcuts import render,redirect
import re
from django.http import JsonResponse
from home.models import menContent,womenContent,kidContent,beautyContent,decorContent,electronicsContent,mobileContent
from django.conf import settings
from django.views.decorators.http import require_GET,require_POST,require_http_methods

def cart(request):
    cart=request.session.get('cart',[])
    return render(request,'cart.html',{"cart":cart})

@require_POST
def add_to_cart(request):
    if request.method == 'POST':
        Id=request.POST.get('id')
        catagory=request.POST.get('catagory')
        
        if "cart" not in request.session:
            request.session['cart']=[]
        cart=request.session['cart']
        found=False

        for item in cart:
            if item['id']==int(Id) and item['Catagory']==catagory:
                item['quantity']=item['quantity']+1
                found=True
                #print("After update",item['quantity'])
                break
        if not found:
            if catagory=="menContent":
                prod=menContent.objects.filter(id=Id).values(
                    "id","image_url","men_title","total","discount","dis_price"
                ).first()
            elif catagory =="womenContent":
                prod=womenContent.objects.filter(id=Id).values(
                    "id","image_url","w_title","total","discount","dis_price"
                ).first()
            elif catagory == "kidContent":
                prod=kidContent.objects.filter(id=Id).values(
                    "id","image_url","k_title","total","discount","dis_price"
                ).first()
            elif catagory == "beautyContent":
                prod=beautyContent.objects.filter(id=Id).values(
                    "id","image_url","b_title","total","discount","dis_price"
                ).first()
            elif catagory == "decorContent":
                prod=decorContent.objects.filter(id=Id).values(
                    "id","image_url","d_title","total","discount","dis_price"
                ).first()
            elif catagory == "electronicsContent":
                prod=electronicsContent.objects.filter(id=Id).values(
                    "id","image_url","e_title","total","discount","dis_price"
                ).first()
            elif catagory == "mobileContent":
                prod=mobileContent.objects.filter(id=Id).values(
                    "id","image_url","m_title","total","discount","dis_price"
                ).first()
            else:
                return JsonResponse({'message':"Invalid content"},status=400)
            
            if prod:
                prod_data={
                    'id':prod['id'],
                    'img':settings.MEDIA_URL + str(prod['image_url']).lstrip('/'),
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

@require_POST
def remove_from_cart(request):
    if request.method == 'POST':
        Id=request.POST.get('id')
        catagory=request.POST.get('catagory')
        cart=request.session.get('cart',[])
        for item in cart:
            print("Before",item)
            if item['id']==int(Id) and item['Catagory']==catagory:
                cart.remove(item)
                break
        request.session['cart']=cart
        request.session.modified=True
    return JsonResponse({'message':'Item removed'},status=200)

@require_GET
def checkout(request):
    cart=request.session.get("cart",[])
    final_amount=0
    total_product=len(cart)
    for item in cart:
        final_price=float(item['dis_price'].replace(',',''))*float(item['quantity'])
        item['total_price']=(f'{final_price:.2f}')
        final_amount+=final_price
    request.session['cart']=cart
    request.session['total_amount']=f'{final_amount:.2f}'

    return render(request,'checkout.html',{'cart':cart,'total_amount':f'{final_amount:.2f}','total':total_product})

@require_GET
def payment(request):
    total_amount=request.session.get("total_amount",0)
    if total_amount==0:
        return render(request,'cart.html')
    
    return render(request,'payment_options.html',{'total':total_amount})

@require_POST
def process_payment(request):
    if request.method == "POST":
        payment=request.POST.get("payment")
        paypal="https://www.paypal.com/in/home"
        print(payment)
        if payment=="Creditcard":
            return redirect('credit')
        elif payment=="upi":
            return redirect('Upi')
        elif payment =="paypal":
            return redirect(paypal)
        elif payment =="cod":
            return redirect('order_success')
        else:
            total=request.session.get("total_amount",0)
            return render(request,"payment_options.html",{"msg":"Invalid ! Please choose a valid payment method","total":total})

    return render(request,'payment_options.html')

@require_POST
def creditcard(request):
    card_payment_template="card_payment.html"
    if request.method == "POST":
        total=request.session.get("total_amount",0)
        card=request.POST.get("card")
        cardnum=request.POST.get("cardNum")
        cardcvv=request.POST.get("cardCvv")
        list_special="!~`#$%^&*()-_+=;:'\"*/ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefhijklmnopqrstuvwxyz"
        if (len(cardnum)==16 and len(cardcvv)==3):
            if any(num in list_special  for num in cardnum):
                return render(request,card_payment_template,{"msg":f"Invalid {card} card Number","total":total})
            elif any(cvv in list_special  for cvv in cardcvv):
                return render(request,card_payment_template,{"msg":"Invalid CVV","total":total})
            else:
                return redirect('payprocess')
        else:
            return render(request,card_payment_template,{"msg":f"Please enter valid {card} card number or cvv"})
    return render(request,card_payment_template)

@require_POST
def upi(request):
    if request.method == 'POST':
        upinum=request.POST.get('upiNum')
        list_match= r"^\d{10}@[a-z]{3}$"
        if re.match(list_match,upinum):
            return redirect('payprocess')
        else:
            return render(request,'upi_payment.html',{"msg":"Error ! Please enter valid upi number"})
    return render(request,'upi_payment.html')

@require_GET
def payment_process(request):
    return render(request,'processing_payment.html')

@require_GET
def order_success(request):
    request.session['cart']=[]
    request.session['total_amount']=0
    return render(request,'order_success.html')
