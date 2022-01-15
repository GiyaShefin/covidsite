from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
from django.contrib import admin
from . models import PatientsDetails,City,Town

# Register your models here.
admin.site.register(PatientsDetails)

class CityAdmin(admin.ModelAdmin):
    list_display = ['name']
admin.site.register(City,CityAdmin)

class TownAdmin(admin.ModelAdmin):
    list_display = ['name']
admin.site.register(Town,TownAdmin)