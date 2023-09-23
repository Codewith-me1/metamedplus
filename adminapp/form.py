from django.forms import ModelForm
from .models import AppointmentDetails
class AppointmentDetailsForm(ModelForm):
  class Meta:
    model = AppointmentDetails  
    fields = ['patient_name', 'appointment_no', 'appointment_date', 'phone', 'gender', 'doctor', 'source', 'priority', 'fees', 'status']