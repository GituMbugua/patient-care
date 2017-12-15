from django import forms
from django.forms import extras
from .models import Profile, Patient

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['injury', 'status']

class UpdateInfoForm(forms.ModelForm):
    class Meta:
        dob = forms.DateField(widget=extras.SelectDateWidget)
        model = Patient
        fields = ['first_name', 'last_name', 'dob', 'gender', 'phone_number', 'email', 'injury', 'blood_type', 'weight', 'height', 'occupation', 'status', 'notes']
