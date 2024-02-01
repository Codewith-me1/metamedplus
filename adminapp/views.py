from django.shortcuts import render
import json, sys
from decimal import Decimal
# Create your views here.
import time
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
import requests
import os
from channels.layers import get_channel_layer
from .models import Other_Attendance
from .models import Bag_available
from .models import Address

from twilio.rest import Client
from .models import Attendance
from django.contrib import messages
from pusher_push_notifications import PushNotifications
from .models import POS

GTK_FOLDER = 'C:\\Program Files\\GTK3-Runtime Win64\\bin'
os.environ['PATH'] = GTK_FOLDER + os.pathsep + os.environ.get('PATH', '')
# from weasyprint import HTML
import pusher

from io import BytesIO

from.models import Blood_Component
from django.template.loader import get_template
from reportlab.pdfgen import canvas

from .models import Blood_Setup
from .models import BRS
from .models import Leaves
import datetime
from .models import Operation_category,Operation_name
from .models import BankBook
from .models import Bank
from asgiref.sync import async_to_sync
from .models import Operation_Assistants
from django.core.mail import EmailMessage, get_connection
import stripe
from .models import Stock
from .models import Postal_dispatch
from .models import Medicine_Composition
from .models import Postal_receive
from .models import Precreption,Precreption_Item
from django.conf import settings
from datetime import datetime, timedelta
from .models import CashBook
# from .models import Pos_item,POS
from django.forms.models import model_to_dict
from .models import ComplainType
from .models import Liablity
from .models import Wallet
from .models import Depreciation
from django.core.serializers import serialize
from .models import Wallet_Transactions
from django.shortcuts import get_object_or_404

from .models import Visitors
from .models import Complain
from .models import SMTPServer
from .models import Complain_source
from django.urls import reverse
from .models import ChatMessages
from .models import DeathRecord
from .models import CustomUser
import re
from .models import BankAccount
from .models import Notice
import smtplib
from email.mime.text import MIMEText
from .models import Ads
from email.mime.multipart import MIMEMultipart
from .models import Expense_Category
from django.contrib.auth import logout
from .models import Payroll
from .models import Asset
from .models import Transaction
from datetime import date
from .models import Referral_commission
from django.db.models import Sum
from django.db.models.functions import Coalesce 
from .models import Purchase
from .models import Item_Acc
from .models import Consultant_register
from django.core.mail import send_mail
from .models import Operation
from .models import MedicationDoseage
from .models import header
from django.utils.datastructures import MultiValueDictKeyError
import decimal
from .models import Expense_inv_Item
from .models import Expense_Item
from .models import Expense_Invoice
from .models import Payment_In
from .models import Ipd_Payments
from .models import Party
from django.core import serializers
from .models import NursingRecord ,DoctorNote
from .models import Unit
from .models import Sales_Invoice
from .models import ChargeType
from urllib.parse import unquote
from django.template.loader import get_template
from django.db.models import Sum, F, ExpressionWrapper, DecimalField
from .models import Item_Invoice
from django.shortcuts import render
from xhtml2pdf import pisa

from .models import Zoom
from .models import Category
from .models import MedicationDose
from django.db.models import F, Sum, DecimalField
from .models import Task
from .models import OpdPatient
from .models import Radiology

from django.shortcuts import render
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from .form import AppointmentDetailsForm


from .models import AppointmentDetails
from .models import Patient
from .models import AddStaff
from .models import Role
from .models import BedGroup, Bedtype, Bed,Floor
from .models import  Symtopms, IpdPatient
from .models import Med_Category, Med_Details, Supplier
from .models import Donor_det,BloodDonation_component, BloodDonation
from .models import Path_Category,Path_Parameter
from .models import Path_Parameter
from django.contrib.contenttypes.models import ContentType
from . models import Charge
from .models import Module_Charge
from .models import Tax_cat 
from .models import Pathology_test
from .models import MedicineCategory
from .models import Pathology
from .models import Income,Expense
from .models import IncomeHead ,ExpenseHead
from .models import TPA
from .models import ChildBirth
from .models import ReferralCategory ,ReferralPerson ,Referral
from .models import add_ambulancecall
from .models import Ambulance
from .models import ItemCategory
from .models import Store
from .models import SupplierDetails
from .models import Item
from .models import ItemStock
from .models import Path_Category
from django.contrib.auth.decorators import login_required
from .models import Radio_Category,Radio_Parameter, Radiology_test
import secrets
import string
appin = "appointment"

def profile(request,id):

    staff  = AddStaff.objects.get(staff_id=id)
    
    
    try:
        payroll = Payroll.objects.get(staff=id)
        context = {
            'payroll':payroll,
            
        }
    except Payroll.DoesNotExist:
            # Handle the case where the patient does not exist
            print('none found')

    try:
        leave = Leaves.objects.get(staff=id)
        context = {
            'leave':leave,
            
        }
    except Leaves.DoesNotExist:
        context={
            'staff':staff,
        }
    context ={
        'staff':staff,
        
        
    }
    return render(request,'admin/admin_profile.html',context)



from django.contrib.auth import authenticate
from django.contrib.auth import login as log
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm



def pathalogist(request):
    total_radio = Radiology.objects.all().aggregate(
        total_balance=Sum(F('net_amount'))
        )['total_balance'] or 0
    context = {
        'radio':total_radio,
    }
    return render(request,'panels/pathalogy.html',context)
def login(request):
     if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        man = [form.data]
        print(man)
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(password)
        print(username)
        user = authenticate(username=username, password=password)
        
        total_opd = OpdPatient.objects.all().aggregate(
        total_opd=Sum(F('amount'))
        )['total_opd'] or 0

       
        total_ipd = Ipd_Payments.objects.all().aggregate(
        total_balance=Sum(F('amount'))
        )['total_balance'] or 0
        total_opd = OpdPatient.objects.all().aggregate(
        total_opd=Sum(F('amount'))
        )['total_opd'] or 0

       
        total_ipd = Ipd_Payments.objects.all().aggregate(
        total_balance=Sum(F('amount'))
        )['total_balance'] or 0
    
        total_path = Pathology.objects.all().aggregate(
        total_balance=Sum(F('net_amount'))
        )['total_balance'] or 0
    
        total_radio = Radiology.objects.all().aggregate(
        total_balance=Sum(F('net_amount'))
        )['total_balance'] or 0
    
        total_blood = BloodDonation.objects.all().aggregate(
        total_balance=Sum(F('net_amount'))
        )['total_balance'] or 0
    
        total_ambu = add_ambulancecall.objects.all().aggregate(
        total_balance=Sum(F('net_amount'))
             )['total_balance'] or 0
    
        total_med = Purchase.objects.all().aggregate(
        total_balance=Sum(F('amount'))
            )['total_balance'] or 0
    
        try:
            indirect_expense_category = Expense_Category.objects.get(expense_type='Indirect_Expense')
            indirect_expenses = Expense_Invoice.objects.filter(expense_category=indirect_expense_category)
            total_indirect_expense = indirect_expenses.aggregate(total_indirect=Sum('total'))['total_indirect'] or 0
        except Expense_Category.DoesNotExist:
            total_indirect_expense = 0

        try:
            direct_expense_type = Expense_Category.objects.get(expense_type='Direct_Expense')
            direct_expense = Expense_Invoice.objects.filter(expense_category=direct_expense_type)
            total_direct_expense = direct_expense.aggregate(total_direct=Sum('total'))['total_direct'] or 0
        except Expense_Category.DoesNotExist:
            total_direct_expense = 0

        income = Income.objects.all().aggregate(
        total_income= Sum(F('amount'))
        )['total_income']or 0

        doctor = AddStaff.objects.filter(role="Doctor").count()
        pathologist = AddStaff.objects.filter(role="Pathalogist").count()
        radiologist = AddStaff.objects.filter(role="Radiologist").count()
        nurse = AddStaff.objects.filter(role="Nurse").count()
        accountant = AddStaff.objects.filter(role="Accountant").count()

        expense = total_indirect_expense+total_direct_expense

        context ={
            'opd':total_opd,
            'ipd':total_ipd,
            'path':total_path,
            'blood':total_blood,
            'ambulance':total_ambu,
            'income':income,
            'med':total_med,
            'acc':accountant,
            'doctor':doctor,
            'nurse':nurse,
            'radiologist':radiologist,
            'pathalogist':pathologist,
            'radio':total_radio,
            'expense':expense,

            }
        
        if user is not None:
            log(request,user)
            if user.role == 'Doctor':
                return redirect('pathalogist')  # Redirect to the doctor's dashboard
            elif user.role == 'Admin':
                return redirect('doctor') 
            elif user.role == 'New':
                return redirect('doctor')
            elif user.role =='Manager':
                return redirect('doctor')
            elif user.role =='Radiologist':
                return redirect('pathalogist')
            elif user.role =='Pathologist': 
                return redirect('pathalogist')
            elif user.role =='Nurse':
                return redirect('pathalogist')
            
            elif user.role =='Pharmacist':
                return redirect('pathalogist')
            elif user.role =='Ipd Nurse':
                return redirect('pathalogist')
            
            elif user.role =='OPD':
                return redirect('pathalogist')
            
            elif user.role =='Front Office':
                return redirect('pathalogist')

            
        
            elif user.role =='Accountant':
                return redirect('doctor')
        
        
            elif user.role == "HumanResource":
                return redirect('pathalogist')
            elif user.role == "Cashier":
                return redirect('pathalogist')
            
            else:
                return redirect('doctor')

            # Redirect to the admin's dashboard or other role-specific redirects as needed

        
     else:  
            
            form = AuthenticationForm()

     return render(request, 'admin/login.html', {'form': form})


def adminapp(request):
  
  return render(request,'main/new.html')
# Create your views here.

def index(request):
   return render(request,'index.html')

# Appointment 


def generate_random_password(length=12):
    password_characters = string.ascii_letters + string.digits + string.punctuation
    print(password_characters)
    return ''.join(secrets.choice(password_characters) for i in range(length))




def appointment(request):
  

  appointments = AppointmentDetails.objects.all()
  patients = Patient.objects.all()
  doctors = AddStaff.objects.filter(role='Doctor')


  context = {
    'appointments': appointments,
    'patients':patients,
     "doctor":doctors,

    
  }

  return render(request,  appin+"/index.html",context)


def appointmentForm(request):
  patients = Patient.objects.all()
  doctors = AddStaff.objects.filter(role='Doctor')
  context={
     'patients':patients,
     "doctor":doctors,

  }
  return render(request,  appin+"/app_form.html",context)


def appointment_details_form_view(request):
   if request.method == 'POST':
        
        patient_id = request.POST.get('patient')
        
        
        if patient_id:
            patient = Patient.objects.get(id=patient_id)
            patient_name = patient


        new = request.POST.get('new')
        

        print(new)
        if new == 'true':
            name = request.POST['name']
            p_phone = request.POST['patient_phone']
            p_gender = request.POST['patient_gender']
            address = request.POST['patient_address']
            date_of_birth = request.POST['date_of_birth']
            patient = Patient(
                name = name,
                phone = p_phone,
                gender = p_gender,
                address = address,
                date_of_birth = date_of_birth,

            )
            patient.save()
            appointment_date = request.POST['appointment_date']
            phone = request.POST['phone']
            gender = request.POST['gender']
            doctor = request.POST['doctor']
            source = request.POST['source']
            priority = request.POST['priority']
            fees = request.POST['fees']
            status = request.POST['status']
            appointment = AppointmentDetails(
            patient_name=name,
            appointment_date=appointment_date,
            phone=phone,
            gender=gender,
            doctor=doctor,
            source=source,
            priority=priority,
            fees=fees,
            status=status
            )
            appointment.save()
            return redirect("appointment")
        else:
            

            appointment_date = request.POST['appointment_date']
            phone = request.POST['phone']
            gender = request.POST['gender']
            doctor = request.POST['doctor']
            source = request.POST['source']
            priority = request.POST['priority']
            fees = request.POST['fees']
            status = request.POST['status']



        # Create a new AppointmentDetails instance and save it to the database
        appointment = AppointmentDetails(
            patient_name=patient_name,
            appointment_date=appointment_date,
            phone=phone,
            gender=gender,
            doctor=doctor,
            source=source,
            priority=priority,
            fees=fees,
            status=status
        )
        appointment.save()
        return redirect("appointment")
   
   else:
        # Load the list of patients for the search input
      patients = AppointmentDetails.objects.all()
      context = {'patients': patients}
      return render(request, appin+"/app_form.html", context)
    

  

# Patient 

def patient_form(request):
    if request.method == 'POST':
        name = request.POST['name']
        date_of_birth = request.POST['date_of_birth']
        phone = request.POST['phone']
        gender = request.POST['gender']
        address = request.POST['address']

        # Create a new Patient instance and save it to the database
        patient = Patient(
            name=name,
            date_of_birth=date_of_birth,
            phone=phone,
            gender=gender,
            address=address
        )
        patient.save()
        return redirect('patient_list')
    
    return render(request, 'patient/patient_form.html')


def patient_list(request):
  patients = Patient.objects.all()

  context = {
    'patients': patients,
  }

  return render(request,  "patient/patient_list.html",context)


def pass_email(email, password):
    subject = 'Your New Account Password'
    message = f'Your new password is: {password}'
    from_email = 'programmer62563@gmail.com'  
    recipient_list = [email]

    try:
        send_mail(subject, message, from_email, recipient_list)
    except Exception as e:
       
        pass  

def add_staff(request):
    try:
        if request.method == 'POST':
            
            # role = request.POST.get('role')
            # designation = request.POST.get('designation')
            # department = request.POST.get('department')   
            # specialist = request.POST.get('specialist')
            # if patient_id:
            #     patient = Patient.objects.get(id=patient_id)
            #     patient_name = patient

            # Get data from the POST request
            staff_id = request.POST.get('staff_id')
            role = request.POST.get('role')
            designation = request.POST.get('designation','')
            department = request.POST.get('department','')
            specialist = request.POST.get('specialist','')
            first_name = request.POST.get('first_name','')
            last_name = request.POST.get('last_name','')
            father_name = request.POST.get('father_name','')
            mother_name = request.POST.get('mother_name','')
            gender = request.POST.get('gender','')
            marital_status = request.POST.get('marital_status','')
            blood_group = request.POST.get('blood_group','')
            date_of_birth = request.POST.get('date_of_birth','')
            date_of_joining = request.POST.get('date_of_joining','')
            phone = request.POST.get('phone')
            emergency_contact = request.POST.get('emergency_contact','')
            email = request.POST.get('email')
            current_address = request.POST.get('current_address','')
            permanent_address = request.POST.get('permanent_address','')
            photo = request.FILES.get('photo')
            
            
            qualification = request.POST.get('qualification', '')
            work_experience = request.POST.get('work_experience', '')
            specialization = request.POST.get('specialization', '')
            note = request.POST.get('note', '')

            # Identification Numbers
            pan_number = request.POST.get('pan_number', '')
            national_id_number = request.POST.get('national_id_number', '')
            local_id_number = request.POST.get('local_id_number', '')

            # Payroll and Salary
            payroll = request.POST.get('payroll', '')
            epf_no = request.POST.get('epf_no', '')
            basic_salary = request.POST.get('basic_salary',0)
            try:
                basic_salary = float(basic_salary)  # Try to convert the value to a float
            except ValueError:
                basic_salary = 0
            
            contract_type = request.POST.get('contract_type')

            # Work Details
            work_shift = request.POST.get('work_shift')
            work_location = request.POST.get('work_location')

            # Leave Information
            if 'paid_leave' in request.POST:
                paid_leave = True
            else:
                paid_leave = False
            number_of_leaves = request.POST.get('number_of_leaves')
            try:
                number_of_leaves = float(number_of_leaves)
                
            except ValueError:
                number_of_leaves

            # Bank Account Details
            account_title = request.POST.get('account_title', '')
            bank_account_no = request.POST.get('bank_account_no', '')
            bank_name = request.POST.get('bank_name', '')
            ifsc_code = request.POST.get('ifsc_code', '')
            bank_branch_name = request.POST.get('bank_branch_name', '')

            # Social Media Links
            facebook_url = request.POST.get('facebook_url', '')
            twitter_url = request.POST.get('twitter_url', '')
            linkedin_url = request.POST.get('linkedin_url', '')
            instagram_url = request.POST.get('instagram_url', '')

            # Documents
            resume = request.FILES.get('resume')
            joining_letter = request.FILES.get('joining_letter')
            other_documents = request.FILES.get('other_documents')
            print(photo)
            password = request.POST.get('password')
            # Create a Staff object and save it to the database
            staff = AddStaff(
                staff_id=staff_id,
                role=role,
                designation=designation,
                department=department,
                specialist=specialist,
                first_name=first_name,
                last_name=last_name,
                father_name=father_name,
                mother_name=mother_name,
                gender=gender,
                marital_status=marital_status,
                blood_group=blood_group,
                date_of_birth=date_of_birth,
                date_of_joining=date_of_joining,
                phone=phone,
                emergency_contact=emergency_contact,
                email=email,
                current_address=current_address,
                photo=photo,
                permanent_address=permanent_address,
                qualification=qualification,
                work_experience=work_experience,
                specialization=specialization,
                note=note,
                pan_number=pan_number,
                national_id_number=national_id_number,
                local_id_number=local_id_number,
                payroll_new=payroll,
                epf_no=epf_no,
                basic_salary=basic_salary,
                contract_type=contract_type,
                work_shift=work_shift,
                work_location=work_location,
                paid_leave=paid_leave,
                number_of_leaves=number_of_leaves,
                account_title=account_title,
                bank_account_no=bank_account_no,
                bank_name=bank_name,
                ifsc_code=ifsc_code,
                bank_branch_name=bank_branch_name,
                facebook_url=facebook_url,
                twitter_url=twitter_url,
                linkedin_url=linkedin_url,
                instagram_url=instagram_url,
                resume=resume,
                joining_letter=joining_letter,
                other_documents=other_documents
                # Add other fields here
            )


            # Save the Staff object to the database
            # password = generate_random_password()
            # message = "Your Password Is " + password

            # subject = "Password"
            
            staff.save()
        

            # Redirect to a success page or staff list page
            

            User = CustomUser.objects.create_user(id=staff_id,username=email, email=email, password=password, role=role)
            
            
            

            

            User.save()
            
            return redirect("staff_list")
        
        

        else:
            # Render the form for adding staff information
            role = Role.objects.all()
            context = {
            "role":role, 
            }
        
            return render(request, 'hr/hr.html',context)
    
    except Exception as e:
        # If an error occurs, delete the created staff object
        if staff:
            staff.delete()
        # Log the error or handle it accordingly
        print(f"Error during staff creation: {str(e)}")
        # You can add additional error handling here if needed
        # ...
        messages.error(request, f"Error during staff creation: {str(e)}")
        # Redirect to an error page or the form page with an error message
        return redirect('staff_list')
    


def staff(request):
  staff = AddStaff.objects.all()
  context={
     'staff':staff,

  }
  return render(request,"hr/listhr.html",context)



def role(request):
   role = Role.objects.all()
   context ={
       'role':role,
   }
   return render(request,"hr/role.html",context)


def role_form(request):
    if request.method == 'POST':
        # Get data from the POST request
        
        
        role = request.POST.get('role') 
        designation = request.POST.get('designation')
        department = request.POST.get('department')
        specialist = request.POST.get('specialist')
        roles = role.strip()

        # Create a Staff object and save it to the database
        staff = Role(
          
            role=roles,
            designation=designation,
            department=department,
            specialist=specialist,
            
            # Add other fields here
        )

        # Save the Staff object to the database
        staff.save()

        # Redirect to a success page or staff list page
        return redirect('role')
       
    role = Role.objects.all()
    context ={
       'role':role,
    }
        # Render the form for adding staff information
    return render(request, 'hr/role.html',context)
    
 
def doctor(request):
    total_opd = OpdPatient.objects.all().aggregate(
    total_opd=Sum(F('amount'))
        )['total_opd'] or 0

       
    total_ipd = Ipd_Payments.objects.all().aggregate(
        total_balance=Sum(F('amount'))
        )['total_balance'] or 0
    
    total_path = Pathology.objects.all().aggregate(
        total_balance=Sum(F('net_amount'))
        )['total_balance'] or 0
    
    total_radio = Radiology.objects.all().aggregate(
        total_balance=Sum(F('net_amount'))
        )['total_balance'] or 0
    
    total_blood = BloodDonation.objects.all().aggregate(
        total_balance=Sum(F('net_amount'))
        )['total_balance'] or 0
    
    total_ambu = add_ambulancecall.objects.all().aggregate(
        total_balance=Sum(F('net_amount'))
        )['total_balance'] or 0
    
    total_med = Purchase.objects.all().aggregate(
        total_balance=Sum(F('amount'))
        )['total_balance'] or 0
    
    try:
        indirect_expense_category = Expense_Category.objects.get(expense_type='Indirect_Expense')
        indirect_expenses = Expense_Invoice.objects.filter(expense_category=indirect_expense_category)
        total_indirect_expense = indirect_expenses.aggregate(total_indirect=Sum('total'))['total_indirect'] or 0
    except Expense_Category.DoesNotExist:
        total_indirect_expense = 0

    try:
        direct_expense_type = Expense_Category.objects.get(expense_type='Direct_Expense')
        direct_expense = Expense_Invoice.objects.filter(expense_category=direct_expense_type)
        total_direct_expense = direct_expense.aggregate(total_direct=Sum('total'))['total_direct'] or 0
    except Expense_Category.DoesNotExist:
        total_direct_expense = 0

    income = Income.objects.all().aggregate(
        total_income= Sum(F('amount'))
    )['total_income']or 0

    doctor = AddStaff.objects.filter(role="Doctor").count()
    pathologist = AddStaff.objects.filter(role="Pathalogist").count()
    radiologist = AddStaff.objects.filter(role="Radiologist").count()
    nurse = AddStaff.objects.filter(role="Nurse").count()
    accountant = AddStaff.objects.filter(role="Accountant").count()

    expense = total_indirect_expense+total_direct_expense

    context ={
            'opd':total_opd,
            'ipd':total_ipd,
            'path':total_path,
            'blood':total_blood,
            'ambulance':total_ambu,
            'income':income,
            'med':total_med,
            'acc':accountant,
            'doctor':doctor,
            'nurse':nurse,
            'radiologist':radiologist,
            'pathalogist':pathologist,
            'radio':total_radio,
            'expense':expense,

        }
     
    return render(request,'panels/doctor.html',context)


def radiologist(request):
    total_radio = Radiology.objects.all().aggregate(
        total_balance=Sum(F('net_amount'))
        )['total_balance'] or 0
    context = {
        'radio':total_radio,
    }

    return render(request,'panels/radiologist.html',context)
def search_staff(request):
    if 'q' in request.GET:
        query = request.GET['q']
        results = AddStaff.objects.filter(role__icontains=query)
    else:
        results = "No result Found"
    role = Role.objects.all()
    context = {
        'role':role,
        'results': results,
    }
    return render(request, 'hr/payroll.html', context)




def add_bed(request):
    
    if request.method == 'POST':
        name =  request.POST.get('name')
        floor =  request.POST.get('floor')
        purpose =  request.POST.get('purpose')
        mark_as_unused = request.POST.get('mark_as_unused')
        print(purpose)
        
        bed = Bed(
          
            name=name,
            floor=floor,
            purpose=purpose,
            mark_as_unused = mark_as_unused == 'on'
            
            # Add other fields here
        )

        bed.save()
        beds = Bed.objects.all()
        beds = BedGroup.objects.all()
        bed_pur = Bedtype.objects.all()
        context = {
           "bed": beds,
            "bed_grp": beds,
            'bed_pur':bed_pur,
        }
        return render(request,'ipd/add_bed.html',context)  # Redirect to bed details page
    beds = Bed.objects.all()
    beds = BedGroup.objects.all()
    bed_pur = Bedtype.objects.all()
    floor = Floor.objects.all()
    context = {
           "bed": beds,
            "bed_grp": beds,
            'bed_pur':bed_pur,
            'floor':floor,
        }
    return render(request, 'ipd/add_bed.html',context)



def add_bedGroup(request):
    
    if request.method == 'POST':
        name =  request.POST.get('name')
        floor =  request.POST.get('floor')
        description =  request.POST.get('purpose')

        
        bed = BedGroup(
          
            name=name,
            floor=floor,
            description=description,

            
            # Add other fields here
        )

        bed.save()
        beds = Bed.objects.all()
        beds = BedGroup.objects.all()
        bed_pur = Bedtype.objects.all()
        floor = Floor.objects.all()
        context = {
           "bed": beds,
            "bed_grp": beds,
            'bed_pur':bed_pur,
            'floor':floor,
        }
        return render(request,'ipd/add_bed.html',context)  # Redirect to bed details page
    beds = Bed.objects.all()
    beds = BedGroup.objects.all()
    bed_pur = Bedtype.objects.all()
    floor = Floor.objects.all()
    context = {
           "bed": beds,
            "bed_grp": beds,
            'bed_pur':bed_pur,
            'floor':floor,
        }
    return render( request, 'ipd/add_bed.html')


def add_purpose(request):
    
    if request.method == 'POST':
        purpose  = request.POST.get('purpose')
        

        
        bed = Bedtype(
     
            purpose=purpose,

            
            # Add other fields here
        )

        bed.save()
        beds = Bedtype.objects.all()
        beds = Bed.objects.all()
        beds = BedGroup.objects.all()
        bed_pur = Bedtype.objects.all()
        floor = Floor.objects.all()
        context = {
           "bed": beds,
            "bed_grp": beds,
            'bed_pur':bed_pur,
            'floor':floor,
        }
        
        return render(request,'ipd/add_bed.html',context)  # Redirect to bed details page
    beds = Bed.objects.all()
    beds = BedGroup.objects.all()
    bed_pur = Bedtype.objects.all()
    floor = Floor.objects.all()
    context = {
           "bed": beds,
            "bed_grp": beds,
            'bed_pur':bed_pur,
            'floor':floor,
        }
    return render(request, 'ipd/add_bed.html')

def add_floor(request):
    
    if request.method == 'POST':
        name =  request.POST.get('name')
        description =  request.POST.get('description')
        

        
        bed = Floor(
     
            name=name,
            description = description,

            
            # Add other fields here
        )

        bed.save()
        beds = Bed.objects.all()
        beds = BedGroup.objects.all()
        bed_pur = Bedtype.objects.all()
        floor = Floor.objects.all()
        context = {
           "bed": beds,
            "bed_grp": beds,
            'bed_pur':bed_pur,
            'floor':floor,
        }
        return render(request,'ipd/add_bed.html',context)  # Redirect to bed details page
    beds = Bed.objects.all()
    beds = BedGroup.objects.all()
    bed_pur = Bedtype.objects.all()
    floor = Floor.objects.all()
    context = {
           "bed": beds,
            "bed_grp": beds,
            'bed_pur':bed_pur,
            'floor':floor,
        }
    return render(request, 'ipd/add_bed.html')



def submit_symptom(request):
    if request.method == 'POST':
        symptoms_type = request.POST['symptoms_type']
        symptoms_title = request.POST['symptoms_title']
        symptoms_description = request.POST['symptoms_description']

        symptom = Symtopms(
            symptoms_type=symptoms_type,
            symptoms_title=symptoms_title,
            symptoms_description=symptoms_description,
        )
        symptom.save()

        return render(request, 'ipd/systoms.html')  

    symptom = Symtopms.objects.all()
    context ={
        'sys':symptom,
    }
    return render(request, 'ipd/systoms.html',context)


from django.shortcuts import render, redirect
from .models import Patient

def ipd_patient(request):
    if request.method == 'POST':
        height = request.POST['height']
        patient_name = request.POST['patient']
        weight = request.POST['weight']
        bp = request.POST.get('bp')
        pulse = request.POST['pulse']
        temperature = request.POST['temperature']
        respiration = request.POST['respiration']
        symptoms_type = request.POST['symptoms_type']
        symptoms_title = request.POST['symptoms_title']
        symptoms_description = request.POST['symptoms_description']
        admission_date = request.POST['admission_date']
        is_case_casualty = request.POST.get('is_case_casualty', False) == 'on'
        is_old_patient = request.POST.get('is_old_patient', False) == 'on'
        is_tpa = request.POST.get('is_tpa', False) == 'on'
        credit_limit = request.POST['credit_limit']
        reference = request.POST['reference']
        consultant_doctor = request.POST['consultant_doctor']
        bed_group = request.POST['bed_group']
        bed_number = request.POST['bed_number']
        try:
            patient = Patient.objects.get(id=patient_name)
            pat = Patient.name
        except Patient.DoesNotExist:
            # Handle the case where the patient does not exist
            return render(request, 'myapp/radiology_form.html', {'error_message': 'Patient not found'})
        


        ipd = IpdPatient(
            patient = patient,
            height=float(height),
            weight=float(weight),
            bp=float(bp),
            pulse=float(pulse),
            temperature=float(temperature),
            symptoms_description=symptoms_description,
            symptoms_title=symptoms_title,
            respiration=float(respiration),
            symptoms_type=symptoms_type,
            admission_date=admission_date,
            is_case_casualty=is_case_casualty,
            is_old_patient=is_old_patient,
            is_tpa=is_tpa,
            credit_limit=credit_limit,
            reference=reference,
            consultant_doctor=consultant_doctor,
            bed_group=bed_group,
            bed_number=bed_number,
        )
        ipd.save()
      
        
        return redirect('ipd_patient')
         # Redirect to a success page
    type = Symtopms.objects.all()
    bedtype = BedGroup.objects.all()
    bed = Bed.objects.all()
    patient =  Patient.objects.all()
    doctors = AddStaff.objects.filter(role="Doctor")
    ipd = IpdPatient.objects.all()
    context = {
        "type": type,
        "doctor":doctors,
        'bedtype':bedtype,
        'bed':bed,
        'ipd':ipd,  
        "patient":patient,
    }
    return render(request, 'ipd/ipd.html',context)



def ipd_dash(request):
    type = IpdPatient.objects.all()
    
    bedtype = BedGroup.objects.all()
    bed = Bed.objects.all()


    
    context = {
        "type": type,

        'bedtype':bedtype,
        'bed':bed,
    }
    return render(request,"ipd/dashboard.html",context)





