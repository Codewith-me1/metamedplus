from django.shortcuts import render
from decimal import Decimal
# Create your views here.
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from django.shortcuts import get_object_or_404
from .models import SMTPServer
from django.urls import reverse
from .models import Message
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
from .models import Radio_Category,Radio_Parameter, Radiology_test
import secrets
import string
appin = "appointment"

def profile(request,id):

    staff  = AddStaff.objects.get(staff_id=id)
    
    
    try:
        payroll = Payroll.objects.get(staff=id)
        context = {
            'payroll':payroll
        }
    except Payroll.DoesNotExist:
            # Handle the case where the patient does not exist
            print('none found')
    
    context ={
        'staff':staff,
        
    }
    return render(request,'admin/admin_profile.html',context)



from django.contrib.auth import authenticate
from django.contrib.auth import login as log
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm

def login(request):
     if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        man = [form.data]
        print(man)
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(password)
        print(username)
        user = authenticate( request,username=username, password=password)
        print(user)
        
        if user is not None:
            log(request, user)  # Corrected login function call
            if user.role == 'doctor':
                return render(request, 'doctor/dashboard.html')  # Redirect to the doctor's dashboard
            elif user.role == 'Admin':
                return redirect('add_staff') 
            elif user.role == 'New':
                return redirect('doctor')
            elif user.role =='Manooj':
                return redirect('doctor')
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
  doctors = AddStaff.objects.filter(designation='doctor')
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
        staff.save()
    

        # Redirect to a success page or staff list page
        password = generate_random_password()

        User = CustomUser.objects.create_user(id=staff_id,username=email, email=email, password="password", role=role)
        message = "Your Password Is " + password
        subject = "Password"
        print(password)
        # send_email(message,email,subject)
        

        User.save()
        
        return HttpResponse("Staff information saved successfully.")
       

    else:
        # Render the form for adding staff information
        role = Role.objects.all()
        context = {
           "role":role, 
        }
       
        return render(request, 'hr/hr.html',context)
    


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

        # Create a Staff object and save it to the database
        staff = Role(
          
            role=role,
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
    return render(request,'panels/doctor.html')
def search_staff(request):
    if 'q' in request.GET:
        query = request.GET['q']
        results = AddStaff.objects.filter(role__icontains=query)
    else:
        results = None

    return render(request, 'hr/staff_search.html', {'results': results})




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

        return HttpResponse('Hello Done')  # Redirect to a success page

    return render(request, 'ipd/systoms.html')


from django.shortcuts import render, redirect
from .models import Patient

def ipd_patient(request):
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
            bed_group=bed_group,
            bed_number=bed_number,
        )
        ipd.save()
        doctors = AddStaff.objects.filter(role='Doctor')
        type = IpdPatient.objects.all()
        bedtype = Bedtype.objects.all()
        bed = Bed.objects.all()
        ipd = IpdPatient.objects.all()
        patient =  Patient.objects.all()
        context = {
            "type":type,
            "doctor":doctors,
            'bedtype':bedtype,
            'bed':bed,
            'ipd':ipd,
            "patient":patient
        }
        return render(request,'ipd/dashboard.html',context)  # Redirect to a success page
    type = Symtopms.objects.all()
    bedtype = BedGroup.objects.all()
    bed = Bed.objects.all()
    patient =  Patient.objects.all()
    doctors = AddStaff.objects.filter(designation="doctor")
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
        context = {
            "med":med,
        }
        return render(request,'pharmacy/medicine/add_med.html',context)  # Redirect to a success page

    return render(request, 'pharmacy/medicine/add_med.html')


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
    doctor = AddStaff.objects.filter(designation="doctor")
    bag = BloodDonation.objects.all()
    context = { 
        'blood' : blood,
        'patient':patient,
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
        charge_name = request.POST.get('charge_name', '')
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
        charge_type = request.POST['charge_type']
        name = request.POST['name']
        description = request.POST['description']

        charge_type = get_object_or_404(Module_Charge,charge_name=charge_type)
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
    doc =  AddStaff.objects.filter(designation='doctor')
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
        discount_percentage = (request.POST.get('discount_percentage',0))
        discount = (request.POST.get('discount',0))
        tax = (request.POST.get('tax',0))
        net_amount = (request.POST.get('net_amount',0))
        payment_amount = (request.POST.get('payment_amount',0))

        try:
            patient = Patient.objects.get(id=patient)
        except Patient.DoesNotExist:
            # Handle the case where the patient does not exist
            return render(request, 'myapp/radiology_form.html', {'error_message': 'Patient not found'})
        pathology_test = Pathology(
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
        )
        pathology_test.save()
        return redirect('path')
    path = Pathology.objects.all()
    doc =  AddStaff.objects.filter(designation='doctor')
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
            weight=weight,
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
        
       
        attachment = request.FILES.get('attachment')
        
        death = DeathRecord(
            case_id=case_id,
            patient_name=patient_name,
            death_date=death_date,
            guardian_name=guardian_name,
            attachment=attachment,
            report=report
        )
        death.save()
    patient = Patient.objects.all()
    context ={
        "patinet":patient,
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
    
    parameter = Path_Parameter.objects.all()
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
    doc =  AddStaff.objects.filter(designation='doctor')
    patient= Patient.objects.all()
    context = {
        'radio':radio,
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
    doc =  AddStaff.objects.filter(designation='doctor')
    charge = Charge.objects.all()
    category = Radio_Category.objects.all()
    parameter = Radio_Parameter.objects.all()
    context = {
        'test':test,
        "doc":doc,
        'charge':charge,
        'category':category,    
        'parameter':parameter,
    }
    return render(request, 'radiology/radio_test.html',context)


def get_tax_info(request):

    try:
        selected =  request.GET.get('test_name')
        parameter = Pathology_test.objects.get(test_name=selected)
        data = {
            'tax': parameter.tax_percentage,
            'standard_charge': parameter.standard_charge,
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
        note = request.POST['note']
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
    doctors = AddStaff.objects.filter(designation="doctor")
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

        # Create a new Medicine object and save it to the database
        medicine = purchase(
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
    context ={
        'medicine':medicine,
        "cat":medicineCat,
        'med':med
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
        patient = get_object_or_404(Patient, id=patient)
        # Create a new NursingRecord object and save it to the database
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
        doctor = request.POST.get('nurse')
        note = request.POST.get('note')
        comment = request.POST.get('comment')
        patient = get_object_or_404(Patient, id=patient)
        # Create a new NursingRecord object and save it to the database
        nursing_record = NursingRecord(
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
    ipd = IpdPatient.objects.filter(pk=ipd_id)
    nurse= NursingRecord.objects.all()
    staff = AddStaff.objects.filter(designation="nurse")
    doctor  = AddStaff.objects.filter(designation="doctor")
    medicine = MedicationDoseage.objects.all()
    consultant = Consultant_register.objects.all()
    operation = Operation.objects.all()
    payment = Ipd_Payments.objects.all()

    context ={
        'nurse':nurse,
        'staff':staff,
        'ipd':ipd,
        'doctor':doctor,
        'medicine':medicine,
        'consultant':consultant,
        'operation':operation,
        'payment':payment
    }
    return render(request,'ipd/pat_dash.html',context)



def add_medication_record(request):
    if request.method == 'POST':
        # Retrieve form data from POST request
        date = request.POST.get('date')
        time = request.POST.get('time')
        category = request.POST.get('category')
        medicine_name = request.POST.get('medicine_name')
        dosage = request.POST.get('dosage')
        remarks = request.POST.get('remarks')

        # Create a new MedicationRecord object and save it to the database
        medication_record = MedicationDose(
            date=date,
            time=time,
            category=category,
            medicine_name=medicine_name,
            dosage=dosage,
            remarks=remarks
        )
        medication_record.save()

    return render(request, 'your_app/medication_record_form.html')




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

        blood_donation = BloodDonation(
            donor_name=donor_name,
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
        asset = Asset(name=name, description=description,asset_type=asset_type, price=price,)
        asset.save()
        return redirect("create_asset")  # Redirect to a list view of assets
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
        patient = get_object_or_404(Patient, id=id)
        # Create a new NursingRecord object and save it to the database
       
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
        patient = get_object_or_404(Patient, id=id)

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
        operation_assistant = request.POST['operation_assistant']
        anesthesia_type = request.POST.get('anesthesia_type', '')
        ot_technician = request.POST.get('ot_technician', '')
        ot_assistant = request.POST.get('ot_assistant', '')
        assistant2 = request.POST.get('assistant2', '')
        remark = request.POST.get('remark', '')
        result = request.POST.get('result', '')
        patient = get_object_or_404(Patient, id=id)



        operation = Operation(
            patient=patient,
            operation_category=operation_category,
            operation_name=operation_name,
            operation_date=operation_date,
            ot_assistant=ot_assistant,
            consultant_doctor=consultant_doctor,
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
        

    return HttpResponse('Not Done ')





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

    context = {
        "transcation":transcation,
        'payment':payment_in,
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
        
        
        invoice_number = request.POST.get('invoice_number')
        invoice_date = request.POST.get('invoice_date')
        expense_category = request.POST.get('expense_category')
        names = re.sub(r'\d', '',name)
        name  = names.replace("_", "")
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
    
    print(total)
    total_long_term_assets = Asset.objects.filter(asset_type='Long-Term').aggregate(
        total_long_term_assets=Sum('price')
    )['total_long_term_assets'] or 0


    indirect_expense = Expense_Category.objects.filter(expense_category='indirect_expense').aggregate(
        total_indirect=Sum(F('expense_invoice'))
    )['total_indirect'] or 0

    direct_expense = Expense_Category.objects.filter(expense_category='direct_expense').aggregate(
        total_direct=Sum(F('expense_invoice'))
    )['total_direct'] or 0

    total_back_account = BankAccount.objects.all().aggregate(
        total_balance=Sum(F('balance'))
    )['total_balance'] or 0
    withdraw = Transaction.objects.filter(transaction_type='Withdrawl').aggregate(
        total_withdrawl= Sum(F('amount'))
    )['total_withdrawl']or 0

    closing_stock = opening_stock + total_purchases - total_sales
    equity =   opening_stock + total_receivable  + total_back_account -withdraw

    balance = (total_sales - total_purchases) + (total_sales_tax - total_purchase_tax) + closing_stock + total_short_term_assets + total_long_term_assets -indirect_expense+direct_expense +equity

    


    context = {
        'total_sales': total_sales,
        'total_purchases': total_purchases,
        'balance': balance,
        'opening_stock': opening_stock,
        'closing_stock': closing_stock,
        'total_sales_tax': total_sales_tax,
        'total_short_term_assets': total_short_term_assets,
        'total_long_term_assets': total_long_term_assets,
        'total_purchase_tax': total_purchase_tax,
        'start_date':start_date,
        'receivable':total_receivable,
        'payable':total_payable,
        'indirect_expense':indirect_expense,
        'direct_expense':direct_expense,
        'withdraw':withdraw,
        'equity':equity,
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
        account = BankAccount.objects.get(id=id)
        account.balance += amount
        account.save()
        Transaction.objects.create(account=account, transaction_type='Deposit', amount=amount)

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
    return render(request, 'withdrawal.html')




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

    
    indirect_expense = Expense_Category.objects.filter(expense_category='indirect_expense').aggregate(
        total_indirect=Sum(F('expense_invoice'))
    )['total_indirect'] or 0

    direct_expense = Expense_Category.objects.filter(expense_category='direct_expense').aggregate(
        total_direct=Sum(F('expense_invoice'))
    )['total_direct'] or 0

  
    total_short_term_assets = Asset.objects.filter(asset_type='Short-Term').aggregate(
        total_short_term_assets=Sum('price')
    )['total_short_term_assets'] or 0

    closing_stock = Sales_Invoice.objects.filter(type='sales').aggregate(
        total_short_term_assets=Sum('item_invoice')
    )['total_short_term_assets'] or 0

    


    # Calculate Gross Profit
    gross_profit = total_sales - total_return - direct_expense

    # Calculate Net Profit
    closing= opening_stock + total_purchase - closing_stock

    net_profit = gross_profit  - direct_expense

    return render(request, 'accounts/report/profit_loss.html', {
        'sales': total_sales,
        'credit_notes': total_return,
        'opening_stock': opening_stock,
        'closing_stock': closing_stock,
        'direct_expenses': direct_expense,
        'tax_payable': total_purchase_tax,
        'short_asset':total_short_term_assets,
        'tax_receivable': total_sales_tax,
        'indirect_expenses': indirect_expense,
        'gross_profit': gross_profit,
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



def send_email(message_text,recipient,subject):
    
    
    server = SMTPServer.objects.get(pk=1)

        # Creating an SMTP connection
    try:
            smtp_connection = smtplib.SMTP(server.host, server.port)
            smtp_connection.starttls()
            smtp_connection.login(server.username, server.password)

            # Composing the email
            msg = MIMEMultipart()
            msg['From'] = server.username
            msg['To'] = recipient
            msg['Subject'] = subject
            msg.attach(MIMEText(message_text,'plain'))

            # Sending the email
            smtp_connection.sendmail(server.username, recipient, msg.as_string())
            smtp_connection.quit()

            return HttpResponse('Email sent successfully!')
    except Exception as e:
            return HttpResponse(f'Error sending email: {str(e)}')




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



def search_patient(request):
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
    return render(request, 'hr/edit_staff.html', {'staff': staff})



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
        data_list.append({
            'name': bed.name,
            # Add more fields here if needed
        })

    if data_list:
        return JsonResponse(data_list, safe=False)
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
        notice = Notice(title=title, content=content)
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



def send_message(request, receiver_id):
    if request.method == 'POST':
        content = request.POST['content']
        receiver = AddStaff.objects.get(pk=receiver_id)
        Message.objects.create(sender=request.user, receiver=receiver, content=content)
        return redirect('message_list')

    receiver = AddStaff.objects.get(pk=receiver_id)
    return render(request, 'messaging/send_message.html', {'receiver': receiver})


def message_list(request):
    user_messages = Message.objects.filter(receiver=request.user).order_by('-timestamp')
    return render(request, 'messaging/message_list.html', {'user_messages': user_messages})


def calculator_view(request):
    return render(request, 'others/calculator.html')