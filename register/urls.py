from django.urls import path
from . import views

urlpatterns=[
    path('signup/',views.register,name='signup'),
    path('login/',views.login,name='login'),
    path('update/',views.update_view,name='update'),
    path('logout/',views.logout_view,name='logout'),
]