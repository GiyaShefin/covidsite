from django.shortcuts import render

from patientdetails.models import City, Town


def detail_patient(request):
    return render(request, 'vaccinationbooking.html')

def cities(request):
    cities = City.objects.all()
    context = {'cities': cities}
    return render(request, 'vaccinationbooking.html', context)


def towns(request):
    city = request.GET.get('city')
    towns = Town.objects.filter(city=city)
    context = {'towns': towns}
    return render(request, 'vaccinationbooking.html', context)
# details1 = PatientsDetails.objects.all()
# # if request.method == 'POST':
# 	name = request.POST.get('name', '')
# 	dob = request.POST.get('date', '')
# 	address=request.POST.get('address','')
# 	district=request.POST.get('district','')
# 	Firstdose=request.POST.get('Fisrtdose','')
# 	Seconddose=request.POST.get('Seconddose','')
#     patientdetails=Pa

def success_page(request):
    return render(request, 'success.html')


# Create your views here.
