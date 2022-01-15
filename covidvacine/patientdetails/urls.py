from django.urls import path
from . import views

app_name = "patientdetails"


urlpatterns = [
    path("detail",views.detail_patient, name="detail_patient"),
    path('success',views.success_page,name="success_page"),
path('cities', views.cities, name='cities'),
    path('towns/', views.towns, name='towns'),
]