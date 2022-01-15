

from django.urls import path

from covidapp import views
app_name='covidapp'

urlpatterns = [

path('',views.covidreg,name='covidreg'),
    path('<slug:c_slug>/',views.covidreg,name='places'),
    ]