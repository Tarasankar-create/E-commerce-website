"""
URL configuration for mywebsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from home import views as hviews
from register import urls


urlpatterns = [
    path('admin/', admin.site.urls),
    #Home
    path('',hviews.home,name='home' ),
    path('menfashion/',hviews.menFashion,name='menFashion' ),
    path('womenfashion/',hviews.womenFashion,name='womenFashion' ),
    path('kidfashion/',hviews.kidFashion,name='kidFashion' ),
    path('beauty/',hviews.beauty,name='beauty' ),
    path('decor/',hviews.decor,name='decor' ),
    path('electronics/',hviews.electronics,name='electronics' ),
    path('mobile/',hviews.mobile,name='mobile' ),
    #Register
    path('register/',include('register.urls')),
    #Customer
    path('customer/',include('customer.urls'))
   
]
