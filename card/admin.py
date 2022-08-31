from django.contrib import admin
from . models import contact, invcard, team, faq, offer

from django.utils.html import format_html

class iadmin(admin.ModelAdmin):
    list_display= ('code','category','date','photo_tag')
    list_per_page= 10

    def photo_tag(self, obj):
        return format_html(f'<img src= "/media/{obj.image}" style= "height:100px;width:"100px>')
    
class cadmin(admin.ModelAdmin):
    list_display= ('name','email','number', 'message')  
    def message(self, obj):
        return obj.desc  

class fadmin(admin.ModelAdmin):
    list_display= ('question','answer')

class tadmin(admin.ModelAdmin):
    list_display= ('name','work','content', 'image_tag')
    def image_tag(self, obj):
        return format_html(f'<img src= "/media/{obj.image}" style= "height:100px;width:"100px>')    

class oadmin(admin.ModelAdmin):
    list_display= ('oname','offer1', 'offer2')
    

admin.site.register(invcard, iadmin)
admin.site.register(contact, cadmin)
admin.site.register(faq, fadmin)
admin.site.register(team, tadmin)
admin.site.register(offer, oadmin)


# Register your models here.