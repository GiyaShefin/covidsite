from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
from .models import City

class CityAdmin(admin.ModelAdmin):
    list_display = ['name','url']
    prepopulated_fields = { 'slug':('name','url')}
    admin.site.register(City)
