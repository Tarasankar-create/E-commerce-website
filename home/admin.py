from django.contrib import admin
from .models import menContent,menSlider,womenSlider,womenContent,kidSlider,kidContent,decorSlider,decorContent,beautySlider,beautyContent,electronicsSlider,electronicsContent,mobileSlider,mobileContent
# Register your models here.

admin.site.register(menSlider)
admin.site.register(menContent)

admin.site.register(womenSlider)
admin.site.register(womenContent)

admin.site.register(kidSlider)
admin.site.register(kidContent)

admin.site.register(decorSlider)
admin.site.register(decorContent)

admin.site.register(beautySlider)
admin.site.register(beautyContent)

admin.site.register(electronicsSlider)
admin.site.register(electronicsContent)

admin.site.register(mobileSlider)
admin.site.register(mobileContent)