from .models import Medicine

def submit_medicine(request):
    if request.method == 'POST':
        name = request.POST['name']
        category = request.POST['category']
        company = request.POST['company']
        composition = request.POST['composition']
        group = request.POST['group']
        unit = request.POST['unit']
        min_level = request.POST['min_level']
        reorder_level = request.POST['reorder_level']
        tax = request.POST['tax_percentage']
        unit_packing = request.POST['unit_packing']
        vat_account = request.POST['vat_account']
        note = request.POST.get('note', '')
        medicine_photo = request.FILES.get('medicine_photo', None)

        medicine = Medicine(
            name=name,
            category=category,
            company=company,
            composition=composition,
            group=group,
            unit=unit,
            min_level=min_level,
            reorder_level=reorder_level,
            tax=tax,
            unit_packing=unit_packing,
            vat_account=vat_account,
            note=note,
            medicine_photo=medicine_photo,
        )
        medicine.save()
        med = Medicine.objects.all()
        category = Med_Category.objects.all()
        context = {
            "med":med,
            'category':category,
        }
        return render(request,'pharmacy/medicine/add_med.html',context)  # Redirect to a success page
    med = Medicine.objects.all()
    category = Med_Category.objects.all()
    composition = Medicine_Composition.objects.all()
    context = {
            "med":med,
            'category':category,
            'composition':composition,
        }
    return render(request, 'pharmacy/medicine/add_med.html',context)


def supplier_form(request):
    if request.method == 'POST':
        # Handle form submission
        supplier_name = request.POST['supplier_name']
        supplier_contact = request.POST['supplier_contact']
        contact_person_name = request.POST['contact_person_name']
        contact_person_phone = request.POST['contact_person_phone']
        drug_license_number = request.POST['drug_license_number']
        address = request.POST['address']

        # Create a new Supplier object and save it to the database
        supplier = Supplier(
            supplier_name=supplier_name,
            supplier_contact=supplier_contact,
            contact_person_name=contact_person_name,
            contact_person_phone=contact_person_phone,
            drug_license_number=drug_license_number,
            address=address
        )
        supplier.save()
        supp = Supplier.objects.all()
        context ={
            'supp':supp
        }
        # Redirect to a success page or another view
        return render(request,'pharmacy/medicine/supplier_form.html',context)
    supp = Supplier.objects.all()
    context ={
            'supp':supp
        }
    return render(request, 'pharmacy/medicine/supplier_form.html',context)


def medicationDetails_form(request):
    if request.method == 'POST':
        # Handle form submission
        category = request.POST['category']
        dose = request.POST['dose']
        interval = request.POST['interval']
        duration = request.POST['duration']

        # Create a new Medication object and save it to the database
        medication = Med_Details(category=category, dose=dose,interval = interval, duration= duration)
        medication.save()

        # Redirect to a success page or another view
        med_det = Med_Details.objects.all()
        context ={
            "med_det":med_det
        }
        return render(request,'pharmacy/medicine/med_details.html',context)
    med_cate = Med_Category.objects.all()
    type = Symtopms.objects.all()
    context ={
            "med_cat":med_cate,
            "types":type,
        }
    return render(request, 'pharmacy/medicine/med_details.html',context )

def medicineCategory(request):
    if request.method == 'POST':
        # Handle form submission
        category = request.POST['category']
        

        # Create a new Medication object and save it to the database
        medication = Med_Category(medicine_category=category)
        medication.save()

        # Redirect to a success page or another view
        med_cate = Med_Category.objects.all()
        context ={
            "med_cat":med_cate
        }
        return render(request,'pharmacy/medicine/med_cat.html',context)
    med_cate = Med_Category.objects.all()
    context ={
            "med_cat":med_cate
        }
    return render(request, 'pharmacy/medicine/med_cat.html',context )


def add_donor(request):
    if request.method == 'POST':
        name = request.POST['name']
        date_of_birth = request.POST['date_of_birth']
        blood_group = request.POST['blood_group']
        gender = request.POST['gender']
        father_name = request.POST.get('father_name', '')
        contact_no = request.POST.get('contact_no', '')
        address = request.POST.get('address', '')

        # total = (request.POST.get('total'))
        # discount_percentage = (request.POST.get('discount_percentage'))
        # discount = (request.POST.get('discount'))
        # tax = (request.POST.get('tax'))
        # net_amount = (request.POST.get('net_amount'))
        # payment_amount = (request.POST.get('payment_amount'))

        donor = Donor_det(
            name = name,
            date_of_birth = date_of_birth,
            blood_group =blood_group,
            gender = gender,
            father_name = father_name,
            contact_no=contact_no,
            address = address,

            # total = total,
            # discount_percentage = discount_percentage,
            # discount=discount,
            # tax = tax,
            # net_amount = net_amount,
            # payment_amount = payment_amount,


        )
        donor.save()
        donor = Donor_det.objects.all()
        context = {
            'donor':donor,
        }
        return render(request,'blood/donor.html',context)
        # total = float(requ    est.POST.get('total', 0))
        # discount_percentage = float(request.POST.get('discount_percentage', 0))
        # discount = float(request.POST.get('discount', 0))
        # tax = float(request.POST.get('tax', 0))
        # net_amount = float(request.POST.get('net_amount', 0))
        # payment_amount = float(request.POST.get('payment_amount', 0))
    donor = Donor_det.objects.all()
    context = {
            'donor':donor,
        }
    return render(request,'blood/donor.html',context)
        
def show(request):
    return HttpResponse('hello')


def add_blood_donation(request):
    if request.method == 'POST':
        patient = request.POST['patient']
        reference_name = request.POST['reference_name']
        issue_date = request.POST['issue_date']
        hospital_doctor = request.POST.get('hospital_doctor', '')
        technician = request.POST.get('technician', '')
        blood_group = request.POST.get('blood_group', '')
        bag = request.POST.get('bag', '')
        charge_category = request.POST.get('charge_category', '')
        charge_name = request.POST.get('charge_name', '')
        standard_charge = request.POST.get('standard_charge', 0)
        note = request.POST.get('note', '')

                
        total = (request.POST.get('total'))
        discount_percentage = (request.POST.get('discount_percentage'))
        patient = get_object_or_404(Patient, id=patient)
        tax = (request.POST.get('tax'))
    


        blood_donation = BloodDonation_component(
            patient = patient,
            reference_name=reference_name,
            issue_date=issue_date,
            hospital_doctor=hospital_doctor,
            technician=technician,
            blood_group=blood_group,
            bag=bag,
            charge_category=charge_category,
            charge_name=charge_name,
            standard_charge=standard_charge,
            note=note,
            total = total,
            discount=discount_percentage,
            tax = tax,
   

        )
        blood_donation.save()
        
        return redirect('issue_blood')
    blood = BloodDonation_component.objects.all()
    patient = Patient.objects.all()
    doctor = AddStaff.objects.filter(role="Doctor")
    charge = Charge.objects.all()
    bag = BloodDonation.objects.all()
    context = { 
        'blood' : blood,
        'patient':patient,
        'charge':charge,
        'doc':doctor,
        'bag':bag,  
    }
    return render(request, 'blood/issue_blood.html',context)



def issue_comp(request):
    if request.method == 'POST':
        category_name = request.POST.get('category_name', '')
        unit = request.POST.get('unit', '')
        percentage = request.POST.get('percentage')

        product =Tax_cat(tax_category=category_name, unit=unit,percentage=percentage)
        product.save()
        comp = Tax_cat.objects.all()
        context = {
        'comp' : comp,
        }
        return redirect('issue_comp')
    comp = Tax_cat.objects.all()
    context = {
        'comp' : comp,
        }
    return render(request, 'blood/issue_com.html',context)


def add_charge(request):
    if request.method == 'POST':
        charge_type = request.POST.get('charge_type', '')
        charge_category = request.POST.get('charge_category', '')
        unit_type = request.POST.get('unit_type', '')
        charge_name = request.POST.get('charge_name')
        tax_category = request.POST.get('tax_category', '')
        tax_percentage = request.POST.get('tax_percentage', 0)
        standard_charge = request.POST.get('standard_charge', 0)
        description = request.POST.get('description', '')

        charge = Charge(
            charge_type=charge_type,
            charge_category=charge_category,
            unit_type=unit_type,
            charge_name=charge_name,
            tax_category=tax_category,
            tax_percentage=tax_percentage,
            standard_charge=standard_charge,
            description=description
        )
        charge.save()
        charge = Charge.objects.all()

        context = {
            'charge':charge
        }

        return redirect('add_charge')  # Redirect to a list view or another page
    charge = Charge.objects.all()
    charge_type = Module_Charge.objects.all()
    category = ChargeType.objects.all()
    tax = Tax_cat.objects.all()

    context = {
            'charge':charge,
            'type':charge_type,
            'category':category,
            'tax':tax,
        }
    return render(request, 'hospital/add_charge.html',context)


def create_charge_type(request):
    if request.method == 'POST':
        charge_type = request.POST.get('charge_type')
        name = request.POST.get('name')
        description = request.POST.get('description')

        charge_type = get_object_or_404(Module_Charge,pk=charge_type)
        ChargeType.objects.create(charge_type=charge_type,name=name, description=description)
        return redirect('charge_type')
    
    charge_type = Module_Charge.objects.all()
    charge = ChargeType.objects.all()
    context = {
        'charge_type':charge_type,
        'charge':charge,
    }
    return render(request, 'hospital/charge_type.html',context)


def charge_name(request):
    if request.method == 'POST':
        # Get the selected options from the form
        charge_name = request.POST.get('charge_name')
        appointment = request.POST.get('appointment')
        opd = request.POST.get('opd',False)
        ipd = request.POST.get('ipd',False)
        pathology = request.POST.get('pathology',False)
        radiology = request.POST.get('radiology',False)
        blood_bank = request.POST.get('blood_bank',False)
        ambulance = request.POST.get('ambulance',False)

        # Create or update the ServiceType object
        service_type, created = Module_Charge.objects.get_or_create(pk=1)
        service_type.charge_name = charge_name
        service_type.appointment = appointment
        service_type.opd = opd
        service_type.ipd = ipd
        service_type.pathology = pathology
        service_type.radiology = radiology
        service_type.blood_bank = blood_bank
        service_type.ambulance = ambulance
        service_type.save()
        return redirect('charge_name')

    # Retrieve the current selected options
    service_type = Module_Charge.objects.first()
    charge = Module_Charge.objects.all()
    context = { 
        'service_type':service_type,
        'charge':charge,
    }
    return render(request, 'hospital/charge_name.html', context)


def tax_category(request):
    if request.method == 'POST':
        tax_category = request.POST.get('tax_category')
        unit = request.POST.get('unit')
        percentage = request.POST.get('percentage')
        # Create a new instance of YourModel
        tax = Tax_cat(
            tax_category=tax_category,
            unit=unit,
            percentage= percentage,
        )
        tax.save()  # Save the object to the database

        return redirect('tax_cat')
    tax = Tax_cat.objects.all()
    context = {
        'tax':tax
    }
    return render(request, 'hospital/tax_cat.html',context)    



# pathology

def path_test(request):
    if request.method == 'POST':
        test_name = request.POST.get('test_name')
        short_name = request.POST.get('short_name')
        test_type = request.POST.get('test_type')
        category_name = request.POST.get('category_name')
        sub_category = request.POST.get('sub_category')
        method = request.POST.get('method')
        report_days = request.POST.get('report_days')
        charge_category = request.POST.get('charge_category')
        charge_name = request.POST.get('charge_name')
        tax_percentage = Decimal(request.POST.get('tax_percentage',0))
        standard_charge = Decimal(request.POST.get('standard_charge',0))
        amount = Decimal(request.POST.get('amount',0))
        test_parameter_name = request.POST.get('test_parameter_name')
        reference_range = request.POST.get('reference_range')
        unit = request.POST.get('unit')

        test = Pathology_test(
            test_name=test_name,
            short_name=short_name,
            test_type=test_type,
            category_name=category_name,
            sub_category=sub_category,
            method=method,
            report_days=report_days,
            charge_category=charge_category,
            charge_name=charge_name,
            tax_percentage=tax_percentage,
            standard_charge=standard_charge,
            amount=amount,
            test_parameter_name=test_parameter_name,
            reference_range=reference_range,
            unit=unit,
        )
        test.save()
        return redirect('path_test')    
    test = Pathology_test.objects.all()
    doc =  AddStaff.objects.filter(role='Doctor')
    charge = Charge.objects.all()
    category = Path_Category.objects.all()
    parameter = Path_Parameter.objects.all()
    context = {
        'test':test,
        "doc":doc,
        'charge':charge,
        'category':category,    
        'parameter':parameter,
    }
    return render(request, 'pathalogy/path_test.html',context)

def Pathology_Index(request):
    if request.method == 'POST':
        patient= request.POST['patient']
        test_name = request.POST['test_name']
        report_days = int(request.POST['report_days'])
        report_date = request.POST['report_date']
        tax_percentage = Decimal(request.POST['tax_percentage'])
        amount = Decimal(request.POST['amount'])
        referral_doctor = request.POST['referral_doctor']

        total = (request.POST.get('total',0))
        discount_percentage = (request.POST.get('discount_percentage'))
        discount = (request.POST.get('discount'))
        tax = (request.POST.get('tax',0))
        net_amount = (request.POST.get('net_amount',0))
        payment_amount = (request.POST.get('payment_amount',0))

        try:
            patient = Patient.objects.get(id=patient)
        except Patient.DoesNotExist:
            # Handle the case where the patient does not exist
            return render(request, 'myapp/radiology_form.html', {'error_message': 'Patient not found'})
        
        test = Pathology_test.objects.get(id=test_name)
        pathology_test = Pathology(
            patient=patient,
            test_name=test,
            report_days=report_days,
            report_date=report_date,
            tax_percentage=tax_percentage,
            amount=amount,
            referral_doctor=referral_doctor,

            total = total,
            discount_percentage = discount_percentage,
            discount=discount,
            tax = tax,
            net_amount = net_amount,
            payment_amount = payment_amount,
        )
        pathology_test.save()
        return redirect('path')
    path = Pathology.objects.all()
    doc = AddStaff.objects.filter(role='Doctor')
    patient = Patient.objects.all()
    test = Pathology_test.objects.all()
    context = {
        'path':path,
        "doc":doc,
        'patient':patient,
        'test':test,
    }
    return render(request, 'pathalogy/pathalogy.html',context)



def ipd_pat(request):
    ipd = IpdPatient.objects.all()
    context ={
        'ipd':ipd
    }
    return render(request,'ipd/dashboard.html',context)


def process_medicine_category(request):
   
    medicine = Medicine.objects.all()
    
    return render(request, 'ipd/precaution.html',{"medicine":medicine})

def pre(request):
     if request.method == 'POST':
        category_name = request.POST.get('category_name')
        medicine_id = request.POST.get('medicine')
        dosage = request.POST.get('dosage')
        dose_interval = request.POST.get('dose_interval')
        dose_duration = request.POST.get('dose_duration')
        instruction = request.POST.get('instruction')

        
        medicine_category = MedicineCategory(
            category_name=category_name,
            medicine_id=medicine_id,
            dosage=dosage,
            dose_interval=dose_interval,
            dose_duration=dose_duration,
            instruction=instruction
        )
        medicine_category.save()

        
        return redirect('ipd_dat')
     

#  FINCANCE SECTION 

def create_income(request):
    if request.method == 'POST':
        demo = request.POST['demo']
        name = request.POST['name']
        invoice_number = request.POST['invoice_number']
        date = request.POST['date']
        amount = request.POST['amount']
        document = request.FILES.get('document')
        description = request.POST['description']

        income = Income(
            demo=demo,
            name=name,
            invoice_number=invoice_number,
            date=date,
            amount=amount,
            document=document,
            description=description
        )
        income.save()

        return redirect('add_income')
    income = Income.objects.all()
    income_head = IncomeHead.objects.all()
    context = {
        'income':income,
        'income_head':income_head,
    }
    return render(request, 'finance/income.html',context)


def create_expense(request):
    if request.method == 'POST':
        expense = request.POST['expense']
        name = request.POST['name']
        invoice_number = request.POST['invoice_number']
        date = request.POST['date']
        amount = request.POST['amount']
        document = request.FILES.get('document')
        description = request.POST['description']

        expense = Expense(
            expense=expense,
            name=name,
            invoice_number=invoice_number,
            date=date,
            amount=amount,
            document=document,
            description=description
        )
        expense.save()

        return redirect('add_expense')
    expense = Expense.objects.all()
    expense_head = ExpenseHead.objects.all()
    context = {
        'expense':expense,
        'expense_head':expense_head,
    }
    return render(request, 'finance/expense.html',context)


def income_head(request):
    if request.method == "POST":
        income_head = request.POST['income_head']
        description = request.POST.get('description')

        # Create a new IncomeHead object
        income_head = IncomeHead(
            income_head=income_head,
            description=description,
        )
        income_head.save()

        return redirect('income_head')
    income_head = IncomeHead.objects.all()
    context ={
        "income_head":income_head,
    }
    return render(request, 'finance/finance.html',context)


def expense_head(request):
    if request.method == "POST":
        expense_head = request.POST['expense_head']
        description = request.POST.get('description')

        # Create a new Expense\Head object
        expense_head = ExpenseHead(
            expense_head=expense_head,
            description=description,
        )
        expense_head.save()

        return redirect('expense_head')
    expense_head = ExpenseHead.objects.all()
    context ={
        "expense_head":expense_head,
    }
    return render(request, 'finance/expense_head.html',context)



# TPA SECTION



def add_tpa(request):
    if request.method == 'POST':
    
        name = request.POST.get('name')
        code = request.POST.get('code')
        contact_no = request.POST.get('contact_no')
        address = request.POST.get('address')
        contact_person_name = request.POST.get('contact_person_name')
        contact_person_phone = request.POST.get('contact_person_phone')
        
        tpa = TPA(
            name=name,
            code=code,
            contact_no=contact_no,
            address=address,
            contact_person_name=contact_person_name,
            contact_person_phone=contact_person_phone,
        )
        tpa.save()

        return redirect('add_tpa')
    
    tpa_main = TPA.objects.all()
    context ={
        'tpa':tpa_main,
    }
    return render(request, 'tpa/tpa.html',context)



def create_child(request):
    if request.method == 'POST':
        # Handle the form submission
        child_name = request.POST.get('child_name')
        gender = request.POST.get('gender')
        weight = request.POST.get('weight')
        birth_date = request.POST.get('birth_date')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        case_id = request.POST.get('case_id')
        mother_name = request.POST.get('mother_name')
        father_name = request.POST.get('father_name')
        report = request.POST.get('report')
        
        # Handle file uploads
        child_photo = request.FILES.get('child_photo')
        mother_photo = request.FILES.get('mother_photo')
        father_photo = request.FILES.get('father_photo')
        document_photo = request.FILES.get('document_photo')
        
        child = ChildBirth(
            child_name=child_name,
            gender=gender,
            weight=Decimal(weight),
            child_photo=child_photo,
            birth_date=birth_date,
            phone=phone,
            address=address,
            case_id=case_id,
            mother_name=mother_name,
            mother_photo=mother_photo,
            father_name=father_name,
            father_photo=father_photo,
            report=report,
            document_photo=document_photo
        )
        child.save()
        return redirect('add_child')
    child = ChildBirth.objects.all()
    context ={
        'child':child,
    }
    return render(request, 'birth/create_child.html',context)


def fetch_case_details(request):
    case_id = request.GET.get('case_id')
    try:
        death_record = DeathRecord.objects.get(case_id=case_id)
        data = {
            'success': True,
            'patient_name': death_record.patient_name,
            'guardian_name': death_record.guardian_name,
        }
    except DeathRecord.DoesNotExist:
        data = {
            'success': False,
            'message': 'Details not found for the given Case ID.',
        }
    return JsonResponse(data)



def create_death_record(request):
    if request.method == 'POST':
        # Handle the form submission
        case_id = request.POST.get('case_id')
        patient_name = request.POST.get('patient_name')
        death_date = request.POST.get('death_date')
        guardian_name = request.POST.get('guardian_name')
        report = request.POST.get('report')

        patient = Patient.objects.get(id=patient_name)
        
       
        attachment = request.FILES.get('attachment')
        
        death = DeathRecord(
            case_id=case_id,
            patient_name=patient,
            death_date=death_date,
            guardian_name=guardian_name,
            attachment=attachment,
            report=report
        )
        death.save()
        return redirect('add_death')
    patient = Patient.objects.all()
    death = DeathRecord.objects.all()
    context ={
        "patinet":patient,
        'death':death,

    }
    return render(request, 'birth/death.html',context)


# REFERRAL

def add_referral_cate(request):
    if request.method == 'POST':
        # Handle the form submission
        name = request.POST.get('name')

        
        death = ReferralCategory(
            name=name,
           
        )
        death.save()
        return redirect('add_referral_cate')
    category = ReferralCategory.objects.all()
    context ={
        "category":category,
    }
    return render(request, 'referral/add_category.html',context)


def create_referralperson(request):
    if request.method == 'POST':
        # Handle form submission here
        referrer_name = request.POST.get('referrer_name')
        referrer_contact = request.POST.get('referrer_contact')
        contact_person_name = request.POST.get('contact_person_name')
        contact_person_phone = request.POST.get('contact_person_phone')
        category = request.POST.get('category')
        standard_commission = request.POST.get('standard_commission')
        address = request.POST.get('address')
        commission_opd = request.POST.get('commission_opd')
        commission_ipd = request.POST.get('commission_ipd')
        commission_pharmacy = request.POST.get('commission_pharmacy')
        commission_pathology = request.POST.get('commission_pathology')
        commission_radiology = request.POST.get('commission_radiology')
        commission_blood_bank = request.POST.get('commission_blood_bank')
        commission_ambulance = request.POST.get('commission_ambulance')

        # Create a new Referral object and save it
        referral = ReferralPerson(
            referrer_name=referrer_name,
            referrer_contact=referrer_contact,
            contact_person_name=contact_person_name,
            contact_person_phone=contact_person_phone,
            category=category,
            standard_commission=standard_commission,
            address=address,
            commission_opd=commission_opd,
            commission_ipd=commission_ipd,
            commission_pharmacy=commission_pharmacy,
            commission_pathology=commission_pathology,
            commission_radiology=commission_radiology,
            commission_blood_bank=commission_blood_bank,
            commission_ambulance=commission_ambulance
        )
        referral.save()
        return redirect('referral_person')
    r_person  = ReferralPerson.objects.all()
    commission = Referral_commission.objects.all()
    context ={
        'ref':r_person,
        'commission':commission,
    }
    return render(request, 'referral/refferal_person.html',context)



def create_referre(request):
    if request.method == 'POST':
        patient = request.POST.get('patient')
        patient_type = request.POST.get('patient_type')
        bill_no = request.POST.get('bill_no')
        bill_amount = request.POST.get('bill_amount')
        payee = request.POST.get('payee')
        commission_percentage = request.POST.get('commission_percentage')
        commission_amount = request.POST.get('commission_amount')


        patient = Patient.objects.get(id=patient)
        # Calculate commission amount based on percentage
        try:
            commission_percentage = float(commission_percentage)
            commission_amount = float(bill_amount) * (commission_percentage / 100)
        except (ValueError, TypeError):
            commission_percentage = 0
            commission_amount = 0

        # Create a new Payment object and save it
        referral = Referral(
            patient=patient,
            patient_type=patient_type,
            bill_no=bill_no,
            bill_amount=bill_amount,
            payee=payee,
            commission_percentage=commission_percentage,
            commission_amount=commission_amount
        )
        referral.save()

        return redirect('referral')  # Redirect to a success page or list view
    patient = Patient.objects.all()
    ref = Referral.objects.all()
    context ={
        'patient':patient,
        'ref':ref,
    }
    return render(request, 'referral/referral.html',context)



def create_vehicle(request):
    if request.method == 'POST':
        vehicle_number = request.POST.get('vehicle_number')
        vehicle_model = request.POST.get('vehicle_model')
        year_made = request.POST.get('year_made')
        driver_name = request.POST.get('driver_name')
        driver_license = request.POST.get('driver_license')
        driver_contact = request.POST.get('driver_contact')
        vehicle_type = request.POST.get('vehicle_type')
        note = request.POST.get('note')

        # Create a new Vehicle object and save it
        vehicle = Ambulance(
            vehicle_number=vehicle_number,
            vehicle_model=vehicle_model,
            year_made=year_made,
            driver_name=driver_name,
            driver_license=driver_license,
            driver_contact=driver_contact,
            vehicle_type=vehicle_type,
            note=note
        )
        vehicle.save()


        return redirect('add_ambulance')  # Redirect to a success page or list view
    vehicle = Ambulance.objects.all()
    context ={
        'vehicle':vehicle,
    }
    return render(request, 'ambulance/add_ambulance.html',context)


def ambulance_call(request):
    if request.method == 'POST':
        vehicle_model = request.POST['vehicle_model']
        driver_name = request.POST['driver_name']
        date = request.POST['date']
        charge_category = request.POST['charge_category']
        charge_name = request.POST['charge_name']
        standard_charge = request.POST['standard_charge']
        note = request.POST['note']
        
        total = (request.POST.get('total',0))
        tax = (request.POST.get('tax',0))
        net_amount = (request.POST.get('net_amount',0))
        payment_amount = (request.POST.get('payment_amount',0))


        amb_all = add_ambulancecall(
            vehicle_model=vehicle_model,
            driver_name=driver_name,
            date=date,
            charge_category=charge_category,
            charge_name=charge_name,
            standard_charge=standard_charge,
            note=note,
            total = total,
            tax = tax,
            net_amount = net_amount,
            payment_amount = payment_amount,
            

        )
        amb_all.save()


        return redirect('ambulance_call')  # Redirect to a page showing the list of expense records
    ambulance = add_ambulancecall.objects.all()
    vehicle = Ambulance.objects.all()
    context ={
        'call':ambulance,
        'vehicle':vehicle,
    }
    return render(request, 'ambulance/call.html',context)


def get_driver_name(request):
    if request.method == 'GET':
        selected_vehicle = request.GET.get('vehicle_model', None)
        try:
            driver = Ambulance.objects.get(vehicle_model=selected_vehicle)
            data = {
              'success': True,
            'driver_name': driver.driver_name,
            
        }
        except Ambulance.DoesNotExist:
         data = {
            'success': False,
            'message': 'Details not found for the given Case ID.',
        }
         
    return JsonResponse(data)




def add_itemcat(request):
    if request.method == 'POST':
        item_category = request.POST['item_category']
        description = request.POST['description']

        item = ItemCategory(
            item_category=item_category,
            description=description,
        )
        item.save()

        return redirect('add_itemcat')  # Redirect to a page showing the list of items
    category= ItemCategory.objects.all()
    context ={
        'category':category
    }
    return render(request,'setup/inventory/add_itemcat.html',context)



def add_store(request):
    if request.method == 'POST':
        store_name = request.POST['store_name']
        stock_code = request.POST['stock_code']
        description = request.POST['description']
        store  = Store(store_name=store_name,
                        stock_code=stock_code,
                          description=description)
        store.save()
        return redirect('add_store')
    store = Store.objects.all()
    context ={
        "store":store
    }
    return render(request, 'setup/inventory/add_store.html',context )

def add_supplierdet(request):
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        contact_person_name = request.POST['contact_person_name']
        address = request.POST['address']
        contact_person_phone = request.POST['contact_person_phone']
        contact_person_email = request.POST['contact_person_email']
        description = request.POST['description']

        supplier_det = SupplierDetails(
            name=name,
            phone=phone,
            email=email,
            contact_person_name=contact_person_name,
            address=address,
            contact_person_phone=contact_person_phone,
            contact_person_email=contact_person_email,
            description=description
        )
        supplier_det.save()
        return redirect('add_supplierdet')

    supplier = SupplierDetails.objects.all()
    context ={
        'supplier':supplier
    }
    return render(request, 'setup/inventory/add_supplier.html',context)



def     add_item(request):
    if request.method == 'POST':
        item = request.POST['item']
        item_category = request.POST['item_category']
        unit = request.POST['unit']
        description = request.POST['description']
        item = Item(
            item=item,
            item_category=item_category, 
            unit=unit, 
            description=description)
        item.save()
        return redirect('add_item')
    item= Item.objects.all()
    item_cat = ItemCategory.objects.all()
    context ={
        'item':item,
        'item_cat':item_cat,
    }
    return render(request, 'inventory/add_item.html',context)


def add_itemstock(request):
    if request.method == 'POST':
        item_category = request.POST['item_category']
        item = request.POST['item']
        supplier = request.POST['supplier']
        store = request.POST['store']
        quantity = request.POST['quantity']
        purchase_price = request.POST['purchase_price']
        date = request.POST['date']
        description = request.POST['description']
        try:
            document = request.FILES['document']
        except MultiValueDictKeyError:
            document = None  # Handle the case when 'document' is missing in FILES


        stock = ItemStock(
            item_category=item_category,
            item=item,
            supplier=supplier,
            store=store,
            quantity=quantity,
            purchase_price=purchase_price,
            date=date,
            description=description,
            document=document
        )
        stock.save()
        item = ItemStock.objects.all()
        context ={
            'item':item
        }
        return redirect('add_itemstock')
    item = Item.objects.all()
    itemstock = ItemStock.objects.all()
    item_category = ItemCategory.objects.all()
    supplier = SupplierDetails.objects.all()
    stores = Store.objects.all()
    context ={
        'item':item,
        'itemstock' :itemstock,
        'itemcat':item_category,
        'supplier':supplier,
        'stores':stores,

    }

    return render(request, 'inventory/add_itemstock.html',context)


def fetch_items_by_category(request):
    # Get the selected category from the AJAX request
    selected_category = request.GET.get('category')

    # Query the database to retrieve items based on the selected category
    
    # Create a list of items to be returned as JSON
    # items_list = [item.item for item in items]    

    # Return the items as a JSON response
    
    try:
       
        items = Item.objects.filter(item_category=selected_category)
        item_list = [{'value': item.item, 'text': item.item} for item in items]
        data = {
            'success': True,
            'items': item_list,
           
        }
    except Item.DoesNotExist:
        data = {
            'success': False,
            'message': 'Details not found for the given Case ID.',
        }
    return JsonResponse(data)
    # return JsonResponse({'items': items_list})


