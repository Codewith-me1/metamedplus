from django.shortcuts import render
from decimal import Decimal
# Create your views here.
import decimal
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
from .models import Donor_det,BloodDonation_component
from .models import Path_Category,Path_Parameter
from django.contrib.contenttypes.models import ContentType
from . models import Charge
from .models import Module_Charge
from .models import Tax_cat 
from .models import Pathology_test
from .models import MedicineCategory
from .models import Pathology
appin = "appointment"




def adminapp(request):
  
  return render(request,'main/new.html')
# Create your views here.

def index(request):
   return render(request,'index.html')

# Appointment 

def appointment(request):
  

  appointments = AppointmentDetails.objects.all()


  context = {
    'appointments': appointments,
    
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
        designation = request.POST.get('designation')
        department = request.POST.get('department')
        specialist = request.POST.get('specialist')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        father_name = request.POST.get('father_name')
        mother_name = request.POST.get('mother_name')
        gender = request.POST.get('gender')
        marital_status = request.POST.get('marital_status')
        blood_group = request.POST.get('blood_group')
        date_of_birth = request.POST.get('date_of_birth')
        date_of_joining = request.POST.get('date_of_joining')
        phone = request.POST.get('phone')
        emergency_contact = request.POST.get('emergency_contact')
        email = request.POST.get('email')
        current_address = request.POST.get('current_address')
        permanent_address = request.POST.get('permanent_address')

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
            permanent_address=permanent_address,
            # Add other fields here
        )

        # Save the Staff object to the database
        staff.save()
        

        # Redirect to a success page or staff list page
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
   return render(request,"hr/role.html")


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
        role = Role.objects.all()
        context ={
           "role":role
        }
        return render(request,"hr/role_list.html",context)
       else:
        # Render the form for adding staff information
        return render(request, 'hr/hr.html')
    

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
    context = {
           "bed": beds,
            "bed_grp": beds,
            'bed_pur':bed_pur
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
        beds = BedGroup.objects.all()
        context = {
           "bed_grp": beds,
        }
        return render(request,'ipd/add_bed.html',context)  # Redirect to bed details page

    return render(request, 'ipd/add_bed.html')


def add_purpose(request):
    
    if request.method == 'POST':
        purpose  = request.POST.get('purpose')
        

        
        bed = Bedtype(
     
            purpose=purpose,

            
            # Add other fields here
        )

        bed.save()
        beds = Bedtype.objects.all()
        context = {
           "bed_pur": beds,
        }
        return render(request,'ipd/add_bed.html',context)  # Redirect to bed details page

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
        beds = Floor.objects.all()
        context = {
           "bed_floor": beds,
        }
        return render(request,'ipd/add_bed.html',context)  # Redirect to bed details page

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

        patient = IpdPatient(
            patient_name = patient_name,
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
        patient.save()
        doctors = AddStaff.objects.filter(designation='doctor')
        type = IpdPatient.objects.all()
        bedtype = Bedtype.objects.all()
        bed = Bed.objects.all()
        patient =  Patient.objects.filter(name=patient_name)
        context = {
            "type":type,
            "doctor":doctors,
            'bedtype':bedtype,
            'bed':bed,
            "patient":patient
        }
        return render(request,'ipd/dashboard.html',context)  # Redirect to a success page
    type = Symtopms.objects.all()
    bedtype = BedGroup.objects.all()
    bed = Bed.objects.all()
    patient =  Patient.objects.filter(name=patient_name)
    context = {
        "type": type,
        "doctor":doctors,
        'bedtype':bedtype,
        'bed':bed,
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

        total = (request.POST.get('total'))
        discount_percentage = (request.POST.get('discount_percentage'))
        discount = (request.POST.get('discount'))
        tax = (request.POST.get('tax'))
        net_amount = (request.POST.get('net_amount'))
        payment_amount = (request.POST.get('payment_amount'))

        donor = Donor_det(
            name = name,
            date_of_birth = date_of_birth,
            blood_group =blood_group,
            gender = gender,
            father_name = father_name,
            contact_no=contact_no,
            address = address,

            total = total,
            discount_percentage = discount_percentage,
            discount=discount,
            tax = tax,
            net_amount = net_amount,
            payment_amount = payment_amount,


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
        discount = (request.POST.get('discount'))
        tax = (request.POST.get('tax'))
        net_amount = (request.POST.get('net_amount'))
        payment_amount = (request.POST.get('payment_amount'))


        blood_donation = BloodDonation_component(
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
            discount_percentage = discount_percentage,
            discount=discount,
            tax = tax,
            net_amount = net_amount,
            payment_amount = payment_amount,

        )
        blood_donation.save()
        blood = BloodDonation_component.objects.all()
        context = {
        'blood' : blood,
         }
        return render(request, 'blood/issue_blood.html',context)#  Redirect to a list view or another page
    blood = BloodDonation_component.objects.all()
    context = {
        'blood' : blood,
    }
    return render(request, 'blood/issue_blood.html',context)



def issue_comp(request):
    if request.method == 'POST':
        category_name = request.POST.get('category_name', '')
        unit = request.POST.get('unit', '')

        product =Path_Category(category_name=category_name, unit=unit)
        product.save()
        comp = Path_Category.objects.all()
        context = {
        'comp' : comp,
        }
        return render(request, 'blood/issue_com.html',context)
    comp = Path_Category.objects.all()
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

        return render(request,'hospital/add_charge.html',context)  # Redirect to a list view or another page
    charge = Charge.objects.all()
    context = {
            'charge':charge
        }
    return render(request, 'hospital/add_charge.html',context)



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

        # Create a new instance of YourModel
        your_model_instance = Tax_cat(
            tax_category=tax_category,
            unit=unit,
        )
        your_model_instance.save()  # Save the object to the database

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
    context = {
        'test':test,
        "doc":doc,
        'charge':charge
    }
    return render(request, 'pathalogy/path_test.html',context)

def Pathology_Index(request):
    if request.method == 'POST':
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
    context = {
        'path':path,
        "doc":doc,
    }
    return render(request, 'pathalogy/pathalogy.html',context)

def ipd_dashboard(request,ipd_id):
    ipd = IpdPatient.objects.filter(pk=ipd_id)
    return render(request,'ipd/pat_dash.html',{"ipd":ipd})

def ipd_pat(request):
    ipd = IpdPatient.objects.all()
    context ={
        'ipd':ipd
    }
    return render(request,'ipd/dashboard.html',context)


def process_medicine_category(request):
   
    medicine = Medicine.objects.all()
    # Handle other HTTP methods or form validation errors if needed
    return render(request, 'ipd/precaution.html',{"medicine":medicine})

def pre(request):
     if request.method == 'POST':
        category_name = request.POST.get('category_name')
        medicine_id = request.POST.get('medicine')
        dosage = request.POST.get('dosage')
        dose_interval = request.POST.get('dose_interval')
        dose_duration = request.POST.get('dose_duration')
        instruction = request.POST.get('instruction')

        # Create a new MedicineCategory instance
        medicine_category = MedicineCategory(
            category_name=category_name,
            medicine_id=medicine_id,
            dosage=dosage,
            dose_interval=dose_interval,
            dose_duration=dose_duration,
            instruction=instruction
        )
        medicine_category.save()

        # Redirect to a success page or display a success message
        
        return redirect('ipd_dat')