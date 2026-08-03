from django.contrib import admin
from .models import Catagories,homeSlider,homeContSlider1,homeContSlider2,menContent,menSlider,womenSlider,womenContent,kidSlider,kidContent,decorSlider,decorContent,beautySlider,beautyContent,electronicsSlider,electronicsContent,mobileSlider,mobileContent
# Register your models here.

admin.site.register(Catagories)
admin.site.register(homeSlider)
admin.site.register(homeContSlider1)
admin.site.register(homeContSlider2)

class user_men(admin.ModelAdmin):
    list_display=("id","men_title")

admin.site.register(menSlider)
admin.site.register(menContent,user_men)

class user_women(admin.ModelAdmin):
    list_display=("id","w_title")

admin.site.register(womenSlider)
admin.site.register(womenContent,user_women)

class user_kid(admin.ModelAdmin):
    list_display=("id","k_title")

admin.site.register(kidSlider)
admin.site.register(kidContent,user_kid)

class user_decor(admin.ModelAdmin):
    list_display=("id","d_title")

admin.site.register(decorSlider)
admin.site.register(decorContent,user_decor)

class user_beauty(admin.ModelAdmin):
    list_display=("id","b_title")

admin.site.register(beautySlider)
admin.site.register(beautyContent,user_beauty)

class user_electronics(admin.ModelAdmin):
    list_display=("id","e_title")

admin.site.register(electronicsSlider)
admin.site.register(electronicsContent,user_electronics)

class user_mobile(admin.ModelAdmin):
    list_display=("id","m_title")

admin.site.register(mobileSlider)
admin.site.register(mobileContent,user_mobile)