from django.shortcuts import render, redirect
from django.http import JsonResponse, Http404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Profile, Patient
from .forms import PatientForm, UpdateInfoForm

@login_required(login_url='/accounts/login/')
def home(request):
    patients = Patient.objects.all().order_by('status')

    if request.method == 'POST':
        form = PatientForm(request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, ('Your patient has been added.'))
            
            return redirect(home)
    else:
        form = PatientForm()

    title = 'Patient Care'
    return render(request, 'home.html', {"title":title, "patients":patients, "form":form})

@login_required(login_url='/accounts/login/')
def patient(request, id):
    patient = Patient.objects.get(id=id)

    if request.method == 'POST':
        form = UpdateInfoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, ('You have successfully updated the patient information.'))
            
            return redirect(home)
    else:
        form = UpdateInfoForm()

    if patient.first_name:
        title = f"{patient.first_name} Records"
    title = 'Patient Records'
    
    return render(request, 'patient.html', {"title":title, "patient":patient, "form":form})

def update_info(request, id):
    pass
