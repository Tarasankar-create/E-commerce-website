from django.urls import path
from . import views

urlpatterns=[
    path('cart/',views.cart,name='cart'),
    path('add_to_cart/',views.add_to_cart,name='add_to_cart'),
    path('remove_from_cart/',views.remove_from_cart,name='remove_from_cart'),
    path('checkout/',views.checkOut,name='checkout'),
    path('payment/',views.payment,name='payment'),
    path('processPayment/',views.process_payment,name='process_payment'),
    path('creditcard/',views.creditcard,name='credit'),
    path('upi/',views.upi,name='Upi'),
    path('payment_process/',views.payment_process,name='payprocess'),
    path('order_success/',views.order_success,name='order_success'),
]