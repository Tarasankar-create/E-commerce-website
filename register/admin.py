from django.contrib import admin
from .models import signup

class userSignup(admin.ModelAdmin):
    list_display=("name","mob","email")

admin.site.register(signup,userSignup)
