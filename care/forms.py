from django import forms
from .models import Profile, Department, Patient

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['injury', 'status']