def path_category(request):
    if request.method == 'POST':
        name = request.POST['category_name']
        path_category = Path_Category(name=name)
        path_category.save()
        return redirect('path_category')
    category = Path_Category.objects.all()
    context ={
        'category':category
    }
    return render(request, 'setup/pathology/category.html',context)

def rado_category(request):
    if request.method == 'POST':
        name = request.POST['category_name']
        path_category = Radio_Category(name=name)
        path_category.save()
        return redirect('radio_category')
    radio = Radio_Category.objects.all()
    context = {
        'radio':radio,
    }
    return render(request, 'setup/radiology/category.html',context)




def path_parameter(request):
    if request.method == 'POST':
        parameter_name = request.POST['parameter_name']
        reference_range = request.POST['reference_range']
        unit = request.POST['unit']
        description = request.POST['description']
        para = Path_Parameter(
            parameter_name=parameter_name,
            reference_range=reference_range,
            unit=unit,
            description=description
        )
        para.save()
        return redirect('path_parameter')
    parameter = Path_Parameter.objects.all()
    context ={
        'parameter':parameter,
    }
    return render(request, 'setup/pathology/create_parameter.html',context)



def radio_parameter(request):
    if request.method == 'POST':
        parameter_name = request.POST['parameter_name']
        reference_range = request.POST['reference_range']
        unit = request.POST['unit']
        description = request.POST['description']
        para = Radio_Parameter(
            parameter_name=parameter_name,
            reference_range=reference_range,
            unit=unit,
            description=description
        )
        para.save()
        return redirect('radio_parameter')
    
    parameter = Radio_Parameter.objects.all()
    context = {
        'parameter':parameter,
    }
    return render(request, 'setup/radiology/create_parameter.html',context)


def get_parameter_details(request):
    try:
        selected =  request.GET.get('test_name')
        parameter = Path_Parameter.objects.get(parameter_name=selected)
        data = {
            'reference_range': parameter.reference_range,
            'unit': parameter.unit,
        }
        return JsonResponse(data)   
    except Path_Parameter.DoesNotExist:
        return JsonResponse({'error': 'Parameter not found'}, status=404)
    

def radiology(request):
    if request.method == 'POST':
        patient = request.POST['patient']
        test_name = request.POST['test_name']
        report_days = int(request.POST['report_days'])
        report_date = request.POST['report_date']
        tax_percentage = Decimal(request.POST['tax_percentage'])
        amount = Decimal(request.POST['amount'])
        referral_doctor = request.POST['referral_doctor']

        total = (request.POST.get('total',0))
        discount_percentage = (request.POST.get('discount_percentage',0))
        discount = (request.POST.get('discount',0))
        tax = (request.POST.get('tax',0))
        net_amount = (request.POST.get('net_amount',0))
        payment_amount = (request.POST.get('payment_amount',0))

        note =request.POST['note']
        test_name = Radiology_test.objects.get(id=test_name)
        try:
            patient = Patient.objects.get(id=patient)
        except Patient.DoesNotExist:
            # Handle the case where the patient does not exist
            return render(request, 'myapp/radiology_form.html', {'error_message': 'Patient not found'})

        pathology_test = Radiology(
            patient = patient,
            test_name=test_name,
            report_days=report_days,
            report_date=report_date,
            tax_percentage=tax_percentage,
            amount=amount,
            referral_doctor=referral_doctor,

            total = total,
            discount_percentage = discount_percentage,
            discount=discount,
            tax = tax,
            net_amount = net_amount,
            payment_amount = payment_amount,

            note = note,
        )
        pathology_test.save()
        return redirect('radiology')
    radio = Radiology.objects.all()
    doc =  AddStaff.objects.filter(role='Doctor')
    test = Radiology_test.objects.all()
    patient= Patient.objects.all()
    context = {
        'radio':radio,
        'test':test,
        "doc":doc,
        'patient':patient,
    }
    return render(request, 'radiology/radiology.html',context)



def radio_test(request):
    if request.method == 'POST':
        test_name = request.POST.get('test_name')
        short_name = request.POST.get('short_name')
        test_type = request.POST.get('test_type')
        category_name = request.POST.get('category_name')
        sub_category = request.POST.get('sub_category')
        method = request.POST.get('method')
        report_days = request.POST.get('report_days')
        charge_category = request.POST.get('charge_category')
        charge_name = request.POST.get('charge_name')
        tax_percentage = Decimal(request.POST.get('tax_percentage',0))
        standard_charge = Decimal(request.POST.get('standard_charge',0))
        amount = Decimal(request.POST.get('amount',0))
        test_parameter_name = request.POST.get('test_parameter_name')
        reference_range = request.POST.get('reference_range')
        unit = request.POST.get('unit')

        test = Radiology_test(
            test_name=test_name,
            short_name=short_name,
            test_type=test_type,
            category_name=category_name,
            sub_category=sub_category,
            method=method,
            report_days=report_days,
            charge_category=charge_category,
            charge_name=charge_name,
            tax_percentage=tax_percentage,
            standard_charge=standard_charge,
            amount=amount,
            test_parameter_name=test_parameter_name,
            reference_range=reference_range,
            unit=unit,
        )
        test.save()
        return redirect('radio_test')    
    test = Radiology.objects.all()
    doc =  AddStaff.objects.filter(role='Doctor')
    parameter = Radio_Parameter.objects.all()
 
    charge = Charge.objects.all()
    category = Radio_Category.objects.all()
    radio_test = Radiology_test.objects.all()
    parameter = Radio_Parameter.objects.all()
    context = {
        'test':test,
        "doc":doc,
        'charge':charge,
        'category':category,    
        'parameter':parameter,
        'radio':radio_test,
    }
    return render(request, 'radiology/radio_test.html',context)


def get_tax_info(request):

    try:
        selected =  request.GET.get('test_name')
        parameter = Pathology_test.objects.get(id=selected)
        data = {
            'tax': parameter.tax_percentage,
            'standard_charge': parameter.standard_charge,
            'report_days': parameter.report_days,
        }
        return JsonResponse(data)   
    except Path_Parameter.DoesNotExist:
        return JsonResponse({'error': 'Parameter not found'}, status=404)




def opd(request):
    if request.method == 'POST':
        height = request.POST['height']
        patient_name = request.POST['patient']
        weight = request.POST['weight']
        bp = request.POST['bp']
        pulse = request.POST['pulse']
        temperature = request.POST['temperature']
        respiration = request.POST['respiration']
        symptoms_type = request.POST['symptoms_type']
        symptoms_title = request.POST['symptoms_title']
        symptoms_description = request.POST['symptoms_description']
        admission_date = request.POST['admission_date']
        is_case_casualty = request.POST.get('is_case_casualty', False) == 'on'
        is_old_patient = request.POST.get('is_old_patient', False) == 'on'
        is_tpa = request.POST.get('is_tpa', False) == 'on'
        credit_limit = request.POST['credit_limit']
        reference = request.POST['reference']
        consultant_doctor = request.POST['consultant_doctor']
        note = request.POST.get('note')
        any_known = request.POST['any_known']
        charge_category = request.POST.get('charge_category')
        charge_name = request.POST.get('charge_name')
        tax_percentage = Decimal(request.POST.get('tax_percentage',0))
        standard_charge = Decimal(request.POST.get('standard_charge',0))
        amount = Decimal(request.POST.get('amount',0))
        paid_amount = Decimal(request.POST.get('paid_amount',0))
        applied_charges = request.POST.get('applied_charges')


        try:
            patient = Patient.objects.get(id=patient_name)
            pat = Patient.name
        except Patient.DoesNotExist:
            # Handle the case where the patient does not exist
            return render(request, 'opd/opd.html', {'error_message': 'Patient not found'})
        


        opd = OpdPatient(
            patient = patient,
            height=height,
            weight=weight,
            bp=bp,
            pulse=pulse,
            temperature=temperature,
            symptoms_description=symptoms_description,
            symptoms_title=symptoms_title,
            respiration=respiration,
            symptoms_type=symptoms_type,
            admission_date=admission_date,
            is_case_casualty=is_case_casualty,
            is_old_patient=is_old_patient,
            is_tpa=is_tpa,
            credit_limit=credit_limit,
            reference=reference,
            consultant_doctor=consultant_doctor,
            charge_category=charge_category,
            charge_name=charge_name,
            tax_percentage=tax_percentage,
            standard_charge=standard_charge,
            amount=amount,
            paid_amount= paid_amount,
            note = note,
            Applied_charges = applied_charges,
            any_known = any_known
            
        )
        opd.save()
        return redirect('opd')
    type = Symtopms.objects.all()
    
    patient =  Patient.objects.all()
    doctors = AddStaff.objects.filter(role="Doctor")
    opd = OpdPatient.objects.all()
    charge = Charge.objects.all()
    category = Path_Category.objects.all()
    context = {
        "type": type,
        "doctor":doctors,
        'opd':opd,  
        'charge':charge,
        'category':category,
        "patient":patient,
    }
    return render(request, 'opd/opd.html',context)



def get_tax(request):

    # try:
    #     selected =  request.GET.get('charge_name')
    # if selected is not None:
    #         decoded =  unquote(selected)
    #         charge = Charge.objects.get(charge_name=decoded)
    #         data = {
    #             'tax': charge.tax_percentage,
    #              'standard_charge': charge.standard_charge,
    #               }
        
    #         return JsonResponse(data)   
    # else:
    # except Charge.DoesNotExist:
    #     return JsonResponse({'error': 'Parameter not found'}, status=404)
    try:
        selected = request.GET.get('test_name')
        if selected is not None:
            decoded = unquote(selected)
            try:
                charge = Charge.objects.get(charge_name=decoded)
                data = {
                    'tax': charge.tax_percentage,
                    'standard_charge': charge.standard_charge,
                }
                return JsonResponse(data)
            except ObjectDoesNotExist:
                return JsonResponse({'error': 'Charge not found'}, status=404)
        else:
            return JsonResponse({'error': 'Parameter not found'}, status=400)
    except Exception as e:
        # Handle any other exceptions that might occur
        return JsonResponse({'error': str(e)}, status=500)


def purchase_med(request):
    if request.method == 'POST':
        # Retrieve form data from POST request
        category = request.POST.get('category')
        name = request.POST.get('name')
        batch_no = request.POST.get('batch_no')
        expiry_date = request.POST.get('expiry_date')
        mrp = request.POST.get('mrp')
        batch_amount = request.POST.get('batch_amount')
        sale_price = request.POST.get('sale_price')
        tax_percentage = request.POST.get('tax_percentage')
        packing_qty = request.POST.get('packing_qty')
        composition = request.POST.get('composition')
        quantity = request.POST.get('quantity')
        purchase_price = request.POST.get('purchase_price')
        tax = request.POST.get('tax')
        note = request.POST.get('note')
        attach_documents = request.POST.get('document')
        amount = request.POST.get('amount')

        total = (request.POST.get('total',0))
        discount_percentage = (request.POST.get('discount_percentage',0))
        discount = (request.POST.get('discount',0))
        tax = (request.POST.get('tax',0))
        net_amount = (request.POST.get('net_amount',0))
        payment_amount = (request.POST.get('payment_amount',0))
        payment_mode = request.POST.get('payment_mode')


        composition = Medicine_Composition.objects.get(id=composition)
        category = Med_Category.objects.get(id=category)
        medicine = Purchase(
            category=category,
            name=name,
            payment_mode = payment_mode,
            note=note,
            documents= attach_documents,
            batch_no=batch_no,
            expiry_date=expiry_date,
            mrp=mrp,
            batch_amount=batch_amount,
            sale_price=sale_price,
            composition = composition,
            packing_qty=packing_qty,
            quantity=quantity,
            purchase_price=purchase_price,
            tax=tax,
            tax_percentage = tax_percentage,    

            total = total,
            discount_percentage = discount_percentage,
            discount=discount,
            
            net_amount = net_amount,
            payment_amount = payment_amount,
            amount=amount,
            
        )
        medicine.save()
        return redirect('purchase_med')
    
    medicine  =  Medicine.objects.all()
    medicineCat = Med_Category.objects.all()
    med = Purchase.objects.all()
    composition = Medicine_Composition.objects.all()
    context ={
        'medicine':medicine,
        "cat":medicineCat,
        'med':med,
        'composition':composition,
    }
    return render(request, 'pharmacy/medicine/purchase.html',context)



def add_nursing_record(request,id):
    if request.method == 'POST':
        # Retrieve form data from POST request
        patient = id
        date = request.POST.get('date')
        nurse = request.POST.get('nurse')
        note = request.POST.get('note')
        comment = request.POST.get('comment')
        ipd_details = get_object_or_404(IpdPatient,id=patient)
        patient = get_object_or_404(Patient, id=ipd_details.patient.id)
       
        nursing_record = NursingRecord(
            date=date,
            patient = patient,
            nurse=nurse,
            note=note,
            comment=comment
        )
        nursing_record.save()
        url = reverse('ipd_dashboard', args=[id])
        url+= "#nurse"
        return redirect(url)
    
    context ={
        'nurse':nurse,
        'staff':staff
    }
    return render(request, 'ipddashboard/nurse.html',context)


def add_doctor_record(request,id):
    if request.method == 'POST':
        # Retrieve form data from POST request
        patient = id
        date = request.POST.get('date')
        doctor = request.POST.get('doctor')
        note = request.POST.get('note')
        comment = request.POST.get('comment') 
        
        ipd_details = get_object_or_404(IpdPatient,id=patient)
        patient = get_object_or_404(Patient, id=ipd_details.patient.id)
        nursing_record = DoctorNote(
            date=date,
            patient = patient,
            doctor=doctor,
            note=note,
            comment=comment
        )
        nursing_record.save()
        url = reverse('ipd_dashboard', args=[id])
        url+= "#doctor"
        return redirect(url)
    
   


def ipd_dashboard(request,ipd_id):
    ipd = IpdPatient.objects.filter(patient=ipd_id)
    nurse= NursingRecord.objects.all()
    staff = AddStaff.objects.filter(role="Nurse")
    doctor  = AddStaff.objects.filter(role="Doctor")
    medicine = MedicationDoseage.objects.all()
    consultant = Consultant_register.objects.all()
    operation = Operation.objects.all()

    dosage = Med_Details.objects.all()
    cat = Med_Category.objects.all()
    medicine_name = Medicine.objects.all()
    operation_cate = Operation_category.objects.all()
    operation_name = Operation_name.objects.all()
    prep = Precreption.objects.all()
    doc_note = DoctorNote.objects.all()

    context= {
        
    }
    payment = Ipd_Payments.objects.all()

    
    try:
        radiology_amount = Radiology.objects.get(patient=ipd_id).amount
        
    except Radiology.DoesNotExist:
        radiology_amount = 0
     

    context ={
        'nurse':nurse,
        'prep':prep,
        'doc_note':doc_note,
        'staff':staff,
        'ipd':ipd,
        'doctor':doctor,
        'medicine':medicine,
        'operation_category':operation_cate,
        'operation_name':operation_name,
        'dosage':dosage,
        'cat':cat,
        'operation':operation,
        'medicine_name':medicine_name,
        'consultant':consultant,
        
        'payment':payment,
        'radio':radiology_amount,
    }
    return render(request,'ipd/pat_dash.html',context)



def add_medication_record(request,id):
    if request.method == 'POST':
        # Retrieve form data from POST request
        date = request.POST.get('date')
        time = request.POST.get('time')
        category = request.POST.get('category')
        medicine_name = request.POST.get('medicine_name')
        dosage = request.POST.get('dosage')
        remarks = request.POST.get('remarks')

        ipd_details = get_object_or_404(IpdPatient,id=id)
        patient = get_object_or_404(Patient,id=ipd_details.patient.id)
        medication_record = MedicationDose(
            patient=patient,
            date=date,
            time=time,
            category=category,
            medicine_name=medicine_name,
            dosage=dosage,
            remarks=remarks
        )
        medication_record.save()

        url = reverse('ipd_dashboard', args=[id])
        url+= "#nurse"
        return redirect(url)
    
    context ={
        
        'staff':staff
    }
    return render(request, 'ipddashboard/nurse.html',context)

    




def blood_donation_form(request):
    if request.method == 'POST':
        donor_name = request.POST['donor_name']
        donate_date = request.POST['donate_date']
        bag = request.POST['bag']
        volume = request.POST['volume']
        unit_type = request.POST['unit_type']
        lot = request.POST['lot']
        charge_category = request.POST['charge_category']
        charge_name = request.POST['charge_name']
        standard_charge = request.POST['standard_charge']
        institution = request.POST['institution']
        note = request.POST['note']
        total = (request.POST.get('total',0))
        discount_percentage = (request.POST.get('discount_percentage',0))
        discount = (request.POST.get('discount',0))
        tax = (request.POST.get('tax',0))
        net_amount = (request.POST.get('net_amount',0))
        payment_amount = (request.POST.get('payment_amount',0))


        donor = Donor_det.objects.get(id =donor_name)
        blood_donation = BloodDonation(
            donor_name=donor,
            donate_date=donate_date,
            bag=bag,
            volume=volume,
            unit_type=unit_type,
            lot=lot,
            charge_category=charge_category,
            charge_name=charge_name,
            standard_charge=standard_charge,
            institution=institution,
            note=note,
            total = total,
            discount_percentage = discount_percentage,
            discount=discount,
            tax = tax,
            net_amount = net_amount,
            payment_amount = payment_amount,
        )
        blood_donation.save()
        bag_available_instance = Bag_available.objects.first()  # Assuming there is only one instance
        bag_available_instance.qty += 1
        bag_available_instance.save()
        return redirect('blood_donation')
    donor = Donor_det.objects.all()
    unit = Tax_cat.objects.all()
    blood = BloodDonation.objects.all()
    context ={
        'donor':donor,
        'unit':unit,
        'blood':blood,
    }
    return render(request, 'blood/blood_donation.html',context)




def get_related_categories(request):
  
    selected_charge_type = request.GET.get('charge_type')
        # Implement logic to retrieve related categories based on the selected_charge_type.
        # Replace the following line with your logic.
    
    try:
        selected_charge_type = request.GET.get('charge_type')   
        if selected_charge_type is not None:
            decoded = unquote(selected_charge_type)
            try:
                charge_category = ChargeType.objects.filter(charge_type=decoded)
                charge = [category.name for category in charge_category]
                data = {
                    'name':charge,  
                    # 'name':charge.name,
                    # 'type': charge.charge_type,
                }
                return JsonResponse(data)
            except ObjectDoesNotExist:
                return JsonResponse({'error': 'Charge not found'}, status=404)
        else:
            return JsonResponse({'error': 'Parameter not found'}, status=400)
    except Exception as e:
        # Handle any other exceptions that might occur
        return JsonResponse({'error': str(e)}, status=500)
    

def get_tax_percentage(request):
    selected_tax_category = request.GET.get('tax_category')

    try:
        tax_data = Tax_cat.objects.get(id=selected_tax_category)
        tax_percentage = tax_data.percentage  # Replace 'tax_percentage' with the actual field name
        print(tax_percentage)
        return JsonResponse({'tax_percentage': tax_percentage})
    except ObjectDoesNotExist:
        return JsonResponse({'error': 'Tax category not found'}, status=404)




def commission_form(request):
    if request.method == 'POST':
        # Handle form submission here
        category = request.POST.get('category')

        standard_commission = request.POST.get('standard_commission')
        commission_opd = request.POST.get('commission_opd')
        commission_ipd = request.POST.get('commission_ipd')
        commission_pharmacy = request.POST.get('commission_pharmacy')
        commission_pathology = request.POST.get('commission_pathology')
        commission_radiology = request.POST.get('commission_radiology')
        commission_blood_bank = request.POST.get('commission_blood_bank')
        commission_ambulance = request.POST.get('commission_ambulance')
        

        # Create a new CategoryCommission object and save it to the database
        Referral_commission.objects.create(
            category=category,
        
            standard_commission=standard_commission,
            commission_opd=commission_opd,
            commission_ipd=commission_ipd,
            commission_pharmacy=commission_pharmacy,
            commission_pathology=commission_pathology,
            commission_radiology=commission_radiology,
            commission_blood_bank=commission_blood_bank,
            commission_ambulance=commission_ambulance

        )

        # Optionally, you can redirect to a success page or another view
        return redirect('referral_commission')

    
        # Render the form template for GET requests

    commission = Referral_commission.objects.all()
    category = ReferralCategory.objects.all()
    context ={
        'commission':commission,
        'category':category,
    }
    return render(request, 'referral/commission.html',context )



def add_task(request):
    if request.method == 'POST':
        # Get the data from the POST request
        title = request.POST['title']
        date = request.POST['date']
        
        # Create a new MyEvent instance and save it to the database
        Task.objects.create(title=title, date=date)
        
        return redirect('add_task')  # Redirect to a page displaying a list of events or wherever you want
    task = Task.objects.all()
    context ={
        'task':task,    
    }
    return render(request, 'admin/task.html',context)

def get_selected_role_data(request):
    if request.method == 'POST':
        selected_role = request.POST.get('role')

        # You can query the database to retrieve staff members with the selected role
        staff_members = AddStaff.objects.filter(role=selected_role)
        

        # Convert the staff members data to a list of dictionaries (JSON)
        staff_data = [{'id': staff.staff_id, 'name': staff.first_name,'role':staff.role} for staff in staff_members]

        return JsonResponse({'staff_data': staff_data})

    return JsonResponse({'error': 'Invalid request'}, status=400)


def payroll(request):
    role = Role.objects.all()
    context = {
        'role':role
    }
    return render(request,'hr/payroll.html',context)


def payroll_id(request,id):

    
   
    staff_id = AddStaff.objects.get(staff_id=id)
    print(staff_id)
    
    if request.method == 'POST':
       
        earning = float(request.POST.get('earning', 0.0))
        deduction = float(request.POST.get('deduction', 0.0))
        tax_percentage = float(request.POST.get('tax_percentage', 0.0))

        # Calculate gross salary, tax, and net salary
        gross_salary = earning - deduction
        float(gross_salary)
        tax = (tax_percentage / 100) * gross_salary
        float(tax)

        net_salary = gross_salary - tax
        float(net_salary)

        # Update or create the salary information for the staff member
        salary, created = Payroll.objects.get_or_create(staff=staff_id)
        salary.earning = earning
        salary.deduction = deduction
        salary.gross_salary = gross_salary
        salary.tax_percentage = tax_percentage
        salary.tax = tax
        salary.net_salary = net_salary
        salary.save()

        return redirect('payroll')  # Redirect to a list of staff salaries or wherever you prefer
    staff = AddStaff.objects.get(staff_id=id)
    context = {
        'staff':staff,  
    }
    
    return render(request,'hr/payroll_id.html',context)




