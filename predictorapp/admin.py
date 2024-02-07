from django.contrib import admin
from .models import Tomato
from .models import Potato
from .models import Cotton
# Register your models here.

@admin.register(Tomato)
class TomatoShow(admin.ModelAdmin):
    list_display=("tomato",'id')
    
@admin.register(Potato)
class PotatoShow(admin.ModelAdmin):
    list_display=("potato",'id')
    

@admin.register(Cotton)
class CottonShow(admin.ModelAdmin):
    list_display=("cotton",'id')
    

    
    
