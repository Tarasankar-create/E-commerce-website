from django.shortcuts import render,redirect
import re
from django.http import JsonResponse
from home.models import menContent,womenContent,kidContent,beautyContent,decorContent,electronicsContent,mobileContent

def cart(request):
    cart=request.session.get('cart',[])
    return render(request,'cart.html',{"cart":cart})

def add_to_cart(request):
    if request.method == 'POST':
        id=request.POST.get('id')
        catagory=request.POST.get('catagory')
        
        if "cart" not in request.session:
            request.session['cart']=[]
        cart=request.session['cart']
        found=False

        for item in cart:
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

def checkOut(request):
    cart=request.session.get("cart",[])
    final_amount=0
    total_product=len(cart)
    for item in cart:
        final_price=float(item['dis_price'].replace(',',''))*float(item['quantity'])
        item['total_price']=round(final_price,3)
        final_amount+=final_price
    request.session['cart']=cart
    request.session['total_amount']=round(final_amount,2)

    return render(request,'checkout.html',{'cart':cart,'total_amount':final_amount,'total':total_product})

def payment(request):
    total_amount=request.session.get("total_amount",0)
    if total_amount==0:
        return render(request,'cart.html')
    
    return render(request,'payment_options.html',{'total':total_amount})

def process_payment(request):
    if request.method == "POST":
        payment=request.POST.get("payment")
        payPal="https://www.paypal.com/in/home"
        print(payment)
        if payment=="Creditcard":
            return redirect('credit')
        elif payment=="upi":
            return redirect('Upi')
        elif payment =="paypal":
            return redirect(payPal)
        elif payment =="cod":
            return redirect('order_success')
        else:
            total=request.session.get("total_amount",0)
            return render(request,"payment_options.html",{"msg":"Invalid ! Please choose a valid payment method","total":total})

    return render(request,'payment_options.html')
def creditcard(request):
    if request.method == "POST":
        total=request.session.get("total_amount",0)
        card=request.POST.get("card")
        cardNum=request.POST.get("cardNum")
        cardCvv=request.POST.get("cardCvv")
        list_special="!~`#$%^&*()-_+=;:'\"*/ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefhijklmnopqrstuvwxyz"
        if (len(cardNum)==16 and len(cardCvv)==3):
            if any(num in list_special  for num in cardNum):
                return render(request,'card_payment.html',{"msg":f"Invalid {card} card Number","total":total})
            elif any(cvv in list_special  for cvv in cardCvv):
                return render(request,'card_payment.html',{"msg":"Invalid CVV","total":total})
            else:
                return redirect('payprocess')
        else:
            return render(request,"card_payment.html",{"msg":f"Please enter valid {card} card number or cvv"})
    return render(request,'card_payment.html')
def upi(request):
    if request.method == 'POST':
        upiNum=request.POST.get('upiNum')
        list_match="^[0-9]{10}@[a-z]{3}"
        if re.match(list_match,upiNum):
            return redirect('payprocess')
        else:
            return render(request,'upi_payment.html',{"msg":"Error ! Please enter valid upi number"})
    return render(request,'upi_payment.html')
def payment_process(request):
    return render(request,'processing_payment.html')
def order_success(request):
    request.session['cart']=[]
    request.session['total_amount']=0
    return render(request,'order_success.html')