def create_meeting(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        meeting_date = request.POST.get('meeting_date')
        duration_minutes = request.POST.get('duration_minutes')
        host_video = request.POST.get('host_video')
        client_video = request.POST.get('client_video')
        description = request.POST.get('description')
        staff_list = request.POST.get('staff_list')

        # Create a new ZoomMeeting object
        meeting = Zoom(
            title=title,
            meeting_date=meeting_date,
            duration_minutes=duration_minutes,
            host_video=host_video,
            client_video=client_video,
            description=description,
            staff_list=staff_list,
        )
        meeting.save()

        return redirect('meeting')  # Redirect to a list of meetings or wherever you prefer
    meet = Zoom.objects.all()
    context = {
        'meet':meet
    }
    return render(request, 'meeting/zoom.html',context)





def party_create(request):
    if request.method == 'POST':
        # Retrieve data from the form and create a new account record
        part_name = request.POST['part_name']
        gstin = request.POST['gstin']
        phone_number = request.POST['phone_number']
        account = request.POST['account']
        gst_type = request.POST['gst_type']
        state = request.POST['state']
        email_id = request.POST['email_id']
        billing_address = request.POST['billing_address']
        opening_balance = request.POST['opening_balance']
        as_of_date = request.POST['as_of_date']
        to_pay = request.POST.get('to_pay', False)
        to_receive = request.POST.get('to_receive', False)

        account = Party(
            part_name=part_name,
            gstin=gstin,
            phone_number=phone_number,
            gst_type=gst_type,
            state=state,
            account_no=int(account),
            email_id=email_id,
            billing_address=billing_address,
            opening_balance=opening_balance,
            as_of_date=as_of_date,
            to_pay=to_pay,
            to_receive=to_receive
        )
        account.save()
        return redirect('party')
        # You can add a success message here if needed
    party = Party.objects.all()
    context ={
        'party':party
    }
    return render(request, 'accounts/party.html',context)




def add_category(request):
    if request.method == 'POST':
        category = request.POST['category']
        Category.objects.create(category=category)
        return redirect('add_   category')  # Redirect to a list view or any other page
    cate = Category.objects.all()
    context ={
        'cate':cate
    }
    return render(request, 'accounts/category.html',context)



def manage_items(request):
    if request.method == 'POST':
        # Retrieve data from the form and create a new item
        item_name = request.POST['item_name']
        
        category = request.POST['category']
        
        sale_price = request.POST['sale_price']
        disc_on_sale_price = request.POST['disc_on_sale_price']
        
        purchase_price = request.POST['purchase_price']
        tax_rate = request.POST['tax_rate']
        opening_quantity = request.POST['opening_quantity']
        at_price = request.POST['at_price']
        unit=request.POST['unit']
        as_of_date = request.POST['as_of_date']
        min_stock_to_maintain = request.POST['min_stock_to_maintain']
        location = request.POST['location']


        
       

        item = Item_Acc(
            item_name=item_name,
            unit=unit,
            category=category,
            
            sale_price=sale_price,
            disc_on_sale_price=disc_on_sale_price,
            
            purchase_price=purchase_price,
            tax_rate=tax_rate,      
            opening_quantity=opening_quantity,
            at_price=at_price,
            as_of_date=as_of_date,
            min_stock_to_maintain=min_stock_to_maintain, 
            location=location
        )
        item.save()
        return redirect('item_acc')
    Medicien = Med_Category.objects.all()
    item_cat = ItemCategory.objects.all()
    cat = Category.objects.all()
    unit = Unit.objects.all()
    item = Item_Acc.objects.all()

    context ={
        'medicine':Medicien,
        'item_cat':item_cat,
        'cat':cat,
        'unit':unit,
        'item':item
    }

    return render(request, 'accounts/item.html',context)


def unit(request):
    if request.method == 'POST':
        # Retrieve data from the form and create a new unit
        unit_name = request.POST['unit_name']

        unit = Unit(unit_name=unit_name)
        unit.save()
        return redirect('unit')
    unit = Unit.objects.all()
    context={
        'unit':unit
    }
    return render(request, 'setup/inventory/unit.html',context)




def sales_invoice(request):
    if request.method == 'POST':
        # Retrieve data from the form
        name = request.POST.get('name')
        phone_number = request.POST.get('phone_number')
        invoice_number = request.POST.get('invoice_number')
        invoice_date = request.POST.get('invoice_date')
        state_of_supply = request.POST.get('state_of_supply')
        item_counter = request.POST.get('item_counter', 0)
        names = re.sub(r'\d', '',name)
        name  = names.replace("_", "")
        print(item_counter)
        if item_counter.isdigit():
            item_counter = int(item_counter)
        else:
            item_counter = 0  # Set a default value if 'item_counter' is not a valid integer
        

        # Create a new Invoice object
        invoice = Sales_Invoice(
            name=name,
            phone_number=phone_number,
            invoice_number=invoice_number,
            invoice_date=invoice_date,
            state_of_supply=state_of_supply,
            type="sales",
           
        )
        
        # Save the invoice object to the database
        invoice.save()
        id = Sales_Invoice.objects.get(id=invoice.id)
        total_all_products =0

        for i in range(1, item_counter + 1):
            
            
            item = request.POST.get(f'item_{i}')
            qty = request.POST.get(f'qty_{i}')
            items = re.sub(r'\d', '',item)

            item  = items.replace("_", "")
            unit = request.POST.get(f'unit_{i}')
            price = request.POST.get(f'price_{i}')
            discount_percentage = request.POST.get(f'discount_{i}')
            discount_amount = request.POST.get(f'discount_amount_{i}')
            tax_percentage = request.POST.get(f'tax_{i}')
            tax_amount = request.POST.get(f'tax_amount_{i}')
            total = request.POST.get(f'total_{i}')
            
            print(item)
            
            print(qty)
            
            item = Item_Invoice(
            
                invoice=id,
                item=item,
                qty=qty,
                unit=unit,
                price=price,
                discount=discount_percentage,
                discount_amount=discount_amount,
                tax=tax_percentage,
                tax_amount=tax_amount,
                total=total,


            )
            
            item.save()
            total_all_products += int(float(total))

        # Redirect to a success page or display a success message
        ids = invoice.id
        invoice.total = total_all_products
        invoice.save()
        context = {
            'id':ids
        } 
        url = reverse('edit_sales', args=[ids])
        
        return redirect(url)
        
    item = Item_Acc.objects.all()
    party = Party.objects.all()
    unit = Unit.objects.all()
    context= {
        'item':item,
        'party':party,
        'unit':unit
    }
    return render(request, 'accounts/sales_invoice.html',context)



def edit_sales(request,id):
    invoice = get_object_or_404(Sales_Invoice, id=id)
    products = Item_Invoice.objects.filter(invoice=id)
    if request.method == 'POST':
        # Retrieve data from the form
        name = request.POST.get('name')
        phone_number = request.POST.get('phone_number')
        invoice_number = request.POST.get('invoice_number')
        invoice_date = request.POST.get('invoice_date')
        state_of_supply = request.POST.get('state_of_supply')
        item = request.POST.get('item')
        print(item)
        print(item)
        qty = request.POST.get('qty')
        unit = request.POST.get('unit')
        price = request.POST.get('price')
        discount_percentage = request.POST.get('discount')
        discount_amount = request.POST.get('discount_amount')
        tax_percentage = request.POST.get('tax')
        tax_amount = request.POST.get('tax_amount')
        total = request.POST.get('total')

        # Update the Sales_Invoice object with the new data
        invoice.name = name
        invoice.phone_number = phone_number
        invoice.invoice_number = invoice_number
        invoice.invoice_date = invoice_date
        invoice.state_of_supply = state_of_supply
        total_all_products=0
        for product in products:
            item_id = product.id  # Get the item's ID
            item = request.POST.get(f'item_{item_id}')
            qty = request.POST.get(f'qty_{item_id}')
            unit = request.POST.get(f'unit_{item_id}')
            price = request.POST.get(f'price_{item_id}')
            discount_percentage = request.POST.get(f'discount_{item_id}')
            discount_amount = request.POST.get(f'discount_amount_{item_id}')
            tax_percentage = request.POST.get(f'tax_{item_id}')
            tax_amount = request.POST.get(f'tax_amount_{item_id}')
            total = request.POST.get(f'total_{item_id}')

            # Update the Item_Invoice object with the new item data
            product.item = item
            product.qty = qty
            product.unit = unit
            product.price = price
            product.discount = discount_percentage
            product.discount_amount = discount_amount
            product.tax = tax_percentage
            product.tax_amount = tax_amount
            product.total = total

            # Save the updated Item_Invoice object
            product.save()
            total_all_products += int(float(total))
        invoice.total = total_all_products

        # Save the updated Sales_Invoice object
        invoice.save()

        # Save the invoice object to the database
        

        # Redirect to a success page or display a success message
        return redirect('sales_invoice')  # Replace 'success_page_url' with your actual success page URL

    context= {
            'invoice':invoice,
            'product':products
    }
    return render(request, 'accounts/edit_invoice.html',context)




def Party_User(request):
    selected_value = request.GET.get('id')

    # Query your database or data source to retrieve user data based on selected_value
    # Replace this with your actual database query
    try:
        party = Party.objects.get(id=selected_value)
        data = {
            'success': True,
            'user_name': party.part_name,
            'phone_no': party.phone_number,
            'billing': party.billing_address,
            'opening_balance': party.opening_balance,
        }
    except Party.DoesNotExist:
        data = {
            'success': False,
            'message': 'Details not found for the given Case ID.',
        }
    return JsonResponse(data)

def Item_Details(request):
    selected_value = request.GET.get('id')

    # Query your database or data source to retrieve user data based on selected_value
    # Replace this with your actual database query
    try:
        item = Item_Acc.objects.get(id=selected_value)
        data = {
            'success': True,
            'sale_price': item.sale_price,
            'tax': item.tax_rate,
            'unit': item.unit,
            
        }
    except Item_Acc.DoesNotExist:
        data = {
            'success': False,
            'message': 'Details not found for the given Case ID.',
        }
    return JsonResponse(data)

   

def POS_Details(request):
    selected_value = request.GET.get('id')

    # Query your database or data source to retrieve user data based on selected_value
    # Replace this with your actual database query
    try:
        item = Item_Acc.objects.get(id=selected_value)
        data = {
            'success': True,
            'sale_price': item.sale_price,
            'tax': item.tax_rate,
            'unit': item.unit,
            
        }
    except Item_Acc.DoesNotExist:
        data = {
            'success': False,
            'message': 'Details not found for the given Case ID.',
        }
    return JsonResponse(data)

   


def generate_invoice_pdf(request, id):
    try:
        # Retrieve the Sales_Invoice object based on the provided invoice_id
        invoice = Sales_Invoice.objects.get(id=id)
        products = Item_Invoice.objects.filter(invoice=id)
    except Sales_Invoice.DoesNotExist:
        return HttpResponse('Invoice not found', content_type='text/plain')

    # Create a context dictionary with data from the Sales_Invoice object
    items = []
    total_all_products = 0

    for product in products:
        item_data = {
            'name': product.item,
            'qty': product.qty,
            'unit': product.unit,
            'price': product.price,
            'discount': product.discount,
            'tax': product.tax, 
            'tax_amount': product.tax_amount,
            'total': product.total,
        }
        
        items.append(item_data)
        total_all_products += int(float(product.total))
    context = {
        'invoice_number': invoice.invoice_number,
        'invoice_date': invoice.invoice_date,   
        'customer_name': invoice.name,
        'phone_number': invoice.phone_number,   
        'state_of_supply': invoice.state_of_supply,
        'items': items,
        'total_amount': total_all_products,
        
    }

    # Render the template
    template = get_template('templat/sales_invoice.html')
    html = template.render(context)

    # Create a response object with PDF content type
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="invoice.pdf"'

    # Generate PDF from HTML using ReportLab and pisa
    pisa_status = pisa.CreatePDF(html, dest=response)

    # Return the response
    if pisa_status.err:
        return HttpResponse('PDF generation failed', content_type='text/plain')
    return response





def purchase_invoice(request):
    if request.method == 'POST':
        # Retrieve data from the form
        name = request.POST.get('name')
        phone_number = request.POST.get('phone_number')
        invoice_number = request.POST.get('invoice_number')
        invoice_date = request.POST.get('invoice_date')
        state_of_supply = request.POST.get('state_of_supply')
        item_counter = request.POST.get('item_counter', 0)
        names = re.sub(r'\d', '',name)
        name  = names.replace("_", "")
        print(item_counter)
        if item_counter.isdigit():
            item_counter = int(item_counter)
        else:
            item_counter = 0  # Set a default value if 'item_counter' is not a valid integer
        

        # Create a new Invoice object
        invoice = Sales_Invoice(
            name=name,
            phone_number=phone_number,
            invoice_number=invoice_number,
            invoice_date=invoice_date,
            state_of_supply=state_of_supply,
            type="purchase",
           
        )
        
        # Save the invoice object to the database
        invoice.save()
        total_all_products =0
        id = Sales_Invoice.objects.get(id=invoice.id)
        for i in range(1, item_counter + 1):
            
            
            item = request.POST.get(f'item_{i}')
            qty = request.POST.get(f'qty_{i}')
            items = re.sub(r'\d', '',item)

            item  = items.replace("_", "")
            unit = request.POST.get(f'unit_{i}')
            price = request.POST.get(f'price_{i}')
            discount_percentage = request.POST.get(f'discount_{i}')
            discount_amount = request.POST.get(f'discount_amount_{i}')
            tax_percentage = request.POST.get(f'tax_{i}')
            tax_amount = request.POST.get(f'tax_amount_{i}')
            total = request.POST.get(f'total_{i}')
            print(item)
            
            print(qty)
            
            item = Item_Invoice(
            
                invoice=id,
                item=item,
                qty=qty,
                unit=unit,
                price=price,
                discount=discount_percentage,
                discount_amount=discount_amount,
                tax=tax_percentage,
                tax_amount=tax_amount,
                total=total,

            )
            item.save()
            total_all_products += int(float(total))
        invoice.total = total_all_products

        # Redirect to a success page or display a success message
        ids = invoice.id
        context = {
            'id':ids
        } 
        url = reverse('edit_purchase', args=[ids])
        
        return redirect(url)
        
    item = Item_Acc.objects.all()
    party = Party.objects.all()
    unit = Unit.objects.all()
    context= {
        'item':item,
        'party':party,
        'unit':unit
    }
    return render(request, 'accounts/purchase/purchase_invoice.html',context)




def edit_purchase(request,id):
    invoice = get_object_or_404(Sales_Invoice, id=id)
    products = Item_Invoice.objects.filter(invoice=id)
    if request.method == 'POST':
        # Retrieve data from the form
        name = request.POST.get('name')
        phone_number = request.POST.get('phone_number')
        invoice_number = request.POST.get('invoice_number')
        invoice_date = request.POST.get('invoice_date')
        state_of_supply = request.POST.get('state_of_supply')
        item = request.POST.get('item')
        qty = request.POST.get('qty')
        unit = request.POST.get('unit')
        price = request.POST.get('price')
        discount_percentage = request.POST.get('discount')
        discount_amount = request.POST.get('discount_amount')
        tax_percentage = request.POST.get('tax')
        tax_amount = request.POST.get('tax_amount')
        total = request.POST.get('total')

        # Update the Sales_Invoice object with the new data
        invoice.name = name
        invoice.phone_number = phone_number
        invoice.invoice_number = invoice_number
        invoice.invoice_date = invoice_date
        invoice.state_of_supply = state_of_supply   
        total_all_products = 0
        for product in products:
            item_id = product.id  # Get the item's ID
            item = request.POST.get(f'item')
            qty = request.POST.get(f'qty')
            unit = request.POST.get(f'unit')
            price = request.POST.get(f'price')
            discount_percentage = request.POST.get(f'discount')
            discount_amount = request.POST.get(f'discount_amount')
            tax_percentage = request.POST.get(f'tax')
            tax_amount = request.POST.get(f'tax_amount')
            total = request.POST.get(f'total')

            # Update the Item_Invoice object with the new item data
            product.item = item
            product.qty = qty
            product.unit = unit
            product.price = price
            product.discount = discount_percentage
            product.discount_amount = discount_amount
            product.tax = tax_percentage
            product.tax_amount = tax_amount
            product.total = total

            # Save the updated Item_Invoice object
            product.save()
            total_all_products += int(float(product.total))


        # Save the updated Sales_Invoice obje
        invoice.total = total_all_products
        invoice.save()

        # Save the invoice object to the database
        

        return redirect('purchase_invoice')  # Replace 'success_page_url' with your actual success page URL

    context= {
            'invoice':invoice,
            'product':products
    }
    return render(request, 'accounts/purchase/edit_purchase.html',context)






def generate_purchase_pdf(request, id):
    try:
        # Retrieve the Sales_Invoice object based on the provided invoice_id
        invoice = Sales_Invoice.objects.get(id=id)
        products = Item_Invoice.objects.filter(invoice=id)
    except Sales_Invoice.DoesNotExist:
        return HttpResponse('Invoice not found', content_type='text/plain')

    # Create a context dictionary with data from the Sales_Invoice object
    items = []

    total_all_product = 0
    for product in products:    
        item_data = {
            'name': product.item,
            'qty': product.qty,
            'unit': product.unit,
            'price': product.price,
            'discount': product.discount,
            'tax': product.tax, 
            'tax_amount': product.tax_amount,
            'total': product.total,
        }
        
        items.append(item_data)
        total_all_product    += int(float(product.total))
    context = {
        'invoice_number': invoice.invoice_number,
        'invoice_date': invoice.invoice_date,   
        'customer_name': invoice.name,
        'phone_number': invoice.phone_number,   
        'state_of_supply': invoice.state_of_supply,
        'items': items,
        'total_amount': total_all_product,
    }

    # Render the template
    template = get_template('templat/purchase_invoice.html')
    html = template.render(context)

    # Create a response object with PDF content type
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="invoice.pdf"'

    # Generate PDF from HTML using ReportLab and pisa
    pisa_status = pisa.CreatePDF(html, dest=response)

    # Return the response
    if pisa_status.err:
        return HttpResponse('PDF generation failed', content_type='text/plain')
    return response

def invoice(request):
    invoice = Sales_Invoice.objects.filter(type="sales")
    context = {
        'invoice':invoice
    }
    return render(request,'accounts/invoice.html',context)


def purchase(request):
    bill = Sales_Invoice.objects.filter(type="purchase")
    context = {
        'bill':bill 
    }
    return render(request,'accounts/purchase.html',context)




def create_asset(request):
    if request.method == "POST":
        name = request.POST.get("name")
        description = request.POST.get("description")
        price = request.POST.get("price")
        asset_type = request.POST.get("asset_type")
        date = request.POST.get('date')
        print(date)
        asset = Asset(
            name=name, 
            description=description,
            asset_type=asset_type, 
            price=price,
            date=date)
        asset.save()
        return redirect("create_asset") 
    asset = Asset.objects.all()
    context={
        'asset':asset,
        
    }
    return render(request, "accounts/create_asset.html",context)


def purchase_report(request):
    bill = Sales_Invoice.objects.filter(type="purchase")
    context={ 
        'bill':bill,
    }
    return render(request,'accounts/report/purchase.html',context)



def sales_report(request):
    bill = Sales_Invoice.objects.filter(type="sales")
    context={ 
        'bill':bill,
    }
    return render(request,'accounts/report/sales.html',context)


# Reports 


def report_appointment(request):
    return render(request, 'reports/appointment.html')




def add_medication_dose(request,id):
    if request.method == 'POST':
        date = request.POST['date']
        time = request.POST['time']
        medicine_category = request.POST['medicine_category']
        medicine_name = request.POST['medicine_name']
        dosage = request.POST['dosage']
        remarks = request.POST['remarks']
        ipd_details = get_object_or_404(IpdPatient,id=id)
        patient = get_object_or_404(Patient,id=ipd_details.patient.id)

        medication_dose = MedicationDoseage(
            date=date,
            time=time,
            medicine_category=medicine_category,
            medicine_name=medicine_name,
            dosage=dosage,
            remarks=remarks,
            patient= patient
        )
        medication_dose.save()
        
        url = reverse('ipd_dashboard', args=[id])
        url+= "#nurse"
        return redirect(url)
       
    medicine = MedicationDoseage.objects.all()
    context ={
        'medicine':medicine,
        
    }
    return render(request, 'ipd/pat_dash.html',context)

          # Redirect to a success page or another view

    

def consultant_register(request,id):
    if request.method == 'POST':
        applied_date = request.POST['applied_date']
        instruction_date = request.POST['instruction_date']
        consultant_doctor = request.POST['consultant_doctor']
        instruction = request.POST['instruction']
        ipd_details = get_object_or_404(IpdPatient,id=id)
        patient = get_object_or_404(Patient, id=ipd_details.patient.id)

        consultant  = Consultant_register(
            applied_date=applied_date,
            instruction_date=instruction_date,
            consultant_doctor=consultant_doctor,
            instruction=instruction,
            patient=patient
        )
        consultant.save()
        url = reverse('ipd_dashboard', args=[id])
        url+= "#nurse"
        return redirect(url)

    return render(request, 'appointment_create.html')





def operation_create(request,id):

    if request.method == 'POST':
        operation_category = request.POST['operation_category']
        operation_name = request.POST['operation_name']
        operation_date = request.POST['operation_date']
        consultant_doctor = request.POST['consultant_doctor']
        anesthesia_type = request.POST.get('anesthesia_type', '')
        ot_technician = request.POST.get('ot_technician', '')
        assitant = request.POST.get('assistant', '')
        assistant2 = request.POST.get('assistant2', '')
        remark = request.POST.get('remark', '')
        result = request.POST.get('result', '')

        ipd_details = get_object_or_404(IpdPatient,id=id)
        patient = get_object_or_404(Patient, id=ipd_details.patient.id)
        doctor = get_object_or_404(AddStaff,id=consultant_doctor)


        operation = Operation(
            patient=patient,
            operation_category=operation_category,
            operation_name=operation_name,
            operation_date=operation_date,
            ot_assistant=ot_assistant,
            consultant_doctor=doctor,
            anesthesia_type=anesthesia_type,
            ot_technician=ot_technician,
            assistant=ot_assistant,
            assistant2=assistant2,
            remark=remark,
            result=result
        )
        operation.save()
        url = reverse('ipd_dashboard', args=[id])
        url+= "#nurse"
        return redirect(url)
        

    return render(request,'ipd/pat_dash.html')





def ipd_payment(request,id):
    if request.method == 'POST':
        date = request.POST['date']
        amount = request.POST['amount']
        payment_mode = request.POST['payment_mode']
        note = request.POST.get('note', '')
        patient = get_object_or_404(Patient,id=id)


        payment = Ipd_Payments(
            date=date,
            amount=amount,
            payment_mode=payment_mode,
            patient = patient,
            note=note
        )
        payment.save()
        url = reverse('ipd_dashboard', args=[id])
        url+= "#nurse"
        return redirect(url)
        

    return render(request, 'ipd/ipd.html')




def search_OPD(request):
    if request.method == 'GET':
        doctor = request.GET.get('name', '')
        patient  = request.GET.get('patient', '')
        systoms  = request.GET.get('systoms', '')

        opd = OpdPatient.objects.all()
        

        if doctor:
            results = opd.filter(consultant_doctor=doctor)
            print(results)
              # Replace field_to_search with the field you want to search
        elif patient:
            patients = get_object_or_404(Patient,name=patient)
            results = opd.filter(patient=patients)
        elif systoms:
            results = opd.filter(symptoms_type=systoms)
        else:
            results = None

        return render(request, 'reports/opd.html', {'results': results, 'doctor':opd,'patient':patient })

    return render(request, 'reports/opd.html')



def search_IPD(request):
    if request.method == 'GET':
        doctor = request.GET.get('name', '')
        patient  = request.GET.get('patient', '')
        systoms  = request.GET.get('systoms', '')
        

        opd = IpdPatient.objects.all()
        

        if doctor:
            results = opd.filter(consultant_doctor=doctor)
            print(results)
              # Replace field_to_search with the field you want to search
        elif patient:   

            patients = get_object_or_404(Patient,name=patient)
            results = opd.filter(patient=patients)
            
        elif systoms:   
            results = opd.filter(symptoms_type=systoms)

        else:
            results = None

        return render(request, 'reports/ipd.html', {'results': results, 'doctor':opd,'patient':patient })

    return render(request, 'reports/ipd.html')


def search_patient(request):
    if request.method == 'GET':
        
        patient  = request.GET.get('patient', '')
       
        

        opd = Patient.objects.all()
        

        if patient:
            results = opd.filter(name=patient)

              # Replace field_to_search with the field you want to search

        else:
            results = None

        return render(request, 'reports/patient.html', {'results': results, 'doctor':opd,'patient':patient })

    return render(request, 'reports/patient.html')




def search_tpa(request):
    if request.method == 'GET':
        
        tpa  = request.GET.get('name', '')

        

        opd = TPA.objects.all()
        

        if tpa:
            results = opd.filter(name=tpa)

              # Replace field_to_search with the field you want to search

        else:
            results = None

        return render(request, 'reports/tpa.html', {'results': results, 'tpas':opd,'patient':tpa })
    
    

    return render(request, 'reports/tpa.html')

def search_medicine(request):
    if request.method == 'GET':
        
        medicine = request.GET.get('medicine','')
        medicine_cat = request.GET.get('category','')
        print(medicine)

        

        opd = Medicine.objects.all()
        cat = MedicineCategory.objects.all()
        

        if medicine:
            results = opd.filter(name=medicine)

              # Replace field_to_search with the field you want to search
        elif medicine_cat:
            results = opd.filter(category=medicine_cat)
        else:
            results = None

        return render(request, 'reports/medicine.html', {'results': results, 'med':opd, 'cat':cat })
    
    

    return render(request, 'reports/medicine.html')



def search_appointments(request):
    if request.method == 'GET':
        doctor = request.GET.get('name', '')
        patient  = request.GET.get('patient', '')
        appointment = AppointmentDetails.objects.all()
        print(doctor)

        if doctor:
            results = appointment.filter(doctor=doctor)
            print(results)
              # Replace field_to_search with the field you want to search
        elif patient:
            results = appointment.filter(patient_name=patient)

        else:
            results = None

        return render(request, 'reports/appointment.html', {'results': results, 'doctor':appointment,'patient':patient })
    return render(request, 'reports/appointment.html')


def all_transcation(request):
    transcation = Sales_Invoice.objects.all()
    payment_in = Payment_In.objects.all()
    expense = Expense_Invoice.objects.all()
    cash = CashBook.objects.all()
    bank = Transaction.objects.all()

    context = {
        "transcation":transcation,
        'payment':payment_in,
        'bank':bank,
        'cash':cash,
        'expense':expense
    }

    return render(request,'accounts/all_transcation.html',context)


def all_party(request):
    party = Party.objects.all()
    context ={
        'party':party
    }

    return render(request,'accounts/all_party.html',context)


def create_expense_category(request):
    if request.method == "POST":
        expense_category = request.POST.get("expense_category")
        expense_type = request.POST.get("expense_type")
        
        # Create a new ExpenseCategory instance and save it to the database
        expense_category_obj = Expense_Category(
            expense_category=expense_category,
            expense_type=expense_type
        )
        expense_category_obj.save()
        
        # Redirect to a success page or another appropriate view
        return redirect('expense_category')  # Change 'success_page' to your desired URL name
    expense = Expense_Category.objects.all()
    context={
        'expense':expense
    }
    return render(request, 'accounts/expense_cat.html',context)


def expense_item(request):
    if request.method == 'POST':
        item_name = request.POST.get('item_name')
        price = request.POST.get('price')
        tax_rate = request.POST.get('tax_rate')

        if item_name and price and tax_rate:  # Check if all required fields are filled
            # Create and save the model instance
            Expense_Item.objects.create(item_name=item_name, price=price, tax=tax_rate)

            # Handle form submission, e.g., save the data to the database
            return redirect('expense_item')  # Redirect to a success page after submission
    item = Expense_Item.objects.all()
    context={
        'item':item
    }
    return render(request, 'accounts/expense_item.html',context)




def expense_invoice(request):
    if request.method == 'POST':
        # Retrieve data from the form
        
        name = request.POST.get('name')
        invoice_number = request.POST.get('invoice_number')
        invoice_date = request.POST.get('invoice_date')
        expense_category = request.POST.get('expense_category')
      
        payment_type = request.POST.get('payment_type')
        item_counter = request.POST.get('item_counter', 0)
 

        print(item_counter)
        if expense_category:
            expense = Expense_Category.objects.get(id=expense_category)
            
        

        if item_counter.isdigit():
            item_counter = int(item_counter)
        else:
            item_counter = 0  # Set a default value if 'item_counter' is not a valid integer
        

        # Create a new Invoice object
        invoice = Expense_Invoice(

            expense_category = expense, 
            invoice_number=invoice_number,
            invoice_date=invoice_date,
            payment_type = payment_type
            
        
           
        )
        
        # Save the invoice object to the database
        invoice.save()
        id = Expense_Invoice.objects.get(id=invoice.id)
        total_all_products =0

        for i in range(1, item_counter + 1):
            
            

            item = request.POST.get(f'item_{i}')
            items = re.sub(r'\d', '',item)

            item  = items.replace("_", "")
            qty = request.POST.get(f'qty_{i}')
            
            price = request.POST.get(f'price_{i}')
            
            
            total = request.POST.get(f'total_{i}')
            
            print(item)
            
            print(qty)
            
            
            item = Expense_inv_Item(
            
                invoice=id,
                item=item,
                qty=qty,
                
                price=price,
                
                total=total,


            )
            
            item.save()
            total_all_products += int(float(total))

        # Redirect to a success page or display a success message
        ids = invoice.id
        invoice.total = total_all_products
        invoice.save()
        
        
        return redirect('expense_invoice')
        
    item = Expense_Item.objects.all()
    party = Party.objects.all()
    unit = Expense_Category.objects.all()
    context= {
        'item':item,
        'party':party,
        'category':unit
    }
    return render(request, 'accounts/expense_invoice.html',context)


def Expense_details(request):
    selected_value = request.GET.get('id')

    # Query your database or data source to retrieve user data based on selected_value
    # Replace this with your actual database query
    try:
        item = Expense_Item.objects.get(id=selected_value)
        data = {
            'success': True,
            'price': item.price,
            'tax': item.tax,
            
            
        }
    except Expense_Item.DoesNotExist:
        data = {
            'success': False,
            'message': 'Details not found for the given Case ID.',
        }
    return JsonResponse(data)



def sales_order(request):
    if request.method == 'POST':
        # Retrieve data from the form
        name = request.POST.get('name')
        phone_number = request.POST.get('phone_number')
        invoice_number = request.POST.get('invoice_number')
        invoice_date = request.POST.get('invoice_date')
        due_date = request.POST.get('due_date')
        advance_amount = request.POST.get('advance_amount')
        names = re.sub(r'\d', '',name)
        name  = names.replace("_", "")
        state_of_supply = request.POST.get('state_of_supply')
        item_counter = request.POST.get('item_counter', 0)
        print(item_counter)
        if item_counter.isdigit():
            item_counter = int(item_counter)
        else:
            item_counter = 0  # Set a default value if 'item_counter' is not a valid integer
        

        # Create a new Invoice object
        invoice = Sales_Invoice(
            name=name,
            phone_number=phone_number,
            invoice_number=invoice_number,
            invoice_date=invoice_date,
            state_of_supply=state_of_supply,
            due_date=due_date,
            advance_amount=advance_amount,
            type="sales_order",
           
        )
        
        # Save the invoice object to the database
        invoice.save()
        id = Sales_Invoice.objects.get(id=invoice.id)
        total_all_products =0

        for i in range(1, item_counter + 1):
            
            
            item = request.POST.get(f'item_{i}')
            qty = request.POST.get(f'qty_{i}')
            items = re.sub(r'\d', '',item)

            item  = items.replace("_", "")
            unit = request.POST.get(f'unit_{i}')
            price = request.POST.get(f'price_{i}')
            discount_percentage = request.POST.get(f'discount_{i}')
            discount_amount = request.POST.get(f'discount_amount_{i}')
            tax_percentage = request.POST.get(f'tax_{i}')
            tax_amount = request.POST.get(f'tax_amount_{i}')
            total = request.POST.get(f'total_{i}')
            
            print(item)
            
            print(qty)
            
            item = Item_Invoice(
            
                invoice=id,
                item=item,
                qty=qty,
                unit=unit,
                price=price,
                discount=discount_percentage,
                discount_amount=discount_amount,
                tax=tax_percentage,
                tax_amount=tax_amount,
                total=total,


            )
            
            item.save()
            total_all_products += int(float(total))

        # Redirect to a success page or display a success message
        ids = invoice.id
        invoice.total = total_all_products
        invoice.save()
        context = {
            'id':ids
        } 
        url = reverse('edit_sales_order', args=[ids])
        
        return redirect(url)
        
    item = Item_Acc.objects.all()
    party = Party.objects.all()
    unit = Unit.objects.all()
    context= {
        'item':item,
        'party':party,
        'unit':unit
    }
    return render(request, 'accounts/sales_order.html',context)





def edit_sales_order(request,id):
    invoice = get_object_or_404(Sales_Invoice, id=id)
    products = Item_Invoice.objects.filter(invoice=id)
    if request.method == 'POST':
        # Retrieve data from the form
        name = request.POST.get('name')
        phone_number = request.POST.get('phone_number')
        invoice_number = request.POST.get('invoice_number')
        invoice_date = request.POST.get('invoice_date')
        state_of_supply = request.POST.get('state_of_supply')
        due_date = request.POST.get('due_date')
        advance_amount = request.POST.get('advance_amount')
        item = request.POST.get('item')
        qty = request.POST.get('qty')
        unit = request.POST.get('unit')
        price = request.POST.get('price')
        discount_percentage = request.POST.get('discount')
        discount_amount = request.POST.get('discount_amount')
        tax_percentage = request.POST.get('tax')
        tax_amount = request.POST.get('tax_amount')
        
        total = request.POST.get('total')

        # Update the Sales_Invoice object with the new data
        invoice.name = name
        invoice.phone_number = phone_number
        invoice.invoice_number = invoice_number
        invoice.invoice_date = invoice_date
        invoice.state_of_supply = state_of_supply   
        invoice.advance_amount= advance_amount
        invoice.due_date=due_date
        total_all_products = 0
        for product in products:
            item_id = product.id  # Get the item's ID
            item = request.POST.get(f'item')
            qty = request.POST.get(f'qty')
            unit = request.POST.get(f'unit')
            price = request.POST.get(f'price')
            discount_percentage = request.POST.get(f'discount')
            discount_amount = request.POST.get(f'discount_amount')
            tax_percentage = request.POST.get(f'tax')
            tax_amount = request.POST.get(f'tax_amount')
            total = request.POST.get(f'total')

            # Update the Item_Invoice object with the new item data
            product.item = item
            product.qty = qty
            product.unit = unit
            product.price = price
            product.discount = discount_percentage
            product.discount_amount = discount_amount
            product.tax = tax_percentage
            product.tax_amount = tax_amount
            product.total = total

            # Save the updated Item_Invoice object
            product.save()
            total_all_products += int(float(product.total))


        # Save the updated Sales_Invoice obje
        invoice.total = total_all_products
        invoice.save()

        # Save the invoice object to the database
        

        return redirect('sales_order')  # Replace 'success_page_url' with your actual success page URL

    context= {
            'invoice':invoice,
            'product':products
    }
    return render(request, 'accounts/sales/edit_salesorder.html',context)





def sales_estimate(request):
    if request.method == 'POST':
        # Retrieve data from the form
        name = request.POST.get('name')
        phone_number = request.POST.get('phone_number')
        invoice_number = request.POST.get('invoice_number')
        invoice_date = request.POST.get('invoice_date')
        
        state_of_supply = request.POST.get('state_of_supply')
        item_counter = request.POST.get('item_counter', 0)
        names = re.sub(r'\d', '',name)
        name  = names.replace("_", "")
        print(item_counter)
        if item_counter.isdigit():
            item_counter = int(item_counter)
        else:
            item_counter = 0  # Set a default value if 'item_counter' is not a valid integer
        

        # Create a new Invoice object
        invoice = Sales_Invoice(
            name=name,
            phone_number=phone_number,
            invoice_number=invoice_number,
            invoice_date=invoice_date,
            state_of_supply=state_of_supply,
        
            type="sales_estimate",
           
        )
        
        # Save the invoice object to the database
        invoice.save()
        id = Sales_Invoice.objects.get(id=invoice.id)
        total_all_products =0

        for i in range(1, item_counter + 1):
            
            
            item = request.POST.get(f'item_{i}')
            qty = request.POST.get(f'qty_{i}')
            unit = request.POST.get(f'unit_{i}')
            items = re.sub(r'\d', '',item)

            item  = items.replace("_", "")
            price = request.POST.get(f'price_{i}')
            discount_percentage = request.POST.get(f'discount_{i}')
            discount_amount = request.POST.get(f'discount_amount_{i}')
            tax_percentage = request.POST.get(f'tax_{i}')
            tax_amount = request.POST.get(f'tax_amount_{i}')
            total = request.POST.get(f'total_{i}')
            
            print(item)
            
            print(qty)
            
            item = Item_Invoice(
            
                invoice=id,
                item=item,
                qty=qty,
                unit=unit,
                price=price,
                discount=discount_percentage,
                discount_amount=discount_amount,
                tax=tax_percentage,
                tax_amount=tax_amount,
                total=total,


            )
            
            item.save()
            total_all_products += int(float(total))

        # Redirect to a success page or display a success message
        ids = invoice.id
        invoice.total = total_all_products
        invoice.save()
        context = {
            'id':ids
        } 
        url = reverse('edit_sales_order', args=[ids])
        
        return redirect(url)
        
    item = Item_Acc.objects.all()
    party = Party.objects.all()
    unit = Unit.objects.all()
    context= {
        'item':item,
        'party':party,
        'unit':unit
    }
    return render(request, 'accounts/sales_estimate.html',context)







def edit_sales_estimate(request,id):
    invoice = get_object_or_404(Sales_Invoice, id=id)
    products = Item_Invoice.objects.filter(invoice=id)
    if request.method == 'POST':
        # Retrieve data from the form
        name = request.POST.get('name')
        phone_number = request.POST.get('phone_number')
        invoice_number = request.POST.get('invoice_number')
        invoice_date = request.POST.get('invoice_date')
        state_of_supply = request.POST.get('state_of_supply')
        
        item = request.POST.get('item')
        qty = request.POST.get('qty')
        unit = request.POST.get('unit')
        price = request.POST.get('price')
        discount_percentage = request.POST.get('discount')
        discount_amount = request.POST.get('discount_amount')
        tax_percentage = request.POST.get('tax')
        tax_amount = request.POST.get('tax_amount')
        total = request.POST.get('total')

        # Update the Sales_Invoice object with the new data
        invoice.name = name
        invoice.phone_number = phone_number
        invoice.invoice_number = invoice_number
        invoice.invoice_date = invoice_date
        invoice.state_of_supply = state_of_supply   
    
        
        total_all_products = 0
        for product in products:
            item_id = product.id  # Get the item's ID
            item = request.POST.get(f'item')
            qty = request.POST.get(f'qty')
            unit = request.POST.get(f'unit')
            price = request.POST.get(f'price')
            discount_percentage = request.POST.get(f'discount')
            discount_amount = request.POST.get(f'discount_amount')
            tax_percentage = request.POST.get(f'tax')
            tax_amount = request.POST.get(f'tax_amount')
            total = request.POST.get(f'total')

            # Update the Item_Invoice object with the new item data
            product.item = item
            product.qty = qty
            product.unit = unit
            product.price = price
            product.discount = discount_percentage
            product.discount_amount = discount_amount
            product.tax = tax_percentage
            product.tax_amount = tax_amount
            product.total = total

            # Save the updated Item_Invoice object
            product.save()
            total_all_products += int(float(product.total))


        # Save the updated Sales_Invoice obje
        invoice.total = total_all_products
        invoice.save()

        # Save the invoice object to the database
        

        return redirect('sales_estimate')  # Replace 'success_page_url' with your actual success page URL

    context= {
            'invoice':invoice,
            'product':products
    }
    return render(request, 'accounts/sales/edit_salesestimate.html',context)




def payment_in(request):
    if request.method == "POST":
        name = request.POST["name"]
        
        payment_type = request.POST["payment_type"]
        receipt_no = request.POST["receipt_no"]
        date = request.POST["date"]
        received = request.POST["received"]

        balance = Party.objects.get(id=name)
        if balance.to_receive ==True:
            
            bal = balance.opening_balance - int(received)
            print(bal)
            balance.opening_balance = bal
            balance.save()

        
        Payment_In.objects.create(
            name=name,
            payment_type=payment_type,
            receipt_no=receipt_no,
            date=date,
            received=received
        )   



    payment = Payment_In.objects.all()
    party = Party.objects.all()
    

    
    context={
        'party':party,
        'payment':payment,

    }


    return render(request, "accounts/payment_in.html",context)






def balance_sheet(request):
    # Calculate total sales and purchases

    start_date = date.today()
    total_sales = Item_Invoice.objects.filter(invoice__type='sales').aggregate(
        total_sales=Sum(F('total'))
    )['total_sales'] or 0

    total_purchases = Item_Invoice.objects.filter(invoice__type='purchase').aggregate(
        total_purchases=Sum(F('total'))
    )['total_purchases'] or 0

    
    total_sales_tax = Item_Invoice.objects.filter(invoice__type='sales').aggregate(
        total_sales_tax=Sum(F('tax_amount'))
    )['total_sales_tax'] or 0

    total_purchase_tax = Item_Invoice.objects.filter(invoice__type='purchase').aggregate(
        total_purchase_tax=Sum(F('tax_amount'))
    )['total_purchase_tax'] or 0


    opening_stock = Item_Acc.objects.aggregate(
        opening_stock=Sum(ExpressionWrapper(F('opening_quantity') * F('purchase_price'), output_field=DecimalField(max_digits=13, decimal_places=3)))
    )['opening_stock'] or 0

    total_short_term_assets = Asset.objects.filter(asset_type='Short-Term').aggregate(
        total_short_term_assets=Sum('price')
    )['total_short_term_assets'] or 0

    total = Asset.objects.filter(asset_type="Long-term")

    total_receivable = Party.objects.filter(to_receive = True).aggregate(
        total_receivable=Sum('opening_balance')
    )['total_receivable'] or 0

    total_payable = Party.objects.filter(to_pay = True).aggregate(
        total_payable=Sum('opening_balance')
    )['total_payable'] or 0
    
    

    total_short_term_liablity = Liablity.objects.filter(liablity_type='Short-Term').aggregate(
        total_short_term_liablity=Sum('price')
    )['total_short_term_liablity'] or 0

    total_long_term_liablity = Liablity.objects.filter(liablity_type='Long-Term').aggregate(
        total_long_term_liablity=Sum('price')
    )['total_long_term_liablity'] or 0

    total_long_term_assets = Asset.objects.filter(asset_type='Long-Term').aggregate(
        total_long_term_assets=Sum('price')
    )['total_long_term_assets'] or 0


    

    depreciation = Depreciation.objects.all().aggregate(amount=Sum('amount'))['amount'] or 0

    
    try:
        indirect_expense_category = Expense_Category.objects.get(expense_type='Indirect_Expense')
        indirect_expenses = Expense_Invoice.objects.filter(expense_category=indirect_expense_category)
        total_indirect_expense = indirect_expenses.aggregate(total_indirect=Sum('total'))['total_indirect'] or 0
    except Expense_Category.DoesNotExist:
        total_indirect_expense = 0

    try:
        direct_expense_type = Expense_Category.objects.get(expense_type='Direct_Expense')
        direct_expense = Expense_Invoice.objects.filter(expense_category=direct_expense_type)
        total_direct_expense = direct_expense.aggregate(total_direct=Sum('total'))['total_direct'] or 0
    except Expense_Category.DoesNotExist:
        total_direct_expense = 0

    total_back_account = BankAccount.objects.all().aggregate(
        total_balance=Sum(F('balance'))
    )['total_balance'] or 0
    withdraw = Transaction.objects.filter(transaction_type='Withdrawl').aggregate(
        total_withdrawl= Sum(F('amount'))
    )['total_withdrawl']or 0

    income = Income.objects.all().aggregate(
        total_income= Sum(F('amount'))
    )['total_income']or 0


    indirect_expense = total_indirect_expense+depreciation
    closing_stock = opening_stock + total_purchases - total_sales
    equity =   opening_stock + total_receivable  + total_back_account -withdraw

    balance = (total_sales - total_purchases) + (total_sales_tax - total_purchase_tax) + closing_stock + total_short_term_assets + total_long_term_assets -indirect_expense+total_direct_expense +equity -(total_long_term_liablity+total_short_term_liablity) + income

    


    context = {
        'total_sales': total_sales,
        'total_purchases': total_purchases,
        'balance': balance,
        'opening_stock': opening_stock,
        'closing_stock': closing_stock,
        'total_sales_tax': total_sales_tax,
        'total_short_term_assets': total_short_term_assets,
        'total_long_term_liablity':total_long_term_liablity,
        'total_short_term_liablity':total_short_term_liablity,
        'total_long_term_assets': total_long_term_assets,
        'total_purchase_tax': total_purchase_tax,
        'start_date':start_date,
        'receivable':total_receivable,
        'payable':total_payable,
        'indirect_expense':total_indirect_expense,
        'direct_expense':total_direct_expense,
        'withdraw':withdraw,
        'equity':equity,
        'other_income':income,
    }

    return render(request, 'accounts/report/balancesheet.html', context)


def cash_flow(request):
    total_sales = Sales_Invoice.objects.filter(type='sales')
    payment_in = Payment_In.objects.all()
    expense = Expense_Invoice.objects.all()

    context ={
        'sales':total_sales,
        'payment_in':payment_in,
        'expense':expense
    }

    return render(request,'accounts/report/cash_flow.html',context)










def delivery_challan(request):
    if request.method == 'POST':
        # Retrieve data from the form
        name = request.POST.get('name')
        phone_number = request.POST.get('phone_number')
        invoice_number = request.POST.get('invoice_number')
        invoice_date = request.POST.get('invoice_date')
        names = re.sub(r'\d', '',name)
        name  = names.replace("_", "")
        
        state_of_supply = request.POST.get('state_of_supply')
        item_counter = request.POST.get('item_counter', 0)
        print(item_counter)
        if item_counter.isdigit():
            item_counter = int(item_counter)
        else:
            item_counter = 0  # Set a default value if 'item_counter' is not a valid integer
        

        # Create a new Invoice object
        invoice = Sales_Invoice(
            name=name,
            phone_number=phone_number,
            invoice_number=invoice_number,
            invoice_date=invoice_date,
            state_of_supply=state_of_supply,
        
            type="delivery_challan",
           
        )
        
        # Save the invoice object to the database
        invoice.save()
        id = Sales_Invoice.objects.get(id=invoice.id)
        total_all_products =0

        for i in range(1, item_counter + 1):
            
            
            item = request.POST.get(f'item_{i}')
            qty = request.POST.get(f'qty_{i}')
            items = re.sub(r'\d', '',item)

            item  = items.replace("_", "")
            unit = request.POST.get(f'unit_{i}')
            price = request.POST.get(f'price_{i}')
            discount_percentage = request.POST.get(f'discount_{i}')
            discount_amount = request.POST.get(f'discount_amount_{i}')
            tax_percentage = request.POST.get(f'tax_{i}')
            tax_amount = request.POST.get(f'tax_amount_{i}')
            total = request.POST.get(f'total_{i}')
            
            print(item)
            
            print(qty)
            
            item = Item_Invoice(
            
                invoice=id,
                item=item,
                qty=qty,
                unit=unit,
                price=price,
                discount=discount_percentage,
                discount_amount=discount_amount,
                tax=tax_percentage,
                tax_amount=tax_amount,
                total=total,


            )
            
            item.save()
            total_all_products += int(float(total))

        # Redirect to a success page or display a success message
        ids = invoice.id
        invoice.total = total_all_products
        invoice.save()
        context = {
            'id':ids
        } 
        url = reverse('edit_challan', args=[ids])
        
        return redirect(url)
        
    item = Item_Acc.objects.all()
    party = Party.objects.all()
    unit = Unit.objects.all()
    context= {
        'item':item,
        'party':party,
        'unit':unit
    }
    return render(request, 'accounts/delivery_challan.html',context)






def edit_delivery_challan(request,id):
    invoice = get_object_or_404(Sales_Invoice, id=id)
    products = Item_Invoice.objects.filter(invoice=id)
    if request.method == 'POST':
        # Retrieve data from the form
        name = request.POST.get('name')
        phone_number = request.POST.get('phone_number')
        invoice_number = request.POST.get('invoice_number')
        invoice_date = request.POST.get('invoice_date')
        state_of_supply = request.POST.get('state_of_supply')
        
        item = request.POST.get('item')
        qty = request.POST.get('qty')
        unit = request.POST.get('unit')
        price = request.POST.get('price')
        discount_percentage = request.POST.get('discount')
        discount_amount = request.POST.get('discount_amount')
        tax_percentage = request.POST.get('tax')
        tax_amount = request.POST.get('tax_amount')
        total = request.POST.get('total')

        # Update the Sales_Invoice object with the new data
        invoice.name = name
        invoice.phone_number = phone_number
        invoice.invoice_number = invoice_number
        invoice.invoice_date = invoice_date
        invoice.state_of_supply = state_of_supply   
    
        
        total_all_products = 0
        for product in products:
            item_id = product.id  # Get the item's ID
            item = request.POST.get(f'item')
            qty = request.POST.get(f'qty')
            unit = request.POST.get(f'unit')
            price = request.POST.get(f'price')
            discount_percentage = request.POST.get(f'discount')
            discount_amount = request.POST.get(f'discount_amount')
            tax_percentage = request.POST.get(f'tax')
            tax_amount = request.POST.get(f'tax_amount')
            total = request.POST.get(f'total')

            # Update the Item_Invoice object with the new item data
            product.item = item
            product.qty = qty
            product.unit = unit
            product.price = price
            product.discount = discount_percentage
            product.discount_amount = discount_amount
            product.tax = tax_percentage
            product.tax_amount = tax_amount
            product.total = total

            # Save the updated Item_Invoice object
            product.save()
            total_all_products += int(float(product.total))


        # Save the updated Sales_Invoice obje
        invoice.total = total_all_products
        invoice.save()

        # Save the invoice object to the database
        

        return redirect('delivery_challan')  # Replace 'success_page_url' with your actual success page URL

    context= {
            'invoice':invoice,
            'product':products
    }
    return render(request, 'accounts/sales/edit_challan.html',context)







def credit_note(request):
    if request.method == 'POST':
        # Retrieve data from the forms
        name = request.POST.get('name')
        phone_number = request.POST.get('phone_number')
        invoice_number = request.POST.get('invoice_number')
        invoice_date = request.POST.get('invoice_date')
        names = re.sub(r'\d', '',name)
        name  = names.replace("_", "")
        
        state_of_supply = request.POST.get('state_of_supply')
        item_counter = request.POST.get('item_counter', 0)
        print(item_counter)
        if item_counter.isdigit():
            item_counter = int(item_counter)
        else:
            item_counter = 0  # Set a default value if 'item_counter' is not a valid integer
        

        # Create a new Invoice object
        invoice = Sales_Invoice(
            name=name,
            phone_number=phone_number,
            invoice_number=invoice_number,
            invoice_date=invoice_date,
            state_of_supply=state_of_supply,
        
            type="credit_note",
           
        )
        
        # Save the invoice object to the database
        invoice.save()
        id = Sales_Invoice.objects.get(id=invoice.id)
        total_all_products =0

        for i in range(1, item_counter + 1):


            
            
            item = request.POST.get(f'item_{i}')

            items = re.sub(r'\d', '',item)

            item  = items.replace("_", "")

            
            qty = request.POST.get(f'qty_{i}')
            unit = request.POST.get(f'unit_{i}')
            price = request.POST.get(f'price_{i}')
            discount_percentage = request.POST.get(f'discount_{i}')
            discount_amount = request.POST.get(f'discount_amount_{i}')
            tax_percentage = request.POST.get(f'tax_{i}')
            tax_amount = request.POST.get(f'tax_amount_{i}')
            total = request.POST.get(f'total_{i}')
            
            print(item)
            
            print(qty)
            
            item = Item_Invoice(
            
                invoice=id,
                item=item,
                
                qty=qty,
                unit=unit,
                price=price,
                discount=discount_percentage,
                discount_amount=discount_amount,
                tax=tax_percentage,
                tax_amount=tax_amount,
                total=total,


            )
            
            item.save()
            total_all_products += int(float(total))

        # Redirect to a success page or display a success message
        ids = invoice.id
        invoice.total = total_all_products
        invoice.save()
        context = {
            'id':ids
        } 
        url = reverse('edit_credit_note', args=[ids])
        
        return redirect(url)
        
    item = Item_Acc.objects.all()
    party = Party.objects.all()
    unit = Unit.objects.all()
    context= {
        'item':item,
        'party':party,
        'unit':unit
    }
    return render(request, 'accounts/credit_note.html',context)





def edit_credit_note(request,id):
    invoice = get_object_or_404(Sales_Invoice, id=id)
    products = Item_Invoice.objects.filter(invoice=id)
    if request.method == 'POST':
        # Retrieve data from the form
        name = request.POST.get('name')
        phone_number = request.POST.get('phone_number')
        invoice_number = request.POST.get('invoice_number')
        invoice_date = request.POST.get('invoice_date')
        state_of_supply = request.POST.get('state_of_supply')
        
        item = request.POST.get('item')
        qty = request.POST.get('qty')
        unit = request.POST.get('unit')
        price = request.POST.get('price')
        discount_percentage = request.POST.get('discount')
        discount_amount = request.POST.get('discount_amount')
        tax_percentage = request.POST.get('tax')
        tax_amount = request.POST.get('tax_amount')
        total = request.POST.get('total')

        # Update the Sales_Invoice object with the new data
        invoice.name = name
        invoice.phone_number = phone_number
        invoice.invoice_number = invoice_number
        invoice.invoice_date = invoice_date
        invoice.state_of_supply = state_of_supply   
    
        
        total_all_products = 0
        for product in products:
            item_id = product.id  # Get the item's ID
            item = request.POST.get(f'item')
            qty = request.POST.get(f'qty')
            unit = request.POST.get(f'unit')
            price = request.POST.get(f'price')
            discount_percentage = request.POST.get(f'discount')
            discount_amount = request.POST.get(f'discount_amount')
            tax_percentage = request.POST.get(f'tax')
            tax_amount = request.POST.get(f'tax_amount')
            total = request.POST.get(f'total')

            # Update the Item_Invoice object with the new item data
            product.item = item
            product.qty = qty
            product.unit = unit
            product.price = price
            product.discount = discount_percentage
            product.discount_amount = discount_amount
            product.tax = tax_percentage
            product.tax_amount = tax_amount
            product.total = total

            # Save the updated Item_Invoice object
            product.save()
            total_all_products += int(float(product.total))


        # Save the updated Sales_Invoice obje
        invoice.total = total_all_products
        invoice.save()

        # Save the invoice object to the database
        

        return redirect('credit_note')  # Replace 'success_page_url' with your actual success page URL

    context= {
            'invoice':invoice,
            'product':products
    }
    return render(request, 'accounts/sales/edit_creditnote.html',context)



def bank_account(request):

    if request.method == 'POST':
        account_number = request.POST.get('account_number')
        balance = request.POST.get('balance')
        as_of_date = request.POST.get('as_of_date')
        # Validate and save the data as needed
        if account_number and balance and as_of_date:
            BankAccount.objects.create(account_number=account_number, balance=balance, as_of_date=as_of_date)
            return redirect('bank_account_list')  # Redirect to a list view or another page
        else:
            print('canhelp1')
    bank = BankAccount.objects.all()
    context ={
        'bank':bank
    }
    return render(request, 'accounts/bank_account.html',context)

def bank_account_list(request,id):
    bank_id = BankAccount.objects.get(id=id)
    transaction = Transaction.objects.filter(account=id)
    
    context = {
        'bank':bank_id,
        'transaction':transaction,
    }
    return render(request,'accounts/bank_accountlist.html',context)




def deposit(request, id):
    if request.method == 'POST':
        amount = Decimal(request.POST['amount'])
        type = request.POST.get('type')
        if type == 'deposit':
            account = BankAccount.objects.get(id=id)
        
            account.balance += amount
            account.save()
            Transaction.objects.create(account=account, transaction_type='Deposit', amount=amount)

            return redirect('bank_accountlist', id=id)
        elif type == 'withdrawl':
            account = BankAccount.objects.get(id=id)
            account.balance -= amount
            account.save()
            Transaction.objects.create(account=account, transaction_type='Withdrawal', amount=amount)
            return redirect('bank_accountlist', id=id)
       
    return render(request, 'account/bank_account.html')

def withdrawal(request, id):
    if request.method == 'POST':
        amount = Decimal(request.POST['amount'])
        account = BankAccount.objects.get(id=id)
        if account.balance >= amount:
            account.balance -= amount
            account.save()
            Transaction.objects.create(account=account, transaction_type='Withdrawal', amount=amount)
            return redirect('bank_accountlist', id=id)
        else:
            return render(request, 'insufficient_funds.html')
    return render(request, 'account/bank_account.html')




def profit_and_loss_statement(request):
    # Query the database for relevant data
    

    # Initialize variables for different sections of the profit and loss statement
 

    # Iterate through the entries and calculate the totals for each section
    total_sales = Item_Invoice.objects.filter(invoice__type='sales').aggregate(
        total_sales=Sum(F('total'))
    )['total_sales'] or 0


    total_purchase = Item_Invoice.objects.filter(invoice__type='purchase').aggregate(
        total_sales=Sum(F('total'))
    )['total_sales'] or 0

    

    total_return = Item_Invoice.objects.filter(invoice__type='credit_note').aggregate(
        total_sales=Sum(F('total'))
    )['total_sales'] or 0
    opening_stock = Item_Acc.objects.aggregate(
        opening_stock=Sum(ExpressionWrapper(F('opening_quantity') * F('purchase_price'), output_field=DecimalField(max_digits=13, decimal_places=3)))
    )['opening_stock'] or 0

    total_sales_tax = Item_Invoice.objects.filter(invoice__type='sales').aggregate(
        total_sales_tax=Sum(F('tax_amount'))
    )['total_sales_tax'] or 0

    total_purchase_tax = Item_Invoice.objects.filter(invoice__type='purchase').aggregate(
        total_purchase_tax=Sum(F('tax_amount'))
    )['total_purchase_tax'] or 0

    


    depreciation = Depreciation.objects.all().aggregate(amount=Sum('amount'))['amount'] or 0

    try:
        indirect_expense_category = Expense_Category.objects.get(expense_type='Indirect_Expense')
        indirect_expenses = Expense_Invoice.objects.filter(expense_category=indirect_expense_category)
        total_indirect_expense = indirect_expenses.aggregate(total_indirect=Sum('total'))['total_indirect'] or 0
    except Expense_Category.DoesNotExist:
        total_indirect_expense = 0

    try:
        direct_expense_type = Expense_Category.objects.get(expense_type='Direct_Expense')
        direct_expense = Expense_Invoice.objects.filter(expense_category=direct_expense_type)
        total_direct_expense = direct_expense.aggregate(total_direct=Sum('total'))['total_direct'] or 0
    except Expense_Category.DoesNotExist:
        total_direct_expense = 0

  
    total_short_term_assets = Asset.objects.filter(asset_type='Short-Term').aggregate(
        total_short_term_assets=Sum('price')
    )['total_short_term_assets'] or 0

    total_short_term_liablity = Liablity.objects.filter(liablity_type='Short-Term').aggregate(
        total_short_term_liablity=Sum('price')
    )['total_short_term_liablity'] or 0
    

    indirect_expense = total_indirect_expense+depreciation

    closing_stock = Sales_Invoice.objects.filter(type='sales').aggregate(
        total_short_term_assets=Sum('item_invoice')
    )['total_short_term_assets'] or 0

    
    income = Income.objects.all().aggregate(
        total_income= Sum(F('amount'))
    )['total_income']or 0

    # Calculate Gross Profit
    gross_profit = total_sales - total_return - total_direct_expense

    # Calculate Net Profit
    closing= opening_stock + total_purchase - closing_stock

    net_profit = gross_profit  - total_direct_expense +income

 

    return render(request, 'accounts/report/profit_loss.html', {
        'sales': total_sales,
        'credit_notes': total_return,
        'opening_stock': opening_stock,
        'closing_stock': closing,
        'direct_expenses': total_direct_expense,
        'tax_payable': total_purchase_tax,
        'short_asset':total_short_term_assets,
        'short_liablity':total_short_term_liablity,
        'tax_receivable': total_sales_tax,
        'indirect_expenses': indirect_expense,
        'gross_profit': gross_profit,
        'other_income':income,
        'net_profit': net_profit
    })



def gstreport(request):
    # Query the database for relevant data
    

    # Initialize variables for different sections of the profit and loss statement
 

    # Iterate through the entries and calculate the totals for each section
  

    total_sales_tax = Item_Invoice.objects.filter(invoice__type='sales').aggregate(
        total_sales_tax=Sum(F('tax_amount'))
    )['total_sales_tax'] or 0

    total_purchase_tax = Item_Invoice.objects.filter(invoice__type='purchase').aggregate(
        total_purchase_tax=Sum(F('tax_amount'))
    )['total_purchase_tax'] or 0

    tax_diffrence = total_sales_tax - total_purchase_tax




    return render(request, 'accounts/report/gstreport.html', {

        'tax_payable': total_purchase_tax,

        'tax_receivable': total_sales_tax,
        'total':tax_diffrence,
       
    })

def get_bed_details(request):
    beds = Bed.objects.all()
    data = serializers.serialize("json", beds)
    return JsonResponse(data, safe=False)



def expense_list(request):
    expense = Expense_Invoice.objects.all()
    context ={
        'expense':expense
    }
    return render(request,'accounts/list/expense.html',context)


def sales_orderlist(request):
    order = Sales_Invoice.objects.filter(type="sales_order")
    context ={
        'order':order,
    }
    return render(request,'accounts/list/sale_order.html',context)



def sales_invoice_list(request):
    sales = Sales_Invoice.objects.filter(type="sales")
    context ={
        'sales':sales,
    }
    return render(request,'accounts/list/sales_invoices.html',context)



def estimate_list(request):
    estimate = Sales_Invoice.objects.filter(type="sales_estimate")
    context ={
        'estimate':estimate,
    }
    return render(request,'accounts/list/estimate_list.html',context)




def challan_list(request):
    challan = Sales_Invoice.objects.filter(type="delivery_challan")
    context ={
        'challan':challan,
    }
    return render(request,'accounts/list/challan_list.html',context)


def return_list(request):
    sales_return = Sales_Invoice.objects.filter(type="credit_note")
    context ={
        'return':sales_return,
    }
    return render(request,'accounts/list/sales_return.html',context)




def payment_list(request):
    payment = Payment_In.objects.all()
    context ={
        'payment':payment,
    }
    return render(request,'accounts/list/payment_in.html',context)




def edit_party(request, party_id=None):
    # Check if an 'id' is provided. If provided, it's for editing.
    if party_id is not None:
        party = get_object_or_404(Party, id=party_id)
    else:
        # If 'id' is not provided, it's for creating a new party.
        party = None

    if request.method == 'POST':
        # Retrieve data from the form and create/update a party record
        part_name = request.POST['part_name']
        gstin = request.POST['gstin']
        phone_number = request.POST['phone_number']
        gst_type = request.POST['gst_type']
        state = request.POST['state']
        email_id = request.POST['email_id']
        billing_address = request.POST['billing_address']
        opening_balance = request.POST['opening_balance']
        as_of_date = request.POST['as_of_date']
        to_pay = request.POST.get('to_pay', False)
        
        to_receive = request.POST.get('to_receive', False)
        if to_pay == 'on':
           to_pay = True
        else:
            to_pay = False
        
        if to_receive == 'on':
           to_receive = True
        else:
            to_receive = False

        if party:
            # If 'party' exists, it's an update operation
            party.part_name = part_name
            party.gstin = gstin
            party.phone_number = phone_number
            party.gst_type = gst_type
            party.state = state
            party.email_id = email_id
            party.billing_address = billing_address
            party.opening_balance = opening_balance
            party.as_of_date = as_of_date
            party.to_pay = to_pay
            party.to_receive = to_receive
            party.save()
        

        return redirect('party')

    context = {
        'party': party
    }
    return render(request, 'accounts/edit/edit_party.html', context)


def add_smtp_server(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        host = request.POST.get('host')
        port = request.POST.get('port')
        username = request.POST.get('username')
        password = request.POST.get('password')

        SMTPServer.objects.create(
            name=name,
            host=host,
            port=port,
            username=username,
            password=password
        )
        return redirect('smtp')
    
    smtp_list = SMTPServer.objects.all()
    context ={
        'smtp_list':smtp_list
    }
    return render(request,'setting/smtp.html',context)

# def edit_smtp_server(request, server_id):
#     server = SMTPServer.objects.get(pk=server_id)

#     if request.method == 'POST':
#         form = SMTPServerForm(request.POST, instance=server)
#         if form.is_valid():
#             form.save()
#             return redirect('smtp_server_list')
#     else:
#         form = SMTPServerForm(instance=server)
    
#     return render(request, 'edit_smtp_server.html', {'form': form, 'server': server})



# def send_email(message_text,recipient,subject):
    
    
#     server = SMTPServer.objects.get(pk=1)

#         # Creating an SMTP connection
#     try:
#             smtp_connection = smtplib.SMTP(server.host, server.port)
#             smtp_connection.starttls()
#             smtp_connection.login(server.username, server.password)

#             # Composing the email
#             msg = MIMEMultipart()
#             msg['From'] = server.username
#             msg['To'] = recipient
#             msg['Subject'] = subject
#             msg.attach(MIMEText(message_text,'plain'))

#             # Sending the email
#             smtp_connection.sendmail(server.username, recipient, msg.as_string())
#             smtp_connection.quit()

#             return HttpResponse('Email sent successfully!')
#     except Exception as e:
#             return HttpResponse(f'Error sending email: {str(e)}')




def add_hospital(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        image = request.FILES.get('image')

        hosptial = header(
            name=name,
            image=image

        )
        
        hosptial.save()
        return redirect('doctor')

    return render(request, 'setting/add_hospital.html')



def search_patients(request):
    query = request.GET.get('q', '')

    if query:
        patients = Patient.objects.filter(name__icontains=query)
    else:
        patients = Patient.objects.all()

    # Create a list of patient data
    patient_data = [
        {
            'name': patient.name,
            'date_of_birth': patient.date_of_birth.strftime('%Y-%m-%d'),
            'phone': patient.phone,
        }
        for patient in patients
    ]

    # Return the patient data as JSON
    return JsonResponse({'patients': patient_data})




def edit_staff(request, id):
    staff = get_object_or_404(AddStaff, id=id)
    

    if request.method == 'POST':
        # Update the staff information based on the POST data
        staff.role = request.POST.get('role')
        staff.designation = request.POST.get('designation', '')
        staff.department = request.POST.get('department', '')
        staff.specialist = request.POST.get('specialist', '')
        staff.first_name = request.POST.get('first_name', '')
        staff.last_name = request.POST.get('last_name', '')
        staff.father_name = request.POST.get('father_name', '')
        staff.mother_name = request.POST.get('mother_name', '')
        staff.gender = request.POST.get('gender', '')
        staff.marital_status = request.POST.get('marital_status', '')
        staff.blood_group = request.POST.get('blood_group', '')
        staff.date_of_birth = request.POST.get('date_of_birth', '')
        staff.date_of_joining = request.POST.get('date_of_joining', '')
        staff.phone = request.POST.get('phone')
        staff.emergency_contact = request.POST.get('emergency_contact', '')
        staff.email = request.POST.get('email')
        staff.current_address = request.POST.get('current_address', '')
        staff.permanent_address = request.POST.get('permanent_address', '')
        staff.photo = request.FILES.get('photo')

        staff.qualification = request.POST.get('qualification', '')
        staff.work_experience = request.POST.get('work_experience', '')
        staff.specialization = request.POST.get('specialization', '')
        staff.note = request.POST.get('note', '')

        staff.pan_number = request.POST.get('pan_number', '')
        staff.national_id_number = request.POST.get('national_id_number', '')
        staff.local_id_number = request.POST.get('local_id_number', '')

 
        staff.epf_no = request.POST.get('epf_no', '')
        basic_salary = request.POST.get('basic_salary', 0)
        try:
            staff.basic_salary = float(basic_salary)
        except ValueError:
            staff.basic_salary = 0

        staff.contract_type = request.POST.get('contract_type', '')

        staff.work_shift = request.POST.get('work_shift', '')
        staff.work_location = request.POST.get('work_location', '')

        if 'paid_leave' in request.POST:
            staff.paid_leave = True
        else:
            staff.paid_leave = False

        number_of_leaves = request.POST.get('number_of_leaves')
        try:
            staff.number_of_leaves = float(number_of_leaves)
        except ValueError:
            staff.number_of_leaves = 0

        staff.account_title = request.POST.get('account_title', '')
        staff.bank_account_no = request.POST.get('bank_account_no', '')
        staff.bank_name = request.POST.get('bank_name', '')
        staff.ifsc_code = request.POST.get('ifsc_code', '')
        staff.bank_branch_name = request.POST.get('bank_branch_name', '')

        staff.facebook_url = request.POST.get('facebook_url', '')
        staff.twitter_url = request.POST.get('twitter_url', '')
        staff.linkedin_url = request.POST.get('linkedin_url', '')
        staff.instagram_url = request.POST.get('instagram_url', '')

        staff.resume = request.FILES.get('resume')
        staff.joining_letter = request.FILES.get('joining_letter')
        staff.other_documents = request.FILES.get('other_documents')

        staff.save()  # Save the changes to the database
        
        return redirect('/hr/list/')  # Redirect to the staff list page or another appropriate page
    

    role = Role.objects.all()
    context = { 
           "role":role, 
           'staff':staff,

        }
    return render(request, 'hr/edit_staff.html',context)



def user_logout(request):
    # user = CustomUser.objects.get(id=id)
    logout(request)
    return redirect('login') 



def get_header_data(request):
    header_data = header.objects.first()  # Assuming you have only one record in the header model
    print(header_data.image.url)
    if header_data:
        data = {
            'name': header_data.name,
            'image': header_data.image.url,
        }
        return JsonResponse(data)
    return JsonResponse({'error': 'No header data found'}, status=404)


def get_bed_data(request):
    bed_data = Bed.objects.all()  # Fetch all records from the Bed model
    data_list = []

    for bed in bed_data:
        ipd = IpdPatient.objects.filter(bed=bed).first()  # Assuming a ForeignKey relationship from IpdPatient to Bed

        if ipd:
            data_list.append({
                'name': bed.name,
                'ipd_bed_number': ipd.bed_number,
                'ipd_id': ipd.id,
                # Add more fields here if needed
            })
        else:
            # Handle the case where no related IpdPatient is found for the bed
            data_list.append({
                'name': bed.name,
                'ipd_bed_number': None,
                'ipd_id': None,
                # Add more fields here if needed
            })
        data = data_list
    if data_list:
        return JsonResponse(data, safe=False)
    return JsonResponse({'error': 'No bed data found'}, status=404)


# def get_ads_data(request):
#     ads_data = Ads.objects.all() 
#      # Assuming you have only one record in the header model
#     ads_list = []
#     print(ads_data)

#     for ad in ads_data:
#         ads_list.append({
# #               # Include the ID if needed
#             'image': ad.ads.url if ad.ads else '',
# #             # Add other fields you want to include in the JSON
#         })

#     data = {
#         'ads': ads_list,
#     }
#     if ads_data:
#         data = {
         
#             'image': ads_data.ads.url,
#         }
#         return JsonResponse(data)
#     return JsonResponse({'error': 'No header data found'}, status=404)



def get_ads_data(request):
    ads_data = Ads.objects.all()
    ads_list = []

    for ad in ads_data:
        ads_list.append({
              # Include the ID if needed
            'image': ad.ads.url if ad.ads else '',
            # Add other fields you want to include in the JSON
        })

    data = {
        'ads': ads_list,
    }

    return JsonResponse(data, safe=False)

def add_ads(request):

    if request.method == 'POST':
    
        image = request.FILES.get('image')

        ads = Ads(
            
            ads=image

        )
        
        ads.save()
        return redirect('doctor')
    ads = Ads.objects.all()
    context ={
        'img':ads
    }
    return render(request, 'setting/ads.html',context)



def edit_ads(request,id):
    ad = Ads.objects.get(id=id)


    if request.method == 'POST':
    
        image = request.FILES.get('image')

        
        
        ad.ads=image
        ad.save()
        return redirect('add_ads')
    
    context ={
        'img':ad
    }
    return render(request, 'setting/edit_ads.html',context)









def admin_notice_board(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        date = request.POST.get('date')
        notice = Notice(title=title, content=content,timestamp=date)
        notice.save()
        # message = 'New Notice By Admin: {}'.format(title)
        # channel_layer = get_channel_layer()
        # async_to_sync(channel_layer.group_send)(
        #     'notifications_group',
        #     {'type': 'send_notification', 'message': message}
        # )
        return redirect('admin_notice')  # Redirect to the same page after adding a notice

    if request.method == 'GET' and 'delete' in request.GET:
        notice_id = request.GET['delete']
        notice = Notice.objects.get(pk=notice_id)
        notice.is_deleted = True
        notice.save()

    notices = Notice.objects.filter(is_deleted=False)
    notice = Notice.objects.filter(is_deleted=True).delete()
 
    return render(request, 'panels/notice.html', {'notices': notices})

def public_notice_board(request):
    notices = Notice.objects.all()
    return render(request, 'panels/public_notice.html', {'notices': notices})



# def send_message(request, receiver_id):
#     if request.method == 'POST':
#         content = request.POST['content']
#         receiver = AddStaff.objects.get(pk=receiver_id)
#         Message.objects.create(sender=request.user, receiver=receiver, content=content)
#         return redirect('message_list')

#     receiver = AddStaff.objects.get(pk=receiver_id)
#     return render(request, 'messaging/send_message.html', {'receiver': receiver})


# def message_list(request):
#     user_messages = Message.objects.filter(receiver=request.user).order_by('-timestamp')
#     return render(request, 'messaging/message_list.html', {'user_messages': user_messages})


def calculator_view(request):
    return render(request, 'others/calculator.html')



from .models import ChatRoom, ChatMessages
@login_required(login_url='/login')
def chat_room(request, room_name):

    user = CustomUser.objects.all()
    context = {
        'all': user,
        
    }

    return render(request, 'chat/room.html', context)

def send_message(request,receiver_id,sender_id):
    if request.method =="POST":
        message = request.POST['message']

        receiver = CustomUser.objects.get(id=receiver_id)
        sender = CustomUser.objects.get(id=sender_id)

        message = ChatMessages(receiver=receiver, sender=sender, content=message)
        message.save()
        url = reverse('send', args=[receiver_id,sender_id])
        

        return redirect(url)
    messges = ChatMessages.objects.filter(receiver=receiver_id,sender=sender_id)
    name = CustomUser.objects.get(id=receiver_id)
    user = CustomUser.objects.all()
    
    received_message = ChatMessages.objects.filter(receiver=sender_id,sender=receiver_id)
    context = {
        'receiver':receiver_id,
        'message':messges,
        'receiver_name':name.username,
        'all': user,
        'received_message':received_message,

    }
    return render(request,'chat/chat.html',context)


def chat_list(request):
  
    messges = ChatMessages.objects.all()
    context ={
        'message':messges
    }
    return render(request,'chat/message.html',context)



def send_email(request,email,messages):  
    
    time.sleep(3)
    with get_connection(  
           host=settings.EMAIL_HOST, 
     port=settings.EMAIL_PORT,  
     username=settings.EMAIL_HOST_USER, 
     password=settings.EMAIL_HOST_PASSWORD, 
     use_tls=settings.EMAIL_USE_TLS  
       ) as connection:  
           subject = "Account Password"
           from_email = "info@phoneixhms.com"
           recipient_list = [email]  
           message =messages
           send_mail(subject, message, from_email, recipient_list, connection=connection)



def deletestaff(request,user_id):
    user = CustomUser.objects.get(id=user_id)
    staff = AddStaff.objects.get(staff_id=user_id)
    staff.delete()
    user.delete()

    return redirect('staff_list')



def pos(request):
    products = Item_Acc.objects.all()
    product_json = []
    for product in products:
        product_json.append({'id':product.id, 'name':product.item_name, 'price':float(product.sale_price)})
    context = {
        'page_title' : "Point of Sale",
        'products' : products,
        'product_json' : json.dumps(product_json)
    }
    # return HttpResponse('')
    return render(request, 'accounts/pos.html',context)
    


def add_to_cart(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        product = Item_Acc.objects.get(pk=product_id)

        if 'cart' not in request.session:
            request.session['cart'] = []

        # Add the selected item to the cart
        request.session['cart'].append({
            'product_id': product.id,
            'product_name': product.name,
            'quantity': 1,
            'item_total': float(product.price),
        })

        # Calculate order summary
        cart = request.session['cart']
        total = sum(item['item_total'] for item in cart)
        tax_rate = 0.08
        tax = total * tax_rate
        grand_total = total + tax

        return JsonResponse({
            'cart_items': render_cart_items(cart),
            'total': total,
            'tax': tax,
            'grand_total': grand_total,
        })

def remove_from_cart(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')

        # Remove the selected item from the cart
        if 'cart' in request.session:
            request.session['cart'] = [item for item in request.session['cart'] if item['product_id'] != product_id]

        # Calculate order summary
        cart = request.session['cart']
        total = sum(item['item_total'] for item in cart)
        tax_rate = 0.08
        tax = total * tax_rate
        grand_total = total + tax

        return JsonResponse({
            'cart_items': render_cart_items(cart),
            'total': total,
            'tax': tax,
            'grand_total': grand_total,
        })

def render_cart_items(cart):
    # Create an HTML string for the cart items
    cart_html = ""
    for item in cart:
        cart_html += f"<tr>"
        cart_html += f"<td>{item['product_name']}</td>"
        cart_html += f"<td>{item['quantity']}</td>"
        cart_html += f"<td>${item['item_total']:.2f}</td>"
        cart_html += f"<td><button class='remove-from-cart' data-product-id='{item['product_id']}'>Remove</button></td>"
        cart_html += f"</tr>"
    return cart_html


def receipt(request):
    id = request.GET.get('id')
    sales = AppointmentDetails.objects.filter(id = id).first()
   

    return render(request, 'posApp/receipt.html')
    

stripe.api_key = settings.STRIPE_SECRET_KEY

@login_required
def add_funds(request):
    if request.method == 'POST':
        amount = request.POST['amount']
        amount_in_cents = int(float(amount) * 100)

        # Create a payment intent using Stripe
        intent = stripe.PaymentIntent.create(
            amount=amount_in_cents,
            currency='inr',
            metadata={'user_id': request.user.id},
        )

        return render(request, 'wallet/add_funds.html', {'client_secret': intent.client_secret})

    return render(request, 'wallet/add_funds.html')

@login_required
def make_payment(request):
    if request.method == 'POST':
        amount = request.POST['amount']
        amount_in_cents = int(float(amount) * 100)
        user = request.user

        # Charge the user using Stripe
        charge = stripe.Charge.create(
            amount=amount_in_cents,
            currency='usd',
            source=request.POST['stripeToken'],
            description='Payment from Wallet',
        )

        # Update the user's wallet balance
        wallet = Wallet.objects.get(user=user)
        wallet.balance -= amount_in_cents / 100
        wallet.save()

        # Create a transaction record
        Transaction.objects.create(user=user, amount=-amount_in_cents / 100)

        return redirect('wallet_balance')

    return render(request, 'wallet/make_payment.html')



def dashboard(request):
    wallet = Wallet.objects.get(user=request.user)
    context = {'wallet': wallet}
    return render(request, 'wallet/dashboard.html', context)

def download(request):
    if request.method == 'GET':
        appointment_id = request.GET.get('id')
        # Replace this with your logic to fetch data based on the appointment_id
        # Example: Fetch data from your database

        appointment_det = AppointmentDetails.objects.get(id=appointment_id)
        hospital_name = header.objects.all().first()
        appointment_data = {
            
            'name':appointment_det.appointment_date,
            'hospital_name':hospital_name.name if hospital_name else 'Your Hospital',
            'phone':appointment_det.phone,
            'doctor':appointment_det.doctor,
            'patient':appointment_det.patient_name,
            'gender':appointment_det.gender,
            

            'other_data': 'Your fetched data here',
        }

        return JsonResponse(appointment_data)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)
    



def download_IPD(request):
    if request.method == 'GET':
        appointment_id = request.GET.get('id')
        # Replace this with your logic to fetch data based on the appointment_id
        # Example: Fetch data from your database

        ipd_patient = IpdPatient.objects.get(id=appointment_id)
        hospital_name = header.objects.all()
        appointment_data = {
            
            'name':ipd_patient.patient.name,
            'hospital_name':hospital_name.name if hospital_name else 'Your Hospital',
            'phone':ipd_patient.patient.phone,
            'doctor':ipd_patient.consultant_doctor,
            'bed':ipd_patient.bed_number,
            'gender':ipd_patient.patient.gender,
            

            'other_data': 'Your fetched data here',
        }

        return JsonResponse(appointment_data)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)
    


def item_list(request):
    items = Item_Acc.objects.all()
    medicine = Purchase.objects.all()
    category = Med_Category.objects.all()
    doctor = AddStaff.objects.filter(role="Doctor")


    context={
        'items':items,
        'medicine':medicine,
        'category':category,
        'doctor':doctor,
    }
    return render(request, 'pos/pos_home.html',context)



def pos_pharma(request):
    items = Item_Acc.objects.all()
    medicine = Purchase.objects.all()
    category = Med_Category.objects.all()
    composition = Medicine_Composition.objects.all()
    doctor = AddStaff.objects.filter(role="Doctor")


    context={
        'items':items,
        'medicine':medicine,
        'category':category,
        'doctor':doctor,
        'composition':composition,
    }
    return render(request, 'pos/pos_pharma.html',context)


def add_to_cart(request, item_id):
    item = Item_Acc.objects.get(id=item_id)
    cart = request.session.get('cart', [])
    cart.append(item.sale_price)
    request.session['cart'] = cart
    return redirect('item_list')

def view_cart(request):
    cart = request.session.get('cart', [])
    total = sum(cart)
    return render(request, 'pos/pos_checkout.html', {'cart': cart, 'total': total})


def create_liablity(request):
    if request.method == "POST":
        name = request.POST.get("name")
        description = request.POST.get("description")
        price = request.POST.get("price")
        liablity_type = request.POST.get("liablity_type")
        liablity = Liablity(name=name, description=description,liablity_type=liablity_type, price=price,)
        liablity.save()
        return redirect("create_liablity")  # Redirect to a list view of assets
    liablity = Liablity.objects.all()
    context={
        'liablity':liablity,
    }
    return render(request, "accounts/create_liablity.html",context)



def IPD_pdf(request,id):

    ipd_patient = IpdPatient.objects.get(id=id)
    hospital_name = header.objects.all().first()
    address = Address.objects.all()
    date = datetime.now()
   

        

        
    context = {
                'id': ipd_patient.id,
                'name': ipd_patient.patient.name,
                'hospital_name': hospital_name.name if hospital_name else 'Your Hospital',
                'phone': ipd_patient.patient.phone,
                'address':address,
                'height':ipd_patient.height,
                'weight':ipd_patient.weight,
                'age':ipd_patient.patient.Age,
                'admission_date':ipd_patient.admission_date,
                'date':date,
                'doctor': ipd_patient.consultant_doctor,
                'bed': ipd_patient.bed_number,
                'gender': ipd_patient.patient.gender,
        }

    template = get_template('templat/ipd_pdf.html')
    html = template.render(context)

    # Create a response object with PDF content type
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="ipd.pdf"'

    # Generate PDF from HTML using ReportLab and pisa
    pisa_status = pisa.CreatePDF(html, dest=response)

    # Return the response
    if pisa_status.err:
            return HttpResponse('PDF generation failed', content_type='text/plain')
    
    return response
    





def OPD_pdf(request,id):
    ipd_patient = OpdPatient.objects.get(id=id)
    hospital_name = header.objects.all().first()
   

    context = {
            'id':ipd_patient.id,
            'name':ipd_patient.patient.name,
            'hospital_name':hospital_name.name if hospital_name else 'Your Hospital',
            'phone':ipd_patient.patient.phone,
            'doctor':ipd_patient.consultant_doctor,
            
            'gender':ipd_patient.patient.gender,
        }
    template = get_template('templat/opd_pdf.html')
    html = template.render(context)

    # Create a response object with PDF content type
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="opd.pdf"'

    # Generate PDF from HTML using ReportLab and pisa
    pisa_status = pisa.CreatePDF(html, dest=response)

    # Return the response
    if pisa_status.err:
        return HttpResponse('PDF generation failed', content_type='text/plain')
    
    return response


  

def pos_pdf(request):
    if request.method == 'POST':
        
        sub_total = request.POST.get('sub_total')
        tax = request.POST.get('tax')
        grand_total = request.POST.get('grand_total')
        discount = request.POST.get('disc')
        small_note = request.POST.get('small_note')
        date_time = request.POST.get('date_time')
        medicine_composition = request.POST.get('medicine_composition')
        payment = request.POST.get('payment')
        patient = request.POST.get('patient')
        doctor = request.POST.get('doctor')
        paid_amount = request.POST.get('paid_amount')
        
        item_counter = request.POST.get('item_counter')

        pos = POS(
            doctor = doctor,
            payment_mode=payment,
            date=date_time,
            composition=medicine_composition,
            small_note=small_note,
            tax_percent=tax,
            discount_percent=discount,
            







        )
        pos.save()
        print(item_counter)
        if item_counter.isdigit():
            item_counter = int(item_counter)
        else:
            item_counter = 0

        product_list = []
        
        for i in range(1, item_counter + 1):
            
            
            print(item_counter)
            item = request.POST.get(f'med_{i}')
            qty = int(request.POST.get(f'qty_{i}'))
            available = int(request.POST.get(f'available_{i}'))


            
            if available < qty:
                return HttpResponse('Error: Insufficient available quantity.')

            
            
            
            medicines_ids = [int(id) for id in re.findall(r'\d+', item)]

            print(medicines_ids)
            for medicines_id in medicines_ids:
        
                stock = get_object_or_404(Stock, medicine=medicines_id)
                updated_available_quantity = available - qty
                print(updated_available_quantity)
                stock.stock = updated_available_quantity
                stock.save()
                print(stock.stock)

            cat = request.POST.get(f'cat_{i}')
            items = re.sub(r'\d', '',item)
            item  = items.replace("_", "")
            price = request.POST.get(f'price_{i}')
            expiry = request.POST.get(f'expiry_{i}')
            batch = request.POST.get(f'batch_{i}')
            tax_ = request.POST.get(f'tax_{i}')

            total = request.POST.get(f'total_{i}')
           
            
            product = {
                'item': item,
                'quantity': qty,
                'price': price,
                'tax_':tax_,
                'expiry':expiry,
                'batch':batch,
                'cat':cat,
                
                'total': total
                }
    
            print(product)
            product_list.append(product)
        print(product_list)

        
      
    hospital = header.objects.all().first()
    address = Address.objects.all().first()
    context= {
        'products':product_list,
        'sub_total':sub_total,
        'tax':tax,
        'hospital':hospital,
        'patient':patient,
        'discount':discount,
        'address':address,
        'small_note':small_note,
                'date_time':date_time,
                'composition':medicine_composition,
                'doctor':doctor,
                'payment':payment,
                'paid_amount':paid_amount,
        'grand_total':grand_total,
    }

    template = get_template('templat/pos_pdf.html')
    html = template.render(context)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="invoice.pdf"'

    # Generate PDF from HTML using ReportLab and pisa
    pisa_status = pisa.CreatePDF(html, dest=response)

    # Return the response
    if pisa_status.err:
        return HttpResponse('PDF generation failed', content_type='text/plain')
    return response






def path_details(request):
    selected_value = request.GET.get('id')
    
    
    
    try:
        test = Pathology_test.objects.get(id=selected_value)
        
      


        data = {
            'success': True,
            'price':test.amount,
            'tax':test.tax_percentage,
   
            
        }
    except Pathology_test.DoesNotExist:
        data = {
            'success': False,
            'message': 'Details not found for the given Case ID.',
        }
    return JsonResponse(data)
def radio_details(request):
    selected_value = request.GET.get('id')
    
    
    
    try:
        test = Radiology.objects.get(id=selected_value)
        
      


        data = {
            'success': True,
            'price':test.test_name.amount,
            'tax':test.test_name.tax_percentage,
   
            
        }
    except Radiology.DoesNotExist:
        data = {
            'success': False,
            'message': 'Details not found for the given Case ID.',
        }
    return JsonResponse(data)

def Medicine_Details(request):
    selected_value = request.GET.get('id')
    
    
    
    try:
        items = Purchase.objects.get(id=selected_value)
        quantity = Stock.objects.get(medicine=selected_value)
        
      
        # for item in items:    
        #     item_data = item['name']
        #     item_list.append(item_data)


        data = {
            'success': True,
            'price':items.sale_price,
            'tax':items.tax_percentage,
            'batch':items.batch_no,
            'quantity':quantity.stock,
            'expiry':items.expiry_date,
       
            
        }


    
    except Purchase.DoesNotExist:
        data = {
            'success': False,
            'message': 'Details not found for the given Case ID.',
        }
    return JsonResponse(data)




def Med_det(request):
    selected_value = request.GET.get('id')
    

    
    
    try:
        item = Purchase.objects.get(id=selected_value)
        
        data = {
            'success': True,
            'expiry':item.expiry_date,
            'tax': item.tax_percentage,
            'price':item.sale_price,
            'batch_no':item.batch_no,
            'quantity':item.quantity,



       
            
        }
    except Purchase.DoesNotExist:
        data = {
            'success': False,
            'message': 'Details not found for the given Case ID.',
        }
    return JsonResponse(data)



def search_OPDBalance(request):
    if request.method == 'GET':
        
        from_age = request.GET.get('from_age')
        to_age = request.GET.get('to_age')
        gender = request.GET.get('gender')
        time_duration = request.GET.get('time_duration')
        
        # discharged = request.GET.get('discharged')


        if not time_duration:
            time_duration = 7

        if not from_age:
            from_age = 0

        if not to_age:
            to_age =100

        start_date = datetime.now() - timedelta(days=int(time_duration))
        if not gender:
            
            patient = OpdPatient.objects.filter(
            patient__Age__gt=from_age,
            patient__Age__lt=to_age,
            
        )
            
        else:
            patient = OpdPatient.objects.filter(
            admission_date__gte=start_date,
            patient__Age__gt=from_age,
            patient__Age__lt=to_age,
            patient__gender=gender,
        )
            

        
        

        opd_results_list = list(patient.select_related('patient').values())

        balances =[]
        for opd in opd_results_list:
            balance = opd['amount'] - opd['paid_amount']
            balances.append(balance)
      
        
        
       
        context = {
            'results': patient,
            'balances':balances
           
            }

        return render(request, 'reports/opd_balance.html', context )

    # Handle other HTTP methods if needed
    return render(request, 'reports/opd_balance.html')



def search_IPDBalance(request):
    if request.method == 'GET':
        
        from_age = request.GET.get('from_age')
        to_age = request.GET.get('to_age')
        gender = request.GET.get('gender')
        time_duration = request.GET.get('time_duration')
        
        # discharged = request.GET.get('discharged')


        if not time_duration:
            time_duration = 7

        if not from_age:
            from_age = 0

        if not to_age:
            to_age =100

        start_date = datetime.now() - timedelta(days=int(time_duration))
        if not gender:
            
            patient = IpdPatient.objects.filter(
            patient__Age__gt=from_age,
            patient__Age__lt=to_age,
            
        )
            
        else:
            patient = IpdPatient.objects.filter(
            admission_date__gte=start_date,
            patient__Age__gt=from_age,
            patient__Age__lt=to_age,
            patient__gender=gender,
        )
            
        

        
        
        
        
        
       
        context = {
            'results': patient,
        
            }

        return render(request, 'reports/ipd_balance.html', context )

    # Handle other HTTP methods if needed
    return render(request, 'reports/ipd_balance.html')



def stock_report(request):
    medicine = Purchase.objects.all()

    context ={
        'medicine':medicine
    }

    return render(request,'reports/inventory_stock.html',context)


def death_report(request):

    if request.method == 'GET':

        gender = request.GET.get('gender')
        time_duration = request.GET.get('time_duration')
        
        if not time_duration:
            time_duration = 7

        start_date = datetime.now() - timedelta(days=int(time_duration))

        if not gender:
            
            death  = DeathRecord.objects.filter(
                death_date=start_date
            
        )
            
        else:
            death = DeathRecord.objects.filter(
            death_date__gte=start_date,
            
            patient_name__gender=gender,
        )
        
        context = {
          'death':death,
        }
        return render(request, 'reports/death.html',context)
    return render (request,'reports/death.html',context)




def birth_report(request):

    if request.method == 'GET':

        gender = request.GET.get('gender')
        time_duration = request.GET.get('time_duration')
        
        if not time_duration:
            time_duration = 7

        start_date = datetime.now() - timedelta(days=int(time_duration))

        if not gender:
            
            birth  = ChildBirth.objects.filter(
                birth_date=start_date
            
        )
            
        else:
            birth = ChildBirth.objects.filter(
            birth_date__gte=start_date,
            
            gender=gender,
        )
        
        context = {
          'birth':birth,
        }
        return render(request, 'reports/birth.html',context)
    return render (request,'reports/birth.html',context)


def discharge(request):
    if request.method =='POST':
        patient = request.POST.get('patient')
        room = request.POST.get('room')
        status = request.POST.get('status')

        if room == 'IPD':
            ipd = IpdPatient.objects.get(patient=patient)
            if ipd:
                ipd.discharged_status = True
                ipd.discharged = status
                ipd.save()
        
        elif room=='OPD':
            opd = OpdPatient.objects.get(patient=patient)

            if opd:
                opd.discharged_status = True
                opd.discharged = status
                opd.save()
        
        return redirect('discharged_patient')
    ipd_discharge = IpdPatient.objects.filter(discharged_status=True)
    opd_discharge = OpdPatient.objects.filter(discharged_status=True)
    patient_ipd = IpdPatient.objects.all()
    patient_opd = OpdPatient.objects.all()
    context ={
        'ipd':ipd_discharge,
        'opd':opd_discharge,
        'patient_ipd':patient_ipd,
        'patient_opd':patient_opd,
    }
    return render(request,'patient/discharged.html',context)


def ipd_discharge(request):
    if request.method == 'GET':
        
        from_age = request.GET.get('from_age')
        to_age = request.GET.get('to_age')
        gender = request.GET.get('gender')
        time_duration = request.GET.get('time_duration')
        status = request.GET.get('status')
        # discharged = request.GET.get('discharged')


        if not time_duration:
            time_duration = 7

        if not from_age:
            from_age = 0

        if not to_age:
            to_age =100

        start_date = datetime.now() - timedelta(days=int(time_duration))
        if not gender:
            
            patient = IpdPatient.objects.filter(
            patient__Age__gt=from_age,
            patient__Age__lt=to_age,
            discharged = status,
            
        )
            
        else:
            patient = IpdPatient.objects.filter(
            admission_date__gte=start_date,
            patient__Age__gt=from_age,
            patient__Age__lt=to_age,
            patient__gender=gender,
            discharged = status,
        )
            
        

        
        
        
        
        
       
        context = {
            'results': patient,
        
            }

        return render(request, 'reports/ipddischarge_report.html', context )

    # Handle other HTTP methods if needed
    return render(request, 'reports/ipddischarge_report.html')



def opd_discharge(request):
    if request.method == 'GET':
        
        from_age = request.GET.get('from_age')
        to_age = request.GET.get('to_age')
        gender = request.GET.get('gender')
        time_duration = request.GET.get('time_duration')
        status = request.GET.get('status')
        # discharged = request.GET.get('discharged')


        if not time_duration:
            time_duration = 7

        if not from_age:
            from_age = 0

        if not to_age:
            to_age =100

        start_date = datetime.now() - timedelta(days=int(time_duration))
        if not gender:
            
            patient = OpdPatient.objects.filter(
            patient__Age__gt=from_age,
            patient__Age__lt=to_age,
            discharged = status,
            
        )
            
        else:
            patient = OpdPatient.objects.filter(
            admission_date__gte=start_date,
            patient__Age__gt=from_age,
            patient__Age__lt=to_age,
            patient__gender=gender,
            discharged = status,
        )
            
        

        
        
        
        
        
       
        context = {
            'results': patient,
        
            }

        return render(request, 'reports/opddischarge.html', context )

    # Handle other HTTP methods if needed
    return render(request, 'reports/opddischarge.html')




def refferal_report(request):
    if request.method == 'GET':
        
        payee = request.GET.get('payee')
        patient_type = request.GET.get('patient_type')
        patient = request.GET.get('patient')
        # discharged = request.GET.get('discharged')


        if not patient_type:
            refferal = Referral.objects.filter(
            payee=payee,
            patient = patient
        )
        elif not patient:
            refferal = Referral.objects.filter(
            payee=payee,
            patient_type=patient_type,
        )
        else:
            refferal = Referral.objects.filter(
            payee=payee,
            patient_type=patient_type,
            patient=patient,
        )
        
            
        
        

        
            
        

        
        
        
        
        
        payee= ReferralPerson.objects.all()       
        patient = Patient.objects.all()    
        context = {
            'results': refferal,
            'payee':payee,
            'patient':patient,
        
            }

        return render(request, 'reports/refferal.html', context )

    # Handle other HTTP methods if needed
    return render(request, 'reports/refferal.html')





def ambulance_report(request):
    if request.method == 'GET':
        vechile = request.GET.get('vechile')
        print(vechile)
        ambulance = Ambulance.objects.filter(
            vehicle_model = vechile,

        )

        print(ambulance)
        model = Ambulance.objects.all()

        context = {
            'ambulance':ambulance,
            'model':model,
        
        }

        return render(request,'reports/ambulance.html',context)

        
    model = Ambulance.objects.all()

    context = {
        'model':model,
    }
    return render(request,'reports/ambulance.html',context)


def prescription(request,id):
    if request.method == 'POST':
        # Retrieve data from the form
        finding_category = request.POST.get('finding_category')
        findings = request.POST.get('findings')
        finding_description = request.POST.get('finding_description')
        doctor = request.POST.get('doctor')
        radiology = request.POST.get('radiology')
        pathology = request.POST.get('pathology')
        
        
        
        
        item_counter = request.POST.get('item_counter', 0)
        
        

        
        
        if item_counter.isdigit():
            item_counter = int(item_counter)
        else:
            item_counter = 0    
        
        ipd = IpdPatient.objects.get(pk=id)

        patient = Patient.objects.get(id=ipd.patient.id)
        radio = Radiology.objects.get(id=radiology)
        
        try:
            path  = Pathology.objects.get(id=pathology)
        except Exception:
            path = None

        try:
            radio = Radiology.objects.get(id=radiology)
        except Exception:
            radio = None


        pres =Precreption (
            patient=patient,
            finding_category=finding_category,
            findings=findings,
            finding_description=finding_description,
            doctor=doctor,
            pathology =path,
            radiology=radio,
           
        )
        

        pres.save()
        id_item = Precreption.objects.get(id=pres.id)
        total_all_products =0

        for i in range(1, item_counter + 1):
            
            medicine_category = request.POST.get(f'medicine_category_{i}')
            
            medicine_categorys = re.sub(r'\d', '',medicine_category)
            medicine_category  = medicine_categorys.replace("_", "")



            medicine = request.POST.get(f'medicine_{i}')
            medicines = re.sub(r'\d', '',medicine)
            medicine  = medicines.replace("_", "")

            dosage = request.POST.get(f'dosage_{i}')

            dosages = re.sub(r'\d', '',dosage)
            dosage  = dosages.replace("_", "")

            dose_interval = request.POST.get(f'dose_interval_{i}')
            dose_intervals = re.sub(r'\d', '',dose_interval)
            dose_interval  = dose_intervals.replace("_", "")

            dose_duration = request.POST.get(f'duration_{i}')
            dose_durations = re.sub(r'\d', '',dose_duration)
            dose_duration  = dose_durations.replace("_", "")


  
            item = Precreption_Item(
            
                pres=id_item,
                medicine_category=medicine_category,
                medicine=medicine,
                dosage=dosage,
                does_interval =dose_interval,
                dose_duration=dose_duration,
               

                


            )
            
            item.save()
            

        
        return redirect('ipd_patient')

    dosage = Med_Details.objects.all()
    cat = Med_Category.objects.all()
    doctor = AddStaff.objects.filter(role="Doctor")
    medicine = Medicine.objects.all()
    ipd = IpdPatient.objects.get(pk=id)
    radio = Radiology.objects.filter(patient=ipd.patient)
    path = Pathology.objects.filter(patient=ipd.patient)
  


   
    
    context = {
        'path':path,
        'radio':radio,
        'dosage':dosage,
        'ipd':id,
        'cat':cat,
        'medicine':medicine,
        'doctor':doctor,
    } 

    
    

    return render(request, 'patient/prescreption.html',context)


    


def blood_donor_report(request):
    if request.method == 'GET':
        gender = request.GET.get('gender')
        blood_donor = request.GET.get('blood_donor')
        blood_group = request.GET.get('blood_group')
        
        if not gender:

            blood_donation = BloodDonation.objects.filter(
                donor_name = blood_donor,
                donor_name__blood_group = blood_group,

            )

        elif not blood_group:
            blood_donation = BloodDonation.objects.filter(
                donor_name = blood_donor,
                donor_name__gender=gender

            )

        elif not blood_group and not blood_donor:
             blood_donation = BloodDonation.objects.filter(
                
                donor_name__gender=gender

            )
        else:

            blood_donation = BloodDonation.objects.filter(
                donor_name = blood_donor,
                donor_name__gender=gender,
                donor_name__blood_group = blood_group,

            )

      
        donor = Donor_det.objects.all()

        context = {
            'result':blood_donation,
            'model':donor,
        
        }

        return render(request,'reports/blood_donor.html',context)

        
    donor = Donor_det.objects.all()

    context = {
        'model':donor,
    }
    return render(request,'reports/blood_donor.html',context)



def blood_issue_report(request):
    if request.method == 'GET':
        gender = request.GET.get('gender')
        patient = request.GET.get('patient')
        blood_group = request.GET.get('blood_group')
        
        print(patient)
        print(blood_group)
        print(gender)
        if not patient and not gender:
            

            blood_donation = BloodDonation_component.objects.filter(
            
                blood_group=blood_group,

            )

        elif not blood_group:
            patient = Patient.objects.get(id=patient)
            blood_donation = BloodDonation_component.objects.filter(
                patient__gender=gender,


            )

        elif not blood_group and not patient:
             blood_donation = BloodDonation_component.objects.filter(
                
                patient__gender=gender

            )
        elif not patient and not blood_group and not gender:
            donor = Patient.objects.all()

            context = {
                'result':"No Result Found",
                'model':donor,
        
            }

            return render(request,'reports/blood_issue.html',context)
        else:
            patient = Patient.objects.get(id=patient)

            blood_donation = BloodDonation_component.objects.filter(
                patient = patient,
                patient__gender=gender,
                blood_group = blood_group,

            )

      
        donor = Patient.objects.all()

        context = {
            'result':blood_donation,
            'model':donor,
        
        }

        return render(request,'reports/blood_issue.html',context)

        
    donor = Patient.objects.all()

    context = {
        'model':donor,
    }
    return render(request,'reports/blood_issue.html',context)



def payroll_report(request):

    if request.method == 'GET':
        role = request.GET.get('role')
        month = request.GET.get('month')
        year = request.GET.get('year')
        
        if  month == "all":
            payroll = Payroll.objects.filter(
                staff__role= role,
                date__year=year,

            )
            


        else:
            payroll = Payroll.objects.filter(   
                staff__role= role,
                date__month=month,
                date__year=year,

            )

        print(payroll)
        role = Role.objects.all()
        context = {
            'result':payroll,
            'role':role,
        
        }

        return render(request,'reports/payroll.html',context)

        
    
    role = Role.objects.all()
    context={
        'role':role,
    }
    return render(request,'reports/payroll.html',context)






# def certificate(request,id):

    
    
#     try:
#         ipd = IpdPatient.objects.get(patient=id)
#     except ObjectDoesNotExist:
#         ipd = None

#     try:
#         opd = OpdPatient.objects.get(patient=id)
#     except ObjectDoesNotExist:
#         opd = None

#    if not ipd:


#     context = {
#             'id':opd.id,
            
#         }
#     template = get_template('templat/opd_pdf.html')
#     html = template.render(context)

#     # Create a response object with PDF content type
#     response = HttpResponse(content_type='application/pdf')
#     response['Content-Disposition'] = 'attachment; filename="opd.pdf"'

#     # Generate PDF from HTML using ReportLab and pisa
#     pisa_status = pisa.CreatePDF(html, dest=response)

#     # Return the response
#     if pisa_status.err:
#         return HttpResponse('PDF generation failed', content_type='text/plain')
    
#     return response







def pos_path(request):
    test = Pathology.objects.all()

    doctor = AddStaff.objects.filter(role="Doctor")


    context={
        'test':test,
  
        'doctor':doctor,
    }
    return render(request, 'pathalogy/pos_path.html',context)


def pos_pathalogy(request):
    test = Pathology.objects.all()

    doctor = AddStaff.objects.filter(role="Doctor")


    context={
        'test':test,
  
        'doctor':doctor,
    }
    return render(request, 'pathalogy/pos.html',context)






def pos_radio(request):
    test = Radiology.objects.all()

    doctor = AddStaff.objects.filter(role="Doctor")


    context={
        'test':test,
  
        'doctor':doctor,
    }
    return render(request, 'radiology/pos_radio.html',context)


def pos_radiology(request):
    test = Radiology.objects.all()
    doctor = AddStaff.objects.filter(role="Doctor")


    context={
        'test':test,
        'doctor':doctor,
    }
    return render(request, 'radiology/pos.html',context)




def visitors_details(request):
    id = request.GET.get('id')
    if id =='IPD':
        result = IpdPatient.objects.all()
        
    elif id=='OPD':
        result = OpdPatient.objects.all()
    
        

    else:
        result = OpdPatient.objects.all()

    patient_list = [{'id': patient.id, 'name': patient.patient.name, 'other_field': patient.height} for patient in result]
    data = {
        'patient':patient_list,
    }
    return JsonResponse(data)
    

  
  

def pos_pathpdf(request):
    if request.method == 'POST':
        
        sub_total = request.POST.get('sub_total')
        tax = request.POST.get('tax')

        
        grand_total = request.POST.get('grand_total')
        discount = request.POST.get('disc')
        small_note = request.POST.get('small_note')
        date_time = request.POST.get('date_time')
        bill_date = request.POST.get('bill_date')
        patient_address = request.POST.get('address')
        
        payment = request.POST.get('payment')
        patient = request.POST.get('patient')
        age = request.POST.get('Age')
        doctor = request.POST.get('doctor')
        paid_amount = request.POST.get('paid_amount')
        item_counter = request.POST.get('item_counter')
        print(item_counter)
        if item_counter.isdigit():
            item_counter = int(item_counter)
        else:
            item_counter = 0

        product_list = []
        
        for i in range(1, item_counter + 1):
            
            
            print(item_counter)

            test = request.POST.get(f'test_{i}')
            
            tests =  re.sub(r'_.*', '', test)

          
            test  = tests.replace("_", "")
           
            cat = request.POST.get(f'cat_{i}')
            cate = re.sub(r'\d', '',cat)

            cat  = cate.replace("_", "")
            price = request.POST.get(f'price_{i}')
           

            total = request.POST.get(f'total_{i}')
           
            
            product = {
                'test': test,
                'cat': cat,
                'price': price,
                'total': total
                }
    
            print(product)
            product_list.append(product)
        print(product_list)

        
      
    hospital_name = header.objects.all().first()
    address = Address.objects.all()
    
    context= {
        'products':product_list,
        'sub_total':sub_total,
        'hospital_name':hospital_name.name,
        'tax':tax,
        'address':address,
        'discount':discount,
        'patient_address':patient_address,
        'age':age,
        'bill_date':bill_date,
        
        'small_note':small_note,
        'date_time':date_time,
        'patient':patient,
        'paid_amount':paid_amount,
        'doctor':doctor,
        'payment':payment,
        'grand_total':grand_total,
    }

    template = get_template('templat/pos_path.html')
    html = template.render(context)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="invoice.pdf"'

    # Generate PDF from HTML using ReportLab and pisa
    pisa_status = pisa.CreatePDF(html, dest=response)

    # Return the response
    if pisa_status.err:
        return HttpResponse('PDF generation failed', content_type='text/plain')
    return response



def opd_dashboard(request,ipd_id):
    ipd = OpdPatient.objects.get(pk=ipd_id)
    nurse= NursingRecord.objects.all()
    staff = AddStaff.objects.filter(role="Nurse")
    doctor  = AddStaff.objects.filter(role="Doctor")
    medicine = MedicationDoseage.objects.all()
    consultant = Consultant_register.objects.all()
    operation = Operation.objects.all()

    dosage = Med_Details.objects.all()
    cat = Med_Category.objects.all()
    medicine_name = Medicine.objects.all()
    prep = Precreption.objects.all()

    pathology = Pathology.objects.filter(patient=ipd.patient)
    radiology = Radiology.objects.filter(patient=ipd.patient)
 
    payment = Ipd_Payments.objects.all()

    
    try:
        radiology_amount = Radiology.objects.get(patient=ipd_id).amount
        
    except Radiology.DoesNotExist:
        radiology_amount = 0
     

    context ={
        'nurse':nurse,
        'prep':prep,
        'staff':staff,
        'pathology':pathology,
        'radiology':radiology,
        'ipd':ipd,
        'doctor':doctor,
        'medicine':medicine,
        'dosage':dosage,
        'cat':cat,
        'medicine_name':medicine_name,
        'consultant':consultant,
        'operation':operation,
        'payment':payment,
        'radio':radiology_amount,
    }
    return render(request,'opd/dashboard.html',context)



def visitors(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        id_card = request.POST.get('id_card')
        purpose = request.POST.get('purpose')
        visit_to = request.POST.get('visit_to')
        patient = request.POST.get('patient')
    
        num_of_person = request.POST.get('num_of_person')
        date = request.POST.get('date')
        in_time = request.POST.get('in_time')
        out_time = request.POST.get('out_time')
        note = request.POST.get('note')
        document = request.FILES.get('document')

        
        record = Visitors(
            purpose=purpose,
            name=name,
            phone=phone,
            id_card=id_card,
            visit_to=visit_to,
            patient=patient,
            num_of_person=num_of_person,
            date=date,
            in_time=in_time,
            out_time=out_time,
            note=note,
            document=document,
        )

        record.save()
        visitor = Visitors.objects.all()
        context = {
            'visitors':visitor,
        }
        return render(request,'visitors/visit.html',context)
    visitor = Visitors.objects.all()
    context = {
        'visitors':visitor,
    }
    return render(request,'visitors/visit.html',context)
  


def postal_receive(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        reference_no = request.POST.get('reference_no', '')
        address = request.POST.get('address', '')
        note = request.POST.get('note', '')
        to_title = request.POST.get('to_title', '')
        date = request.POST.get('date', '')
        attach_document = request.FILES.get('attach_document')

        # Validate and save data
        
        receive = Postal_receive(
                title=title,
                reference_no=reference_no,
                address=address,
                note=note,
                to_title=to_title,
                date=date,
                attach_document=attach_document
            )
        receive.save()
        return redirect('postal_receive')
    postal = Postal_receive.objects.all()
    context = {
        'postal':postal,
    }
    return render(request,'postal/receive.html',context)



def postal_dispatch(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        reference_no = request.POST.get('reference_no', '')
        address = request.POST.get('address', '')
        note = request.POST.get('note', '')
        from_title = request.POST.get('to_title', '')
        date = request.POST.get('date', '')
        attach_document = request.FILES.get('attach_document')

      
        receive = Postal_dispatch(
                title=title,
                reference_no=reference_no,
                address=address,
                note=note,
                from_title=from_title,
                date=date,
                attach_document=attach_document
            )
        receive.save()
        return redirect('postal_dispatch')
    postal = Postal_dispatch.objects.all()
    context = {
        'postal':postal,
    }
    return render(request,'postal/dispatch.html',context)


def complain_type(request):
    if request.method == 'POST':
        name = request.POST.get('name')
    
        type = ComplainType(
            name=name,
        )
        type.save()
        return redirect('complain_type')
    type = ComplainType.objects.all()
    context = {
        'type':type,
    }
    return render(request,'complain/complain_type.html',context)



def complain_source(request):
    if request.method == 'POST':
        name = request.POST.get('name')
    
        source = Complain_source(
            name=name,
        )
        source.save()
        return redirect('complain_source')
    type = Complain_source.objects.all()
    context = {
        'type':type,
    }
    return render(request,'complain/complain_source.html',context)


def complain(request):
    if request.method == 'POST':
        complain_type = request.POST.get('complain_type', '')
        source = request.POST.get('source', '')
        complain_by = request.POST.get('complain_by', '')
        phone = request.POST.get('phone', '')
        date = request.POST.get('date', '')
        description = request.POST.get('description', '')
        action_taken = request.POST.get('action_taken', '')
        assigned = request.POST.get('assigned', '')
        note = request.POST.get('note', '')
        attach_document = request.FILES.get('attach_document')

        
        
        complain =Complain(
                complain_type=complain_type,
                source=source,
                complain_by=complain_by,
                phone=phone,
                date=date,
                description=description,
                action_taken=action_taken,
                assigned=assigned,
                note=note,
                attach_document=attach_document
            )
        complain.save()    
        return redirect('complain')
    complain_type = ComplainType.objects.all()
    complain_source = Complain_source.objects.all()
    complain = Complain.objects.all()
    context = {
        'complain':complain,
        'type':complain_type,
        "source":complain_source,
    }
    return render(request, 'complain/complain.html',context)


# def OT_Report(request):


#     return render(request,'')

def operation_name(request):
    if request.method == 'POST':
        name = request.POST.get('name')

        operation = Operation_name(
            name=name
        )
        operation.save()

        return redirect('operation_name')
    operation = Operation_name.objects.all()
    context = {
        'operation':operation,
    }
    return render(request,'operation/operation_name.html',context)

def operation_cate(request):
    if request.method=="POST":
        name = request.POST.get('name')
        
        operation = Operation_category(
            name=name,
        )
        operation.save()
        return redirect('operation_cate')
    operation = Operation_category.objects.all()
    context ={
        'operation':operation,
    }    
    return render(request,'operation/operation_category.html',context)


def ot_report(request):

    if request.method == 'GET':
        doctor_name = request.GET.get('doctor')
        category = request.GET.get('category')
        operation = request.GET.get('operation_name')
        year = request.GET.get('year')
        
        if  doctor_name == "doctor":
            result = Operation.objects.filter(
                operation_category= category,
                operation_name=operation,
                operation_date__year=int(year)

            )
            


        else:
            result = Operation.objects.filter(   
                operation_name=operation,
                operation_category=category,
                operation_date__year=year,
                consultant_doctor=doctor_name,

            )

        operation_category = Operation_category.objects.all()
        operation_name = Operation_name.objects.all()
        doctor = Operation.objects.all()
        context ={
            'operation_category':operation_category,
            'doctor':doctor,
            'operation_name':operation_name,
            'results':result,
        }
        print(result)
        return render(request,'reports/ot_report.html',context)
    operation_category = Operation_category.objects.all()
    operation_name = Operation_name.objects.all()
    doctor = AddStaff.objects.filter(role='Doctor')
    context ={
        'operation_category':operation_category,
        'doctor':doctor,
        'operation_name':operation_name,
    }
    return render(request,'reports/ot_report.html',context)




def     search_case_id(request):
    if request.method == 'GET':

        search_id = request.GET.get('case_id', None)

        if search_id is not None:
            
            ipd_result = IpdPatient.objects.filter(id=search_id)
            ipd_result = Radiology.objects.filter(id=search_id)
            ipd_result = Pathology.objects.filter(id=search_id)
            opd_result = OpdPatient.objects.filter(id=search_id)

            context = {
                'ipd_result': ipd_result,
                'opd_result': opd_result,
            }

            return render(request, 'reports/case.html', context)

    return render(request, 'reports/case.html', {})


def stock(request):
    if request.method=="POST":
        name = request.POST.get('name')
        stock = request.POST.get('stock')
        medicine = Purchase.objects.get(id=name)
        
        stock = Stock(
            medicine=medicine,
            stock=stock,
        )
        stock.save()
        return redirect('stock')
    
    medicine = Purchase.objects.all()
    stock = Stock.objects.all()
    context ={
        'medicine':medicine,
        'stock':stock,
    }

    return render(request,'pharmacy/medicine/stock.html',context)




def cash_book(request):
    total_sales = Sales_Invoice.objects.filter(type='sales',payment_type='cash')
    path = Pathology.objects.filter(payment_mode='cash')
    payment_in = Payment_In.objects.all()
    expense = Expense_Invoice.objects.all()

    context ={
        'sales':total_sales,
        'payment_in':payment_in,
        'expense':expense
    }

    return render(request,'accounts/report/cash_flow.html',context)


def party_report(request,id):
    party = Party.objects.get(id=id)
    sales = Sales_Invoice.objects.filter(name=party.part_name)
    total = sum(transaction.total or 0 for transaction in sales)
    
    
    context = {
        'sales':sales,
        "party":party,
        'balance':total,
        
    }
    return render(request,'accounts/report/party_report.html',context)




def approval(request):
    test = Pathology_test.objects.all()
    context ={
        'test':test,
    }
    return render(request,'panels/approval.html',context)


def approval_path(request,id):
    test = Pathology_test.objects.get(id=id)
    test.approved = True
    test.save()
    
    messages.success(request,("Application Has Been Approved"))
    
    
    return redirect('/approval')

def cashbook(request):
    if request.method=="POST":
        date = request.POST.get('date')
        
        particulars = request.POST.get('particulars')
        type = request.POST.get('type')
        lf = request.POST.get('lf')
        debit = request.POST.get('debit')
        credit = request.POST.get('credit')
        
        
       
        
        cashbook = CashBook(
            date =date,
            particulars=particulars,
            lf=lf,
            debit=debit,

            credit=credit,
         
            
            
        )
        cashbook.save()
        return redirect('cashbook')
    
    cash = CashBook.objects.all()
    
    total_debit = sum(transaction.debit or 0 for transaction in cash)
    total_credit = sum(transaction.credit or 0 for transaction in cash)
    balance = total_debit -total_credit
    context = {
        'cash':cash,
        'balance':balance,
    }
    return render(request,'accounts/report/cashbook.html',context)


def medicine_composition(request):
    if request.method=="POST":
        composition = request.POST.get('composition')
        med = Medicine_Composition(
            name=composition,
        )
        med.save()

        return redirect('medicine_composition')
    
    composition = Medicine_Composition.objects.all()
    context = {
        'composition':composition,
    }

    return render(request,'pharmacy/medicine/composition.html',context)


def bankbooks(request):
    if request.method=="POST":
        date = request.POST.get('date')
   
        particulars = request.POST.get('particulars')
     
        lf = request.POST.get('lf')
        debit = request.POST.get('debit')
        credit = request.POST.get('credit')
       

        
        cashbook = BankBook(
            date =date,
            particulars=particulars,
            lf=lf,
            debit=debit,
            type="orgination",
            credit=credit,
          
            
            
            
        )
        cashbook.save()
        cash = BankBook.objects.filter(type="orgination")
        total_debit = sum(transaction.debit or 0 for transaction in cash)
        total_credit = sum(transaction.credit or 0 for transaction in cash)
        balance = total_credit - total_debit
        context = {
      
            'cash':cash,
            'balance':balance,
        }
        return render(request,'accounts/report/bankorigin.html',context)
    
    cash = BankBook.objects.filter(type="orgination")
    total_debit = sum(transaction.debit or 0 for transaction in cash)
    total_credit = sum(transaction.credit or 0 for transaction in cash)
    balance = total_credit - total_debit
    context = {
      
        'cash':cash,
        'balance':balance,
    }
    return render(request,'accounts/report/bankorigin.html',context)





def bankbook(request,id):
    if request.method=="POST":
        date = request.POST.get('date')
        id = Bank.objects.get(id=id)

        particulars = request.POST.get('particulars')
        type = request.POST.get('type')
        lf = request.POST.get('lf')
        debit = request.POST.get('debit')
        credit = request.POST.get('credit')
        balance = request.POST.get('balance')

        
        cashbook = BankBook(
            date =date,
            particulars=particulars,
            lf=lf,
            debit=debit,
            bank=id,
            credit=credit,
          
            
            
            
        )
        cashbook.save()
        
        return redirect('bank')
    bank = Bank.objects.get(id=id)
    cash = BankBook.objects.filter(bank=id)
    total_debit = sum(transaction.debit or 0 for transaction in cash)
    total_credit = sum(transaction.credit or 0 for transaction in cash)
    balance = total_credit - total_debit
    context = {
        'bank':bank,
        'cash':cash,
        'balance':balance,
    }
    return render(request,'accounts/report/bankbook.html',context)



def brs(request):
    if request.method == 'POST':
        balance = request.POST.get('openingBalance')
        adjusted = request.POST.get('adjustedAmount')
        item_counter = request.POST.get('itemCounter')
      
        

        print(balance)
        print(item_counter)
    
        if item_counter.isdigit():
            item_counter = int(item_counter)
        else:
            item_counter = 0 
        for i in range(1, item_counter + 1):
            
            
            item = request.POST.get(f'particulars_{i}')
           

            value = request.POST.get(f'value_{i}')
            operation = request.POST.get(f'operation_{i}')
          
        
            item = BRS(
                particulars =item,
                amount=value,
                balance=balance,
                adjusted=adjusted,
                operation=operation,




            )
            
            item.save()
            
    
        
        
        return redirect('brs')
        
    brs = BRS.objects.all()
    context= {
        'brs':brs,
     
    }
    return render(request, 'accounts/report/brs.html',context)


def bank(request):
    if request.method =="POST":
        bank_name = request.POST.get('bank_name')
        branch = request.POST.get('branch')
        type = request.POST.get('type')
        ac = request.POST.get('bank_no')
        bank = request
        bank = Bank(
            bank_name=bank_name,
            branch=branch,
            type=type,
            ac=ac,
        )
        bank.save()
        return redirect('bank') 
    
    bank = Bank.objects.all()
    context ={
        'bank':bank
    }

    return render(request,'accounts/bank.html',context)


def depreciation(request):
    if request.method =='POST':
        asset = request.POST.get('asset')
        dep = int(request.POST.get('dep'))
        assets = Asset.objects.get(id=asset)
        depreciation_amount = int(assets.price) * (dep / 100)
        date = request.POST.get('date')
        net_value = int(assets.price) - int(depreciation_amount)
        assets.price = net_value
        assets.save() 
        depreciation = Depreciation(
            asset=assets,
            date=date,
            percentage=dep,
            amount=depreciation_amount,

        )
        depreciation.save()

        return redirect('depreciation')
    assets = Asset.objects.all()
    dep = Depreciation.objects.all()
    context ={
        'assets':assets,
        'depreciaton':dep,

    }

    return render(request,'accounts/assets/depreciation.html',context)


def pos_bankpdf(request):


    if request.method == 'POST':
        
        from_date = request.POST.get('date_time')
        to_date = request.POST.get('to_date')
        item_counter = request.POST.get('item_counter')

      
        print(item_counter)
        if item_counter.isdigit():
            item_counter = int(item_counter)
        else:
            item_counter = 0

        product_list = []
        
        for i in range(1, item_counter + 1):
            
            
            print(item_counter)
            transfer = request.POST.get(f'tranfer_{i}')


            value = request.POST.get(f'value_{i}')
            
            description = request.POST.get(f'des_{i}')
            cheque = request.POST.get(f'cheque_{i}')
            debit = request.POST.get(f'debit_{i}')
            credit = request.POST.get(f'credit_{i}')

            balance = request.POST.get(f'balance_{i}')
           
            
            product = {
                'transfer': transfer,
                'value': value,
                'description': description,
                'cheque':cheque,
                'debit':debit,
                'credit':credit,
                'balance':balance,
                
                }
    
            print(product)
            product_list.append(product)
        print(product_list)

        
      
        
    
    context= {
        'products':product_list,
        'from_date':from_date,
        "to_date":to_date,
    }

    template = get_template('templat/pos_bank.html')
    html = template.render(context)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="statement.pdf"'

    # Generate PDF from HTML using ReportLab and pisa
    pisa_status = pisa.CreatePDF(html, dest=response)

    # Return the response
    if pisa_status.err:
        return HttpResponse('PDF generation failed', content_type='text/plain')
    return response


def pos_bank(request):
    return render(request,'accounts/report/pos_bank.html')







def bank_pdf(request,id):

        
    bank=BankBook.objects.filter(bank=id)
 

    total_debit = sum(transaction.debit or 0 for transaction in bank)
    total_credit = sum(transaction.credit or 0 for transaction in bank)
    dt = datetime.now()
    date = dt.strftime("%A, %d %B %Y")
    balance = total_credit-total_debit
    context= {
        'balance':balance,
        'date':date,    
        'bank':bank,
    }
    template = get_template('templat/bank_pdf.html')
    html = template.render(context)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="bankbook.pdf"'

    # Generate PDF from HTML using ReportLab and pisa
    pisa_status = pisa.CreatePDF(html, dest=response)

    # Return the response
    if pisa_status.err:
        return HttpResponse('PDF generation failed', content_type='text/plain')
    return response




def cash_pdf(request):

    if request.method =="POST":
        from_date = request.POST.get('from_date')
        to_date = request.POST.get('to_date')
        cash=CashBook.objects.filter(date__range=(from_date,to_date))


        total_debit = sum(transaction.debit or 0 for transaction in cash)
        total_credit = sum(transaction.credit or 0 for transaction in cash)
        dt = datetime.now()
        date = dt.strftime("%A, %d %B %Y")
        balance = total_credit-total_debit
        context= {
            'balance':balance,
            'date':date,    
            'cash':cash,
    }
        template = get_template('templat/cash_pdf.html')
        html = template.render(context)

        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="cashbook.pdf"'

    # Generate PDF from HTML using ReportLab and pisa
        pisa_status = pisa.CreatePDF(html, dest=response)

    # Return the response
        if pisa_status.err: 
            return HttpResponse('PDF generation failed', content_type='text/plain')
        return response
    return redirect('cashbook')

def bankorigin(request):

        
    bank=BankBook.objects.filter(type='orgination')
 

    total_debit = sum(transaction.debit or 0 for transaction in bank)
    total_credit = sum(transaction.credit or 0 for transaction in bank)
    balance = total_credit-total_debit
    dt = datetime.now()
    date =  dt.strftime("%A, %d %B %Y")
    context= {
        'balance':balance,
        'date':date,
        'bank':bank,
    }
    template = get_template('templat/bank_pdf.html')
    html = template.render(context)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="bankbook.pdf"'

    # Generate PDF from HTML using ReportLab and pisa
    pisa_status = pisa.CreatePDF(html, dest=response)

    # Return the response
    if pisa_status.err:
        return HttpResponse('PDF generation failed', content_type='text/plain')
    return response




def pos_blood(request):
    blood_component = Blood_Component.objects.all()
    qty = Bag_available.objects.all()
    context = {
        'component':blood_component,
        'qty':qty,  
    }
    return render(request,'blood/pos_blood.html',context)

def house_blood(request):
    blood_component = Blood_Component.objects.all()
    qty = Bag_available.objects.all()
    doctor = AddStaff.objects.filter(role="Doctor")
    patient = Patient.objects.all()
    context = {
        'component':blood_component,
        'qty':qty,  
        'doctor':doctor,
        'patient':patient
    }
    return render(request,'blood/house_blood.html',context)



def pdf_blood(request):
    if request.method == 'POST':
        
        sub_total = request.POST.get('sub_total')
        tax = request.POST.get('tax')
        grand_total = request.POST.get('grand_total')
        discount = request.POST.get('disc')
        small_note = request.POST.get('small_note')
        date_time = request.POST.get('date_time')
        
        payment = request.POST.get('payment')
        paid_amount = request.POST.get('paid_amount')
        patient = request.POST.get('path_test')
        doctor = request.POST.get('doctor')
        
        item_counter = request.POST.get('item_counter')

        pos = POS(
            doctor=doctor,
            payment_mode=payment,
            date=date_time,

            small_note=small_note,
            tax_percent=tax,
            discount_percent=discount,
            







        )

        print(item_counter)
        if item_counter.isdigit():
            item_counter = int(item_counter)
        else:
            item_counter = 0

        product_list = []
        
        for i in range(1, item_counter + 1):
            
            
            print(item_counter)
            
            qty = int(request.POST.get(f'qty_{i}'))
            available = int(request.POST.get(f'available_{i}'))


            
            if available < qty:
                return HttpResponse('Error: Insufficient available quantity.')

            
            
            
           
            
        
            stock = Bag_available.objects.get(id=1)
            updated_available_quantity = available - qty
            print(updated_available_quantity)
            stock.qty = updated_available_quantity
            stock.save()
            

            group = request.POST.get(f'group_{i}')
            
            component = request.POST.get(f'test_{i}')
            volume = request.POST.get(f'volume_{i}')
            

            total = request.POST.get(f'total_{i}')
           
            
            product = {
                
                'quantity': qty,
                'component': component,
                
                'volume':volume,
                'group':group,
                
                'total': total
                }
    
            print(product)
            product_list.append(product)
        print(product_list)

        
      
        
    
    context= {
        'products':product_list,
        'sub_total':sub_total,
        'tax':tax,
        'discount':discount,
        'patient':patient,
        'paid_amount':paid_amount,
        'small_note':small_note,
        'date_time':date_time,
        
        'doctor':doctor,
        'payment':payment,
        'grand_total':grand_total,
    }

    template = get_template('templat/pos_blood.html')
    html = template.render(context)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="invoice.pdf"'

    # Generate PDF from HTML using ReportLab and pisa
    pisa_status = pisa.CreatePDF(html, dest=response)

    # Return the response
    if pisa_status.err:
        return HttpResponse('PDF generation failed', content_type='text/plain')
    return response


def certificate(request):
    

    ipd = IpdPatient.objects.filter(discharged_status=True)
    opd = OpdPatient.objects.filter(discharged_status=True)
    context ={
        'ipd':ipd,
        'opd':opd,
    }
    return render(request,'certificate/certificate.html',context)

def hr_certificate(request):
    return render(request,'hr/certificate.html')


def blood_setup(request):
    if request.method =="POST":
        name = request.POST.get('name')
        type = request.POST.get('component')
        blood = Blood_Setup(
            name=name,
            type=type,
        )
        blood.save()
        return redirect('blood_setup')
    type = Blood_Setup.objects.all()

    
    context ={
        'type':type
    }

    return render(request,'setup/blood/component.html',context)

def blood_component(request):
    if request.method =="POST":
        blood_group = request.POST.get('blood_group')
        bag = request.POST.get('bag')
        volume = request.POST.get('volume')
        unit = request.POST.get('unit')
        lot = request.POST.get('lot')
        institution = request.POST.get('institution')
        component_name = request.POST.get('component_name')
        component = Blood_Setup.objects.get(id=component_name)
        blood = Blood_Component(
            blood_group=blood_group,
            bag=bag,
            volume=volume,
            unit=unit,
            lot=lot,
            institution=institution,
            component_name=component,
            
        )

        blood.save()
        return redirect('blood_component')
    blood = Blood_Component.objects.all()
    donor = BloodDonation.objects.all()
    component = Blood_Setup.objects.all()
    context ={
        'blood':blood,
        'donor':donor,
        'component':component
    }

    return render(request,'blood/blood_component.html',context)



def leaves(request):
    if request.method == "POST":
        name = request.POST.get('name')
        type = request.POST.get('type')
        date = request.POST.get('date')
        staff = AddStaff.objects.get(id=name)
        leav = Leaves(
            staff=staff,
            type=type,
            date=date,
        )
        leav.save()
        return redirect('leaves')
    leave = Leaves.objects.all()
    staff = AddStaff.objects.all()
    context = {
        'leave':leave,
        'staff':staff,
    }
    return render(request,'hr/leaves.html',context)


def birth_certificate(request):
    child = ChildBirth.objects.all()
    context ={
        'child':child
    }
    return render(request,'birth/birth_certifcate.html',context)



def birth_pdf(request,id):
    child = ChildBirth.objects.get(id=id)

   
 

    header_name = header.objects.all().first()

    child= {
        'child':child,
        'hospital_name':header_name.name,
        'url':header_name.image.url,

    }

    template = loader.get_template('templat/birth_pdf.html')
    # response = HttpResponse(content_type='application/pdf')
    # response['Content-Disposition'] = 'attachment; filename="birth.pdf"'

    # template = get_template('templat/birth_pdf.html')
    # html = template.render(context)

    

    # # Generate PDF from HTML using ReportLab and pisa
    # pisa_status = pisa.CreatePDF(html, dest=response)

    # # Return the response
    # if pisa_status.err:
    #     return HttpResponse('PDF generation failed', content_type='text/plain')
    # return response
    
    html_file_path = 'C:/Users/devsh/Desktop/metamedplus/adminapp/templates/templat/birth_pdf.html'

    html_content = template.render({'child': child},request=request)

    # Create a WeasyPrint HTML object
    html = HTML(string=html_content, base_url=request.build_absolute_uri())

    # Generate the PDF content
    pdf_content = html.write_pdf()

    # Create a Django HttpResponse with PDF content
    response = HttpResponse(pdf_content, content_type='application/pdf')
    response['Content-Disposition'] = 'filename="output.pdf"'

    return response




def death_pdf(request,id):
       
    child=DeathRecord.objects.get(id=id)
 



 
  
   
 


    header_name = header.objects.all().first()
    child= {
        'child':child,
        'hospital_name':header_name.name,

    }

    template = loader.get_template('templat/death.html')
    # response = HttpResponse(content_type='application/pdf')
    # response['Content-Disposition'] = 'attachment; filename="birth.pdf"'

    # template = get_template('templat/birth_pdf.html')
    # html = template.render(context)

    

    # # Generate PDF from HTML using ReportLab and pisa
    # pisa_status = pisa.CreatePDF(html, dest=response)

    # # Return the response
    # if pisa_status.err:
    #     return HttpResponse('PDF generation failed', content_type='text/plain')
    # return response
    
    html_file_path = 'C:/Users/devsh/Desktop/metamedplus/adminapp/templates/templat/death.html'

    html_content = template.render({'child': child},request=request)

    # Create a WeasyPrint HTML object
    html = HTML(string=html_content, base_url=request.build_absolute_uri())

    # Generate the PDF content
    pdf_content = html.write_pdf()

    # Create a Django HttpResponse with PDF content
    response = HttpResponse(pdf_content, content_type='application/pdf')
    response['Content-Disposition'] = 'filename="output.pdf"'

    return response

def send(request):
    if request.method == "POST":
        title = request.POST.get('title')
        attachment = request.FILES['attach']  # Assuming 'attachment' is a file field in your form
        message = request.POST.get('message')
        bcc = request.POST.get('bcc')
        cc = request.POST.get('cc')
        to = request.POST.get('to')
        from_mail = request.POST.get('from')

        mails = AddStaff.objects.all()
        to_list = to
        cc_list = [c.strip() for c in cc.split(',') if c.strip()]

        # Split and clean the 'bcc' values
        bcc_list = [b.strip() for b in bcc.split(',') if b.strip()]
        print(bcc_list)
        with get_connection(  
           host=settings.EMAIL_HOST, 
     port=settings.EMAIL_PORT,  
     username=settings.EMAIL_HOST_USER, 
     password=settings.EMAIL_HOST_PASSWORD, 
     use_tls=settings.EMAIL_USE_TLS  ,
        ) as connection:  
            subject = title
            from_email = from_mail
            
            
            
            email = EmailMessage(subject, message, from_email, [to_list],bcc=bcc_list,cc=cc_list, connection=connection)

            email.attach(attachment.name, attachment.read(), attachment.content_type)
              
 
            email.send()

    return render(request, 'messaging/mail.html')


def send_test(request):  
    
    time.sleep(3)
    with get_connection(  
           host=settings.EMAIL_HOST, 
     port=settings.EMAIL_PORT,  
     username=settings.EMAIL_HOST_USER, 
     password=settings.EMAIL_HOST_PASSWORD, 
     use_tls=settings.EMAIL_USE_TLS  
       ) as connection:  
           subject = "Account Password"
           from_email = "info@phoneixhms.com"
           recipient_list = ['programmer62563@gmail.com','devshandilaya1@gmail.com']  
           message = "Hello Workinf"
           send_mail(subject, message, from_email, recipient_list, connection=connection)


def send_push_notification(request):
    account_sid = 'ACedb7a50d829d28765419e0f2ad173f5a'
    auth_token = '095924488d50386a6eb099130f94060e'

    # Twilio phone number (a Twilio phone number that you have purchased)
    twilio_phone_number = '+12055397628'

    # Recipient's phone number
    to_phone_number = "+919873054516"  # Replace with the actual recipient's phone number

    # Create a Twilio client
    client = Client(account_sid, auth_token)

    # Send SMS
    message = client.messages.create(
        body="test mail",
        from_=twilio_phone_number,
        to=to_phone_number
    )

    return redirect('send_notification')



def send_notification_push(request):
    if request.method =="POST":
        to = request.POST.get('to')
        body = request.POST.get('body')
     
        account_sid = 'ACedb7a50d829d28765419e0f2ad173f5a'
        auth_token = '9fb04b0aa3f828af698f4ba666f5f2ad'

    # Twilio phone number (a Twilio phone number that you have purchased)
        twilio_phone_number = '+12055397628'

    # Recipient's phone number
        to_phone_number = "+91"+to  # Replace with the actual recipient's phone number

    # Create a Twilio client
        client = Client(account_sid, auth_token)
        print(to)

    # Send SMS
        message = client.messages.create(
            body=body,
            from_=twilio_phone_number,
            to=to_phone_number,
        )
    

   

        return redirect('send_notification')
    return render(request,'messaging/notification.html')


def appointment_letter(request):
    if request.method == "POST":
        employe = request.POST.get('employe')
        date = request.POST.get('date')
        designation = request.POST.get('designation')
        joining = request.POST.get('joining')
        salary = request.POST.get('salary')
        basis = request.POST.get('basis')
        expiry = request.POST.get('expiry')
        department = request.POST.get('department')
        sender = request.POST.get('sender')
        basis = request.POST.get('basis')
        sender_designation = request.POST.get('sender_designation')
        hospital_name = header.objects.all().first()
        context = {
        'sender_designation':sender_designation,
        'basis':basis,
        'sender_name':sender,
        'expiry_date':expiry,
        'salary':salary,
        'image':hospital_name.image.url if hospital_name else 'Logo',
        'joining_date':joining,
        'department':department,
        'company_name':hospital_name.name if hospital_name else 'Your Hospital',
        'designation':designation,
        'date':date,
        'employe':employe,
        'name':'Letter'
          }
    
        template = get_template('letters/appointment.html')
        html = template.render(context)

        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="appointment.pdf"'

    # Generate PDF from HTML using ReportLab and pisa
        pisa_status = pisa.CreatePDF(html, dest=response)

    
        if pisa_status.err:
            return HttpResponse('PDF generation failed', content_type='text/plain')
        return response
    return render(request,'hr/letter/appointment.html')
def resign_letter(request):
    context = {
        'name':'Letter'
    }
    template = get_template('letters/resign.html')
    html = template.render(context)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="resign.pdf"'

    # Generate PDF from HTML using ReportLab and pisa
    pisa_status = pisa.CreatePDF(html, dest=response)

    # Return the response
    if pisa_status.err:
        return HttpResponse('PDF generation failed', content_type='text/plain')
    return response


def leave_letter(request):
    if request.method == "POST":
        employe = request.POST.get('employe')
        date = request.POST.get('date')
        
        
        to = request.POST.get('to')
        from_date = request.POST.get('from_date')
        days = request.POST.get('days')
        reason = request.POST.get('reason')
        to_date = request.POST.get('to_date')
        
        
        hospital_name = header.objects.all().first()
        context = {
       
      
 
        'image':hospital_name.image.url if hospital_name else 'Logo',
        'from_date':from_date,
        'to_date':to_date,
        'manager':to,
        'company_name':hospital_name.name if hospital_name else 'Your Hospital',
        
        'date':date,
        'days':days,
        'employe':employe,
        'reason':reason,
        'name':'Letter'
          }
   
        template = get_template('letters/leave.html')
        html = template.render(context)

        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="leave.pdf"'

    # Generate PDF from HTML using ReportLab and pisa
        pisa_status = pisa.CreatePDF(html, dest=response)

    # Return the response
        if pisa_status.err:
            return HttpResponse('PDF generation failed', content_type='text/plain')
        return response
    
    return render(request,'hr/letter/leave.html')
def sampleappointment_letter(request):
    
        template = get_template('letters/sample_appointment.html')
        html = template.render(template)

        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="appointment.pdf"'

    # Generate PDF from HTML using ReportLab and pisa
        pisa_status = pisa.CreatePDF(html, dest=response)

    # Return the response
        if pisa_status.err:
                return HttpResponse('PDF generation failed', content_type='text/plain')
        return response
    


def sampleresign_letter(request):
    context = {
        'name':'Letter'
    }
    template = get_template('letters/sample_resign.html')
    html = template.render(context)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="resign.pdf"'

    # Generate PDF from HTML using ReportLab and pisa
    pisa_status = pisa.CreatePDF(html, dest=response)

    # Return the response
    if pisa_status.err:
        return HttpResponse('PDF generation failed', content_type='text/plain')
    return response


def inhouse_pathpdf(request):
    if request.method == 'POST':
        
        sub_total = request.POST.get('sub_total')
        tax = request.POST.get('tax')
        grand_total = request.POST.get('grand_total')
        discount = request.POST.get('disc')
        small_note = request.POST.get('small_note')
        date_time = request.POST.get('date_time')
        bill_date = request.POST.get('bill_date')
        
        payment = request.POST.get('payment')
        patient = request.POST.get('patient')
        paid_amount = request.POST.get('paid_amount')
        doctor = request.POST.get('doctor')
        item_counter = request.POST.get('item_counter')
        print(item_counter)
        if item_counter.isdigit():
            item_counter = int(item_counter)
        else:
            item_counter = 0

        product_list = []
        
        for i in range(1, item_counter + 1):
            
            
            print(item_counter)

            test = request.POST.get(f'test_{i}')
            
            tests =  re.sub(r'_.*', '', test)

          
            test  = tests.replace("_", "")
           
            cat = request.POST.get(f'cat_{i}')
            cate = re.sub(r'\d', '',cat)

            cat  = cate.replace("_", "")
            price = request.POST.get(f'price_{i}')
           

            total = request.POST.get(f'total_{i}')
         
            
            product = {
                'test': test,
                'cat': cat,
                'price': price,
                
                
                'total': total
                }
    
            print(product)
            product_list.append(product)
        print(product_list)

        
      
        
    balance = float(grand_total)-float(paid_amount)
    patient_details = Pathology.objects.get(id=patient)
    context= {
        'products':product_list,
        'sub_total':sub_total,
        'tax':tax,
        'discount':discount,
        'paid_amount':paid_amount,
        'small_note':small_note,
        'bill_date':bill_date,
        'date_time':date_time,
        'balance':balance,
        'patient_details':patient_details,
        'patient':patient,
        'doctor':doctor,
        'payment':payment,
        'grand_total':grand_total,
    }

    template = get_template('templat/house_path.html')
    html = template.render(context)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="invoice.pdf"'

    # Generate PDF from HTML using ReportLab and pisa
    pisa_status = pisa.CreatePDF(html, dest=response)

    # Return the response
    if pisa_status.err:
        return HttpResponse('PDF generation failed', content_type='text/plain')
    return response


def inhousepharma_pdf(request):
    if request.method == 'POST':
        
        sub_total = request.POST.get('sub_total')
        tax = request.POST.get('tax')
        grand_total = request.POST.get('grand_total')
        discount = request.POST.get('disc')
        small_note = request.POST.get('small_note')
        date_time = request.POST.get('date_time')
        medicine_composition = request.POST.get('medicine_composition')
        payment = request.POST.get('payment')
        
        paid_amount = request.POST.get('paid_amount')
        doctor = request.POST.get('doctor')
        
        item_counter = request.POST.get('item_counter')

        pos = POS(
            doctor = doctor,
            payment_mode=payment,
            date=date_time,
            composition=medicine_composition,
            small_note=small_note,
            tax_percent=tax,
            discount_percent=discount,
            


            







        )
        pos.save()

        print(item_counter)
        if item_counter.isdigit():
            item_counter = int(item_counter)
        else:
            item_counter = 0

        product_list = []
        
        for i in range(1, item_counter + 1):
            
            
            print(item_counter)
            item = request.POST.get(f'med_{i}')
            qty = int(request.POST.get(f'qty_{i}'))
            
            available = int(request.POST.get(f'available_{i}'))
            print(qty)
            print(available)


            
            if available < qty:
                return HttpResponse('Error: Insufficient available quantity.')

            
            
            
            medicines_ids = [int(id) for id in re.findall(r'\d+', item)]

            print(medicines_ids)
            for medicines_id in medicines_ids:
        
                stock = get_object_or_404(Stock, medicine=medicines_id)
                updated_available_quantity = available - qty
                print(updated_available_quantity)
                stock.stock = updated_available_quantity
                stock.save()
                print(stock.stock)

            cat = request.POST.get(f'cat_{i}')
            items = re.sub(r'\d', '',item)
            item  = items.replace("_", "")
            price = request.POST.get(f'price_{i}')
            expiry = request.POST.get(f'expiry_{i}')
            batch = request.POST.get(f'batch_{i}')
            tax_ = request.POST.get(f'tax_{i}')

            total = request.POST.get(f'total_{i}')
           
            
            product = {
                'item': item,
                'quantity': qty,
                'price': price,
                'tax_':tax_,
                'expiry':expiry,
                'batch':batch,
                'cat':cat,
                
                'total': total
                }
    
            print(product)
            product_list.append(product)
        print(product_list)

        
      
    balance  = float(grand_total) - float(paid_amount)
    address = Address.objects.all().first()
    hospital = header.objects.all().first()
    context= {
        'products':product_list,
        'sub_total':sub_total,
        'tax':tax,
        'discount':discount,
        'address':address,
        'small_note':small_note,
        'hospital_name':hospital.name,
        'paid_amount':paid_amount,
        'balance':balance,
                'date_time':date_time,
                'composition':medicine_composition,
                'doctor':doctor,
                'payment':payment,
        'grand_total':grand_total,
    }

    template = get_template('templat/inhousepharmacy_pdf.html')
    html = template.render(context)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="invoice.pdf"'

    # Generate PDF from HTML using ReportLab and pisa
    pisa_status = pisa.CreatePDF(html, dest=response)

    # Return the response
    if pisa_status.err:
        return HttpResponse('PDF generation failed', content_type='text/plain')
    return response



def housepdf_blood(request):
    if request.method == 'POST':
        
        sub_total = request.POST.get('sub_total')
        tax = request.POST.get('tax')
        grand_total = request.POST.get('grand_total')
        discount = request.POST.get('disc')
        small_note = request.POST.get('small_note')
        date_time = request.POST.get('date_time')
        paid_amount = request.POST.get('paid_amount')
        
        payment = request.POST.get('payment')
        patient = request.POST.get('path_test')
        doctor = request.POST.get('doctor')
        
        item_counter = request.POST.get('item_counter')

        pos = POS(
            doctor=doctor,
            payment_mode=payment,
            date=date_time,

            small_note=small_note,
            tax_percent=tax,
            discount_percent=discount,
            







        )
        

        print(item_counter)
        if item_counter.isdigit():
            item_counter = int(item_counter)
        else:
            item_counter = 0

        product_list = []
        
        for i in range(1, item_counter + 1):
            
            
            print(item_counter)
            
            qty = int(request.POST.get(f'qty_{i}'))
            available = int(request.POST.get(f'available_{i}'))


            
            if available < qty:
                return HttpResponse('Error: Insufficient available quantity.')

            
            
            
           
            
        
            stock = Bag_available.objects.get(id=1)
            updated_available_quantity = available - qty
            print(updated_available_quantity)
            stock.qty = updated_available_quantity
            stock.save()
            

            group = request.POST.get(f'group_{i}')
            
            component = request.POST.get(f'test_{i}')
            volume = request.POST.get(f'volume_{i}')
            

            total = request.POST.get(f'total_{i}')
           
            
            product = {
                
                'quantity': qty,
                'component': component,
                
                'volume':volume,
                'group':group,
                
                'total': total
                }
    
            print(product)
            product_list.append(product)
        print(product_list)

        
      
        
    balance = float(grand_total)-float(paid_amount)
    context= {
        'products':product_list,
        'sub_total':sub_total,
        'tax':tax,
        'discount':discount,
        'patient':patient,
        'paid_amount':paid_amount,
        'balance':balance,
        'small_note':small_note,
        'date_time':date_time,
        
        'doctor':doctor,
        'payment':payment,
        'grand_total':grand_total,
    }

    template = get_template('templat/house_blood.html')
    html = template.render(context)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="invoice.pdf"'

    # Generate PDF from HTML using ReportLab and pisa
    pisa_status = pisa.CreatePDF(html, dest=response)

    # Return the response
    if pisa_status.err:
        return HttpResponse('PDF generation failed', content_type='text/plain')
    return response


def pos_records(request):
    pos = POS.objects.all()

    context ={
        'pos':pos
    }

    return render(request,'pos/pos_records.html',context)




def search_attendance(request):
    if 'q' in request.GET:
        query = request.GET['q']
        results = Attendance.objects.filter(role__icontains=query)
        context = {
            'results':results,
            'role':query,
        }
    else:
        context = {
            'results':None,
            'role':query,
        }

    return render(request, 'hr/attendance/attendance_record.html', context)

def attendance_role(request):
    role = Role.objects.all()
    context = {
        'role':role
    }
    return render(request,'hr/attendance/search_attendance.html',context)


def attendance(request):
    if request.method == 'POST':
        
        date  =request.POST.get('date')
        for staff in AddStaff.objects.all():
            
            attendance_status = request.POST.get(f'attendance_{staff.id}')
            shift = request.POST.get(f'shift_{staff.id}')

            Attendance.objects.create(
                name=staff,
                role=staff.role,
                
                attendance=attendance_status,
                date=date,
                
                shift=shift,
            )
        return redirect('attendance')  
    
    staff = AddStaff.objects.all()
    context ={
        'staff':staff,
    }
    return render(request,'hr/attendance/attendance.html',context)





def other_attendance(request):
    if request.method == 'POST':
        
        date = request.POST.get('date')
        
        item_counter = request.POST.get('item_counter')

        

        print(item_counter)
        if item_counter.isdigit():
            item_counter = int(item_counter)
        else:
            item_counter = 0

        
        
        for i in range(1, item_counter + 1):
            
            
           
            name = request.POST.get(f'name_{i}')
            role = request.POST.get(f'role_{i}')
            attendance = request.POST.get(f'attendance_{i}')
            shift = request.POST.get(f'shift_{i}')


            attendance = Other_Attendance(
                name=name,
                role=role,
                date=date,
                attendance=attendance,
                shift=shift,
            )
            attendance.save()


        return redirect('other_attendance')
        
    
    return render(request,'hr/attendance/other_attendance.html')

            
        
            
def otherattendance_record(request):
    attendance = Other_Attendance.objects.all()

    context={
        'attendance':attendance,
    }

    return render(request,'hr/attendance/other_record.html',context)
    


def attendance_form(request):
    
    dt = datetime.now()
    date = dt.strftime("%A, %d %B %Y")
    context ={
        'lemon': range(1,60),
        'date':date,
    }
    template = get_template('templat/attendance_pdf.html')
    html = template.render(context)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="attendance.pdf"'

    # Generate PDF from HTML using ReportLab and pisa
    pisa_status = pisa.CreatePDF(html, dest=response)

    # Return the response
    if pisa_status.err:
        return HttpResponse('PDF generation failed', content_type='text/plain')
    return response


def download_ipdcolumn(request):

    
    if request.method=="POST":
        from_date = request.POST.get('from_date')
        to_date = request.POST.get('to_date')
        
        ipd_patient = IpdPatient.objects.filter(admission_date__range=(from_date, to_date))
    
        hospital_name = header.objects.all().first()
        context ={
            'ipd': ipd_patient,
            'hospital_name':hospital_name.name if hospital_name else 'Your Hospital',
        }
        template = get_template('templat/ipd_list.html')
        html = template.render(context)

        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="ipd_list.pdf"'

    # Generate PDF from HTML using ReportLab and pisa
        pisa_status = pisa.CreatePDF(html, dest=response)

    # Return the response
        if pisa_status.err:
            return HttpResponse('PDF generation failed', content_type='text/plain')
        return response
    return redirect('ipd_patient')


def download_opdcolumn(request):
    if request.method=="POST":
        from_date = request.POST.get('from_date')
        to_date = request.POST.get('to_date')
        
        opd = OpdPatient.objects.filter(admission_date__range=(from_date, to_date))

    
        hospital_name = header.objects.all().first()
        context ={
            'opd': opd,
            'hospital_name':hospital_name.name if hospital_name else 'Your Hospital',
        }
        template = get_template('templat/opd_list.html')
        html = template.render(context)

        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="opd_list.pdf"'

    # Generate PDF from HTML using ReportLab and pisa
        pisa_status = pisa.CreatePDF(html, dest=response)

    # Return the response
        if pisa_status.err:
            return HttpResponse('PDF generation failed', content_type='text/plain')
        return response
    return redirect('opd')


def add_address(request):
    if request.method == 'POST':
        address = request.POST.get('address')
        phone_no = request.POST.get('phone_no')
        email_id = request.POST.get('email_id')

        Address.objects.create(
            address=address,
            phone_no=phone_no,
            email_id=email_id
        )

        return redirect('add_address')

    return render(request, 'hospital/address.html')




def appointment_download(request):
    appointment = AppointmentDetails.objects.all()
    hospital_name = header.objects.all().first()
    context ={
            'appointment': appointment,
            'hospital_name':hospital_name.name if hospital_name else 'Your Hospital',
        }
    template = get_template('templat/appointment.html')
    html = template.render(context)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="appointment.pdf"'

    # Generate PDF from HTML using ReportLab and pisa
    pisa_status = pisa.CreatePDF(html, dest=response)

    # Return the response
    if pisa_status.err:
        return HttpResponse('PDF generation failed', content_type='text/plain')
    return response

def appointmentpdf_download(request,id):
    id = AppointmentDetails.objects.get(id=id)
    
    hospital_name = header.objects.all().first()
    context ={
            'appointment': id,
            'hospital_name':hospital_name.name if hospital_name else 'Your Hospital',
        }
    template = get_template('templat/appointment_pdf.html')
    html = template.render(context)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="appointment.pdf"'

    # Generate PDF from HTML using ReportLab and pisa
    pisa_status = pisa.CreatePDF(html, dest=response)

    # Return the response
    if pisa_status.err:
        return HttpResponse('PDF generation failed', content_type='text/plain')
    return response


def beds(request):
    beds = Bed.objects.all()

    occupied_beds = []
    vacant_beds = []

    for bed in beds:
        occupied = IpdPatient.objects.filter(bed_number=bed.name) 

        if occupied.exists():
            patient = occupied.first()
            occupied_beds.append({'bed_number': bed.name, 'status': 'occupied', 'ipdpatient_id': patient.patient.id})
            # You can customize the dictionary based on your requirements
        else:
            vacant_beds.append({'bed_number': bed.name, 'status': 'vacant'})
            # You can customize the dictionary based on your requirements

    context = {
        'occupied_beds': occupied_beds,
        'vacant_beds': vacant_beds,
    }
    return render(request, 'beds/beds.html', context)


def emergency_patient(request):
    if request.method == 'POST':
        name = request.POST['name']
        date_of_birth = request.POST['date_of_birth']
        phone = request.POST['phone']
        gender = request.POST['gender']
        guardian_1 = request.POST.get('guardian_1')
        guardian_2 = request.POST.get('guardian_2')
        guardian_3 = request.POST.get('guardian_3')
        tpa = request.POST.get('tpa')
        cause = request.POST.get('cause')
        address = request.POST['address']

        # Create a new Patient instance and save it to the database
        patient = Patient(
            name=name,
            date_of_birth=date_of_birth,
            phone=phone,
            gender=gender,
            address=address,
            cause_of_emergebcy=cause,
            tpa=tpa,
            gardian_1=guardian_1,
            gardian_2=guardian_2,
            gardian_3=guardian_3,
            emergency=True,
        )
        patient.save()
        return redirect('emergency_patient')
    patient = Patient.objects.filter(emergency=True)
    context={
        'patient':patient,
    }
    return render(request,'patient/emergency.html',context)