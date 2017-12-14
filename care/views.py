from django.shortcuts import render, redirect
from django.http import JsonResponse, Http404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Profile, Patient
from .forms import PatientForm

@login_required(login_url='/accounts/login/')
def home(request):
    patients = Patient.objects.all().order_by('status')

    title = 'Patient Care'
    return render(request, 'home.html', {"title":title, "patients":patients})

@login_required(login_url='/accounts/login/')
def add_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, ('Your patient has been added.'))
            
            return redirect(home)
    else:
        form = PatientForm()
    
    title = 'Add Patient'
    return render(request, 'add_patient.html', {"title":title, "form":form})

def patient(request, id):
    patient = Patient.objects.get(id=id)

    if patient.first_name:
        title = f"{patient.first_name} Records"
    title = 'Patient Records'
    
    return render(request, 'patient.html', {"title":title, "patient":patient})
    