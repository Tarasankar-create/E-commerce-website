from django.contrib import admin
from .models import Catagories,homeSlider,homeContSlider1,homeContSlider2,menContent,menSlider,womenSlider,womenContent,kidSlider,kidContent,decorSlider,decorContent,beautySlider,beautyContent,electronicsSlider,electronicsContent,mobileSlider,mobileContent
# Register your models here.

admin.site.register(Catagories)
admin.site.register(homeSlider)
admin.site.register(homeContSlider1)
admin.site.register(homeContSlider2)

class userMen(admin.ModelAdmin):
    list_display=("id","men_title")

admin.site.register(menSlider)
admin.site.register(menContent,userMen)

class userWomen(admin.ModelAdmin):
    list_display=("id","w_title")

admin.site.register(womenSlider)
admin.site.register(womenContent,userWomen)

class userKid(admin.ModelAdmin):
    list_display=("id","k_title")

admin.site.register(kidSlider)
admin.site.register(kidContent,userKid)

class userDecor(admin.ModelAdmin):
    list_display=("id","d_title")

admin.site.register(decorSlider)
admin.site.register(decorContent,userDecor)

class userBeauty(admin.ModelAdmin):
    list_display=("id","b_title")

admin.site.register(beautySlider)
admin.site.register(beautyContent,userBeauty)

class userElectronics(admin.ModelAdmin):
    list_display=("id","e_title")

admin.site.register(electronicsSlider)
admin.site.register(electronicsContent,userElectronics)

class userMobile(admin.ModelAdmin):
    list_display=("id","m_title")

admin.site.register(mobileSlider)
admin.site.register(mobileContent,userMobile)