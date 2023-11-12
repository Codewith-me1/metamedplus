from django.db import models
from django.contrib.contenttypes.fields import GenericRelation

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.auth.models import AbstractUser
from django.contrib.contenttypes.models import ContentType
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.
from datetime import timezone
class User(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)




class AppointmentDetails(models.Model):
  patient_name = models.CharField(max_length=255)
  appointment_no = models.CharField(max_length=255)
  appointment_date = models.DateTimeField()
  phone = models.CharField(max_length=255)
  gender = models.CharField(max_length=255)
  doctor = models.CharField(max_length=255)
  source = models.CharField(max_length=255)
  priority = models.CharField(max_length=255)
  fees = models.DecimalField(max_digits=10, decimal_places=2)
  status = models.CharField(max_length=255)

  class Meta:
    verbose_name = 'Appointment Details'
    verbose_name_plural = 'Appointment Details'

  def __str__(self):
    return self.patient_name
  

# models.py


class Patient(models.Model):
    id = models.AutoField(primary_key=True) 
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    Age = models.IntegerField(max_length=10,default=0)
    phone = models.CharField(max_length=15)
    gender = models.CharField(max_length=1, choices=[('M', 'Male'), ('F', 'Female')])
    address = models.CharField(max_length=200)
    # Add other patient-related fields here

    def __str__(self):
        return self.name



class AddStaff(models.Model):
    # Personal Information
    staff_id = models.CharField(max_length=100, unique=True)
    role = models.CharField(max_length=100)
    designation = models.CharField(max_length=100,blank=False,null=True)
    department = models.CharField(max_length=100,blank=False,null=True)
    specialist = models.CharField(max_length=100,blank=False,null=True)

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100, blank=True, null=True)
    mother_name = models.CharField(max_length=100, blank=True, null=True)   
    gender = models.CharField(max_length=10)
    marital_status = models.CharField(max_length=20)
    blood_group = models.CharField(max_length=5)
    date_of_birth = models.DateField()
    date_of_joining = models.DateField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    emergency_contact = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField()
    photo = models.FileField(upload_to='static/staff_photos', blank=True, null=True)
    current_address = models.TextField(blank=True, null=True)
    permanent_address = models.TextField(blank=True, null=True)

    # Qualifications and Experience
    qualification = models.TextField(blank=True, null=True)
    work_experience = models.TextField(blank=True, null=True)
    specialization = models.CharField(max_length=100, blank=True, null=True)
    note = models.TextField(blank=True, null=True)

    # Identification Numbers
    pan_number = models.CharField(max_length=20, blank=True, null=True)
    national_id_number = models.CharField(max_length=20, blank=True, null=True) 
    local_id_number = models.CharField(max_length=20, blank=True, null=True)

    # Payroll and Salary
    payroll_new = models.CharField(max_length=100, blank=True, null=True)
    epf_no = models.CharField(max_length=20, blank=True, null=True)
    basic_salary = models.IntegerField( max_length=10, blank=True, null=True,default='0')
    contract_type = models.CharField(max_length=100, blank=True, null=True)

    # Work Details
    work_shift = models.CharField(max_length=100, blank=True, null=True)
    work_location = models.CharField(max_length=100, blank=True, null=True)

    # Leave Information
    paid_leave = models.BooleanField(default=False)
    number_of_leaves = models.PositiveIntegerField(blank=True, null=True,default=0)

    # Bank Account Details
    account_title = models.CharField(max_length=100, blank=True, null=True)
    bank_account_no = models.CharField(max_length=20, blank=True, null=True)
    bank_name = models.CharField(max_length=100, blank=True, null=True)
    ifsc_code = models.CharField(max_length=20, blank=True, null=True)
    bank_branch_name = models.CharField(max_length=100, blank=True, null=True)

    # Social Media Links
    facebook_url = models.URLField(blank=True, null=True)
    twitter_url = models.URLField(blank=True, null=True)
    linkedin_url = models.URLField(blank=True, null=True)
    instagram_url = models.URLField(blank=True, null=True)

    # Documents
    resume = models.FileField(upload_to='staff_documents/', blank=True, null=True)
    joining_letter = models.FileField(upload_to='staff_documents/', blank=True, null=True)
    other_documents = models.FileField(upload_to='staff_documents/', blank=True, null=True)

    def __str__(self):
        return self.staff_id

class Role(models.Model):
    role = models.CharField(max_length=100,blank=True, null=True)
    designation = models.CharField(max_length=100,blank=True, null=True)
    department = models.CharField(max_length=100,blank=True, null=True)
    specialist = models.CharField(max_length=100,blank=True, null=True)


# BED 

class Floor(models.Model):
   name =  models.CharField(max_length=100)
   description = models.CharField(max_length=100,blank=True, null=True)



class BedGroup(models.Model):
   name =  models.CharField(max_length=100)
   floor = models.CharField(max_length=100)
   description = models.CharField(max_length=100,blank=True, null=True)

class Bedtype(models.Model):
   purpose = models.CharField(max_length=100)


class Bed(models.Model):
   name =  models.CharField(max_length=100)
   floor = models.CharField(max_length=100)
   purpose = models.CharField(max_length=100)
   mark_as_unused = models.BooleanField(default=False)
   



class IpdPatient(models.Model):
    id = models.AutoField(primary_key=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE,blank=True,null=True)
    height = models.FloatField()
    weight = models.FloatField()
    bp = models.CharField(max_length=20)
    pulse = models.IntegerField()
    temperature = models.FloatField(null=True,blank=True)
    respiration = models.IntegerField(null=True,blank=True)
    symptoms_type = models.CharField(max_length=255)
    symptoms_title = models.CharField(max_length=255)
    symptoms_description = models.CharField(max_length=255)
    admission_date = models.DateTimeField()
    is_case_casualty = models.BooleanField()
    is_old_patient = models.BooleanField()
    is_tpa = models.BooleanField()  
    credit_limit = models.DecimalField(max_digits=10, decimal_places=2)
    reference = models.CharField(max_length=255)
    consultant_doctor = models.CharField(max_length=255)
    bed_group = models.CharField(max_length=255)
    bed_number = models.CharField(max_length=10)






class Symtopms(models.Model):
    symptoms_type = models.CharField(max_length=255)
    symptoms_title = models.CharField(max_length=255)
    symptoms_description = models.CharField(max_length=255)


class Medicine(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    composition = models.CharField(max_length=255)
    group = models.CharField(max_length=255)
    unit = models.CharField(max_length=255)
    min_level = models.DecimalField(max_digits=13, decimal_places=3,blank=True,null=True)
    reorder_level = models.DecimalField(max_digits=13, decimal_places=3,blank=True,null=True)
    tax = models.DecimalField(max_digits=13, decimal_places=3,blank=True,null=True)
    unit_packing = models.CharField(max_length=255)
    vat_account = models.CharField(max_length=255,blank=True,null=True)
    note = models.TextField(blank=True, null=True)
    medicine_photo = models.ImageField(upload_to='medicine_photos/', blank=True, null=True)



class Med_Category(models.Model):
   medicine_category = models.CharField(max_length=100)


class Supplier(models.Model):
    supplier_name = models.CharField(max_length=255)
    supplier_contact = models.CharField(max_length=255,blank=True,null=True)
    contact_person_name = models.CharField(max_length=255,blank=True,null=True)
    contact_person_phone = models.CharField(max_length=20,blank=True,null=True)
    drug_license_number = models.CharField(max_length=50,blank=True,null=True)
    address = models.TextField(blank=True,null=True)

    def __str__(self):
        return self.supplier_name
    
class Med_Details(models.Model):
    category = models.CharField(max_length=255)
    dose = models.CharField(max_length=100)
    interval = models.CharField(max_length=100,null=True)
    duration = models.CharField(max_length=100,null=True)
    def __str__(self):
        return f"{self.category} - {self.dose}"


    
class Purchase(models.Model):
    category = models.ForeignKey(Med_Category, on_delete=models.CASCADE,blank=True,null=True) 
    name = models.CharField(max_length=255)
    batch_no = models.CharField(max_length=50)
    expiry_date = models.DateField()
    mrp = models.IntegerField(max_length=20)
    batch_amount = models.IntegerField(max_length=20,blank=True,null=True)
    sale_price = models.IntegerField(max_length=10)
    packing_qty = models.IntegerField(blank=True,null=True)
    quantity = models.IntegerField()
    purchase_price = models.IntegerField(max_length=20 )
    tax_percentage = models.IntegerField(max_length=20)
    amount = models.IntegerField(max_length=10)
    documents = models.ImageField(upload_to='medicine/', blank=True, null=True)
    note = models.TextField()


    total = models.IntegerField(max_length=10)
    discount_percentage = models.IntegerField(max_length=10 )
    discount = models.IntegerField(max_length=10 )
    tax = models.IntegerField(max_length=10)
    net_amount = models.IntegerField(max_length=10)
    payment_mode = models.CharField(max_length=255)
    payment_amount = models.IntegerField(max_length=10)


    def __str__(self):
        return self.name
    



class Donor_det(models.Model):
    id = models.AutoField(primary_key=True) 
    
    name = models.CharField(max_length=255, verbose_name='Donor Name')
    date_of_birth = models.DateField(verbose_name='Date of Birth')
    blood_group = models.CharField(max_length=3)
    gender = models.CharField(max_length=10)
    father_name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Father Name')
    contact_no = models.CharField(max_length=15, blank=True, null=True, verbose_name='Contact No')
    address = models.TextField(blank=True, null=True, verbose_name='Address')
    
    # total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    # discount_percentage = models.DecimalField(max_digits=5, decimal_places=2 ,default=0,)
    # discount = models.DecimalField(max_digits=10,  default=0, decimal_places=2 )
    # tax = models.DecimalField(max_digits=10,  default=0,  decimal_places=2)
    # net_amount = models.DecimalField(max_digits=10,  default=0, decimal_places=2)
    # payment_mode = models.CharField(max_length=255)
    # payment_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Donors'


    
class BloodDonation_component(models.Model):
    patient =  models.ForeignKey(Patient, on_delete=models.CASCADE,null=True)
    reference_name = models.CharField(max_length=255)
    issue_date = models.CharField(max_length=20,  )
    hospital_doctor = models.CharField(max_length=255,  blank=True, null=True)
    technician = models.CharField(max_length=255, blank=True, null=True)
    blood_group = models.CharField(max_length=3,  blank=True, null=True)
    bag = models.CharField(max_length=20, blank=True, null=True)
    charge_category = models.CharField(max_length=20,  blank=True, null=True)
    charge_name = models.CharField(max_length=255, blank=True, null=True)
    standard_charge = models.DecimalField(max_digits=10, decimal_places=2, default=0, blank=True, null=True)
    note = models.TextField( blank=True, null=True)
            
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    
    discount = models.DecimalField(max_digits=10,  default=0, decimal_places=2 )
    tax = models.DecimalField(max_digits=10,  default=0,  decimal_places=2)
   


  

    def __str__(self):
        return self.reference_name

#  Pathalogy

class Path_Category(models.Model):
    category_name = models.CharField(max_length=100,blank=True,null=True)
    unit = models.CharField(max_length=100,blank=True,null=True)

class Path_Parameter(models.Model):
    parameter_name = models.CharField(max_length=100,blank=True,null=True)
    range = models.CharField(max_length=100,blank=True,null=True)
    unit = models.CharField(max_length=100,blank=True,null=True)
    description = models.CharField(max_length=100,blank=True,null=True)


# Hospital Charges 
class Charge(models.Model):


    charge_type = models.CharField(max_length=100)
    charge_category = models.CharField(max_length=100)
    unit_type = models.CharField(max_length=100)
    charge_name = models.CharField(max_length=100)
    tax_category = models.CharField(max_length=100)
    tax_percentage = models.CharField(max_length=5)
    standard_charge = models.CharField(max_length=10)
    description = models.TextField(blank=True,null=True)

    def __str__(self):
        return self.charge_name

  


class Module_Charge(models.Model):
    charge_name = models.CharField(max_length=100)
    appointment = models.BooleanField(default=False)
    opd = models.BooleanField(default=False)
    ipd = models.BooleanField(default=False)
    pathology = models.BooleanField(default=False)
    radiology = models.BooleanField(default=False)
    blood_bank = models.BooleanField(default=False)
    ambulance = models.BooleanField(default=False)

    def __str__(self):
        return self.charge_name

class ChargeType(models.Model):
    charge_type = models.ForeignKey(Module_Charge,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Tax_cat(models.Model):
    tax_category = models.CharField(max_length=100,blank=True,null=True)
    percentage = models.IntegerField(max_length=100,default=12  )
    unit = models.CharField(max_length=100,blank=True,null=True)

class Pathology_test(models.Model):
    test_name = models.CharField(max_length=100)
    short_name = models.CharField(max_length=50)
    test_type = models.CharField(max_length=100, blank=True, null=True)
    category_name = models.CharField(max_length=100, blank=True, null=True)
    
    sub_category = models.CharField(max_length=100, blank=True, null=True)
    method = models.CharField(max_length=100, blank=True, null=True)
    report_days = models.PositiveIntegerField(default=0)
    
    charge_category = models.CharField(max_length=100, blank=True, null=True)
    charge_name = models.CharField(max_length=100, blank=True, null=True)
    tax_percentage = models.IntegerField(max_length=5, blank=True, null=True)
    standard_charge = models.IntegerField(max_length=10)
    amount = models.IntegerField(max_length=10)
    
    test_parameter_name = models.CharField(max_length=100)
    reference_range = models.CharField(max_length=100)
    unit = models.CharField(max_length=50)

    def __str__(self):
        return self.test_name
    


class Pathology(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE,null=True)
    test_name = models.CharField(max_length=255)
    report_days = models.PositiveIntegerField()
    report_date = models.DateField()
    tax_percentage = models.IntegerField(max_length=10)
    amount = models.IntegerField(max_length=10)
    referral_doctor = models.CharField(max_length=255)

    total = models.IntegerField(max_length=10)
    discount_percentage = models.IntegerField(max_length=10 )
    discount = models.IntegerField(max_length=10 )
    tax = models.IntegerField(max_length=10)
    net_amount = models.IntegerField(max_length=10)
    payment_mode = models.CharField(max_length=255)
    payment_amount = models.IntegerField(max_length=10)


    def __str__(self):
        return self.test_name


class Radiology(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE,null=True)
    test_name = models.CharField(max_length=255)
    report_days = models.PositiveIntegerField()
    report_date = models.DateField()
    tax_percentage = models.IntegerField(max_length=10)
    amount = models.IntegerField(max_length=10)
    referral_doctor = models.CharField(max_length=255)

    total = models.IntegerField(max_length=10)
    discount_percentage = models.IntegerField(max_length=10 )
    discount = models.IntegerField(max_length=10 )
    tax = models.IntegerField(max_length=10)
    net_amount = models.IntegerField(max_length=10)
    payment_mode = models.CharField(max_length=255)
    payment_amount = models.IntegerField(max_length=10)

    note = models.TextField(null=True)
    def __str__(self):
        return self.test_name

class MedicineCategory(models.Model):
    category_name = models.CharField(max_length=255)
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    dosage = models.CharField(max_length=255)
    dose_interval = models.CharField(max_length=255)
    dose_duration = models.CharField(max_length=255)
    instruction = models.CharField(max_length=255)

    def __str__(self):
        return self.category_name
    
class IncomeHead(models.Model):
    income_head = models.CharField(max_length=100)
    description = models.TextField(blank=True,null=True)


class ExpenseHead(models.Model):
    expense_head = models.CharField(max_length=100)
    description = models.TextField(blank=True,null=True)


class Income(models.Model):
    demo = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    invoice_number = models.CharField(max_length=255)
    date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    document = models.FileField(upload_to='income_documents/', blank=True, null=True)
    description = models.TextField()

    def __str__(self):
        return f"{self.demo} - {self.name}"
    

class Expense(models.Model):
    expense = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    invoice_number = models.CharField(max_length=255)
    date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    document = models.FileField(upload_to='expense_documents/', blank=True, null=True)
    description = models.TextField()

    def __str__(self):
        return f"{self.expense} - {self.name}"
    

class TPA(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20)
    contact_no = models.CharField(max_length=15)
    address = models.TextField()
    contact_person_name = models.CharField(max_length=100)
    contact_person_phone = models.CharField(max_length=15)



class ChildBirth(models.Model):
    child_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    child_photo = models.ImageField(upload_to='Birth/child_photos/', blank=True, null=True)
    birth_date = models.DateField()
    phone = models.CharField(max_length=15)
    address = models.TextField()
    case_id = models.CharField(max_length=20)
    mother_name = models.CharField(max_length=100)
    mother_photo = models.ImageField(upload_to='Birth/mother_photo/', blank=True, null=True)
    father_name = models.CharField(max_length=100, blank=True, null=True)
    father_photo = models.ImageField(upload_to='Birth/father_photo/', blank=True, null=True)
    report = models.TextField()
    document_photo = models.ImageField(upload_to='Birth/document_photos/', blank=True, null=True)


class DeathRecord(models.Model):
    case_id = models.CharField(max_length=20)
    patient_name = models.CharField(max_length=100)
    death_date = models.DateField()
    guardian_name = models.CharField(max_length=100)
    attachment = models.FileField(upload_to='death_attachments/', blank=True, null=True)
    report = models.TextField()


# Referral 

class ReferralCategory(models.Model):
    name = models.CharField(max_length=20)



class ReferralPerson(models.Model):
    referrer_name = models.CharField(max_length=255)
    referrer_contact = models.CharField(max_length=255)
    contact_person_name = models.CharField(max_length=255)
    contact_person_phone = models.CharField(max_length=15)
    category = models.CharField(max_length=255)
    standard_commission = models.DecimalField(max_digits=5, decimal_places=2,)
    address = models.TextField()
    commission_opd = models.DecimalField(max_digits=5, decimal_places=0,null=True,blank=True)
    commission_ipd = models.DecimalField(max_digits=5, decimal_places=0,null=True,blank=True)
    commission_pharmacy = models.DecimalField(max_digits=5, decimal_places=0,null=True,blank=True)
    commission_pathology = models.DecimalField(max_digits=5, decimal_places=0,null=True,blank=True)
    commission_radiology = models.DecimalField(max_digits=5, decimal_places=0,null=True,blank=True)
    commission_blood_bank = models.DecimalField(max_digits=5, decimal_places=0,null=True,blank=True)
    commission_ambulance = models.DecimalField(max_digits=5, decimal_places=0,null=True,blank=True)

    def __str__(self):
        return self.referrer_name   
    

class Referral(models.Model):

    patient = models.CharField(max_length=20,default=None)
    patient_type = models.CharField(max_length=255)
    bill_no = models.CharField(max_length=255)
    bill_amount = models.DecimalField(max_digits=10, decimal_places=2,null=True,blank=True)
    payee = models.CharField(max_length=255)
    commission_percentage = models.DecimalField(max_digits=5, decimal_places=2,null=True,blank=True)
    commission_amount = models.DecimalField(max_digits=10, decimal_places=2,null=True,blank=True)

    def __str__(self):
        return self.bill_no
    


class Ambulance(models.Model):

    vehicle_number = models.CharField(max_length=20)
    vehicle_model = models.CharField(max_length=255)
    year_made = models.IntegerField()
    driver_name = models.CharField(max_length=255)
    driver_license = models.CharField(max_length=20)
    driver_contact = models.CharField(max_length=15)
    vehicle_type = models.CharField(max_length=255)
    note = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.vehicle_number
    

    
class add_ambulancecall(models.Model):
    patient = models.CharField(max_length=100)
    vehicle_model = models.CharField(max_length=100)
    driver_name = models.CharField(max_length=100)
    date = models.DateField()
    charge_category = models.CharField(max_length=100)
    charge_name = models.CharField(max_length=100)
    standard_charge = models.DecimalField(max_digits=10, decimal_places=2)
    note = models.TextField()

    total = models.IntegerField(max_length=10)
    tax = models.IntegerField(max_length=10)
    net_amount = models.IntegerField(max_length=10)
    payment_mode = models.CharField(max_length=255)
    payment_amount = models.IntegerField(max_length=10)



class ItemCategory(models.Model):
    item_category = models.CharField(max_length=100)
    description = models.CharField(max_length=200)



class Store(models.Model):
    store_name = models.CharField(max_length=100)
    stock_code = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.store_name
    
class SupplierDetails(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20,null=True,blank=True)
    email = models.EmailField(null=True,blank=True)
    contact_person_name = models.CharField(max_length=100,null=True,blank=True)
    address = models.TextField(null=True,blank=True)
    contact_person_phone = models.CharField(max_length=20,null=True,blank=True)
    contact_person_email = models.EmailField(null=True,blank=True)
    description = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.name


class Item(models.Model):
    item = models.CharField(max_length=100)
    item_category = models.CharField(max_length=100)
    unit = models.CharField(max_length=50)
    description = models.TextField(null=True,blank=True)

    def __str__(self):  
        return self.item
    

class ItemStock(models.Model):
    item_category = models.CharField(max_length=100 ,blank=False)
    item = models.CharField(max_length=100)
    supplier = models.CharField(max_length=100)
    store = models.CharField(max_length=100, null=True , blank=True)
    quantity = models.PositiveIntegerField()
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(blank=True,null=True)
    description = models.TextField(blank=True,null=True)
    document = models.FileField(upload_to='documents/',blank=True,null=True )

    def __str__(self):
        return self.item


class Path_Category(models.Model):
    name = models.CharField(max_length=255,default=True)

class Radio_Category(models.Model):
    name = models.CharField(max_length=255,default=True)

class Path_Parameter(models.Model):
    parameter_name = models.CharField(max_length=255,null=True)
    reference_range = models.CharField(max_length=255,null=True)
    unit = models.CharField(max_length=50,null=True)
    description = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.parameter_name
    

class Radio_Parameter(models.Model):
    parameter_name = models.CharField(max_length=255,null=True)
    reference_range = models.CharField(max_length=255,null=True)
    unit = models.CharField(max_length=50,null=True)
    description = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.parameter_name
    


class Radiology_test(models.Model):
    test_name = models.CharField(max_length=100)
    short_name = models.CharField(max_length=50)
    test_type = models.CharField(max_length=100, blank=True, null=True)
    category_name = models.CharField(max_length=100, blank=True, null=True)
    
    sub_category = models.CharField(max_length=100, blank=True, null=True)
    method = models.CharField(max_length=100, blank=True, null=True)
    report_days = models.PositiveIntegerField(default=0)
    
    charge_category = models.CharField(max_length=100, blank=True, null=True)
    charge_name = models.CharField(max_length=100, blank=True, null=True)
    tax_percentage = models.IntegerField(max_length=5, blank=True, null=True)
    standard_charge = models.IntegerField(max_length=10)
    amount = models.IntegerField(max_length=10)
    
    test_parameter_name = models.CharField(max_length=100)
    reference_range = models.CharField(max_length=100)
    unit = models.CharField(max_length=50)

    def __str__(self):
        return self.test_name
    


class OpdPatient(models.Model):
    id = models.AutoField(primary_key=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE,blank=True,null=True)
    height = models.FloatField()
    weight = models.FloatField()
    bp = models.CharField(max_length=20)
    pulse = models.IntegerField()
    temperature = models.FloatField()
    respiration = models.IntegerField()
    symptoms_type = models.CharField(max_length=255)
    symptoms_title = models.CharField(max_length=255)
    symptoms_description = models.CharField(max_length=255)
    admission_date = models.DateTimeField()
    is_case_casualty = models.BooleanField()
    is_old_patient = models.BooleanField()
    is_tpa = models.BooleanField()
    credit_limit = models.DecimalField(max_digits=10, decimal_places=2)
    reference = models.CharField(max_length=255)
    consultant_doctor = models.CharField(max_length=255)

    charge_category = models.CharField(max_length=100, blank=True, null=True)
    charge_name = models.CharField(max_length=100, blank=True, null=True)
    tax_percentage = models.IntegerField(max_length=5, blank=True, null=True)
    standard_charge = models.IntegerField(max_length=10)
    amount = models.IntegerField(max_length=100)
    Applied_charges = models.IntegerField(max_length=100)
    paid_amount = models.IntegerField(max_length=100)
    note = models.TextField(null=True,blank=True)
    any_known = models.TextField(null=True,blank=True)


class NursingRecord(models.Model):
    date = models.DateField()
    nurse = models.CharField(max_length=100)
    note = models.TextField()
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE,null=True)
    comment = models.TextField()    


class DoctorNote(models.Model):
    date = models.DateField()
    doctor = models.CharField(max_length=100)
    note = models.TextField()
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE,null=True)
    comment = models.TextField()    


class MedicationDose(models.Model):
    patient =  models.ForeignKey(Patient, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    category = models.CharField(max_length=50)
    medicine_name = models.CharField(max_length=100)
    dosage = models.CharField(max_length=50)
    remarks = models.TextField()



class BloodDonation(models.Model):
    donor_name = models.CharField(max_length=100)
    donate_date = models.DateField()
    bag = models.CharField(max_length=50)
    volume = models.DecimalField(max_digits=5, decimal_places=2)
    unit_type = models.CharField(max_length=50)
    lot = models.CharField(max_length=50)
    charge_category = models.CharField(max_length=100)
    charge_name = models.CharField(max_length=100)
    standard_charge = models.DecimalField(max_digits=10, decimal_places=2)
    institution = models.CharField(max_length=100)
    note = models.TextField()


    total = models.IntegerField(max_length=10)
    discount_percentage = models.IntegerField(max_length=10 )
    discount = models.IntegerField(max_length=10 )
    tax = models.IntegerField(max_length=10)
    net_amount = models.IntegerField(max_length=10)
    payment_mode = models.CharField(max_length=255)
    payment_amount = models.IntegerField(max_length=10)

    def __str__(self):  
        return self.donor_name
    

class CustomUser(AbstractUser):
    USER_ROLE_CHOICES = (
        ('doctor', 'Doctor'),
        ('admin', 'Administrator'),
        # Add more role choices as needed
    )

    role = models.CharField(max_length=20, choices=USER_ROLE_CHOICES, default='doctor')


class Referral_commission(models.Model):


    category = models.CharField(max_length=20)
    standard_commission = models.IntegerField(max_length=10)
    commission_opd = models.DecimalField(max_digits=5, decimal_places=0,null=True,blank=True)
    commission_ipd = models.DecimalField(max_digits=5, decimal_places=0,null=True,blank=True)
    commission_pharmacy = models.DecimalField(max_digits=5, decimal_places=0,null=True,blank=True)
    commission_pathology = models.DecimalField(max_digits=5, decimal_places=0,null=True,blank=True)
    commission_radiology = models.DecimalField(max_digits=5, decimal_places=0,null=True,blank=True)
    commission_blood_bank = models.DecimalField(max_digits=5, decimal_places=0,null=True,blank=True)
    commission_ambulance = models.DecimalField(max_digits=5, decimal_places=0,null=True,blank=True)

    

    def __str__(self):
        return self.category
    


class Task(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()




class Payroll(models.Model):
    staff = models.ForeignKey(AddStaff, on_delete=models.CASCADE)
    earning = models.IntegerField(default=0)
    deduction = models.IntegerField(default=0)
    gross_salary = models.IntegerField(default=0)
    tax_percentage = models.FloatField( default=0.00)
    tax = models.IntegerField(default=0)
    net_salary = models.IntegerField(default=0)


class Zoom(models.Model):
    title = models.CharField(max_length=255)
    meeting_date = models.DateField()
    duration_minutes = models.PositiveIntegerField()
    host_video = models.BooleanField(default=True)
    client_video = models.BooleanField(default=True)
    description = models.TextField()
    staff_list = models.TextField()  # You can use a TextField to store a list of staff members

    def __str__(self):
        return self.title
    



class Party(models.Model):
    part_name = models.CharField(max_length=255)
    gstin = models.CharField(max_length=15,null=True,blank=True)
    phone_number = models.CharField(max_length=15,null=True,blank=True)
    gst_type = models.CharField(max_length=10)
    state = models.CharField(max_length=255)
    email_id = models.EmailField()
    billing_address = models.TextField()
    opening_balance = models.DecimalField(max_digits=13, decimal_places=3)
    as_of_date = models.DateField()
    to_pay = models.BooleanField(default=False)  # To Pay as a Boolean Field
    to_receive = models.BooleanField(default=False)


class Category(models.Model):
        category = models.CharField(max_length=20)






class Sales_Invoice(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    invoice_number = models.CharField(max_length=10)
    invoice_date = models.DateField()
    type = models.CharField(max_length=100,default='sales')
    payment_type = models.CharField(max_length=100,default='cash')
    state_of_supply = models.CharField(max_length=255)
    due_date = models.DateField(auto_now_add=True,null=True)
    balance = models.IntegerField(max_length=20,null=True,blank=True)
    advance_amount = models.CharField(max_length=20,default=True,null=True)
    total = models.DecimalField(max_digits=13, decimal_places=3,null=True)
    
    def __str__(self):
        return self.due_date



class Item_Invoice(models.Model):
    invoice = models.ForeignKey(Sales_Invoice, on_delete=models.CASCADE)
    item = models.CharField(max_length=255) 
    qty = models.DecimalField(max_digits=13, decimal_places=3)
    unit = models.CharField(max_length=13)
    price = models.DecimalField(max_digits=13, decimal_places=3)
    
    discount = models.DecimalField(max_digits=13, decimal_places=3)
    discount_amount = models.DecimalField(max_digits=13, decimal_places=3)
    tax = models.DecimalField(max_digits=5, decimal_places=3)
    tax_amount = models.DecimalField(max_digits=10, decimal_places=3)
    total = models.DecimalField(max_digits=13, decimal_places=3)



class Item_Acc(models.Model):
    item_name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)

    item_image = models.ImageField(upload_to='item_images/', blank=True, null=True)
    sale_price = models.IntegerField(max_length=20)
    disc_on_sale_price = models.DecimalField(max_digits=13, decimal_places=3, default=0)
    unit = models.CharField(max_length=100,blank=True, null=True)
    purchase_price = models.DecimalField(max_digits=13, decimal_places=3)
    tax_rate = models.DecimalField(max_digits=13, decimal_places=3)
    opening_quantity = models.DecimalField(max_digits=13, decimal_places=3)
    at_price = models.DecimalField(max_digits=13, decimal_places=3)
    as_of_date = models.DateField()
    min_stock_to_maintain = models.DecimalField(max_digits=13, decimal_places=3)
    location = models.CharField(max_length=255)



class Unit(models.Model):
    unit_name = models.CharField(max_length=255)



class Asset(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True,blank=True)    
    price = models.DecimalField(max_digits=13, decimal_places=3)  # Add a price field
    asset_type = models.CharField(max_length=20)
    

    def __str__(self):
        return self.name


class Liablity(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True,blank=True)    
    price = models.DecimalField(max_digits=13, decimal_places=3)  # Add a price field
    liablity_type = models.CharField(max_length=20)
    

    def __str__(self):
        return self.name
    
    

class MedicationDoseage(models.Model):
    date = models.DateField()
    time = models.TimeField()
    medicine_category = models.CharField(max_length=100)
    medicine_name = models.CharField(max_length=100)
    dosage = models.CharField(max_length=50)
    remarks = models.TextField()
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.medicine_name} - {self.date} {self.time}"


class Consultant_register(models.Model):
    patient = models.ForeignKey(Patient,on_delete=models.CASCADE,null=True)
    applied_date = models.DateField()
    instruction_date = models.DateField()
    consultant_doctor = models.CharField(max_length=100)
    instruction = models.TextField()


class Operation(models.Model):
   
    patient = models.ForeignKey(Patient,on_delete=models.CASCADE)
    operation_category = models.CharField(max_length=50)
    operation_name = models.CharField(max_length=100)
    operation_date = models.DateField()
    consultant_doctor = models.CharField(max_length=100)
    assistant = models.CharField(max_length=50,null=True)
    assistant2 = models.CharField(max_length=50,null=True)

    anesthesia_type = models.CharField(max_length=100, blank=True)
    ot_technician = models.CharField(max_length=100, blank=True)
    ot_assistant = models.CharField(max_length=100, blank=True)
    remark = models.TextField(blank=True)
    result = models.TextField(blank=True)

    def __str__(self):
        return f"{self.operation_name} - {self.operation_date}"
    



    
class Ipd_Payments(models.Model):
    date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    patient = models.ForeignKey(Patient,on_delete=models.CASCADE)
    payment_mode = models.CharField(max_length=10)
    note = models.TextField(blank=True)

    def __str__(self):
        return f"Payment on {self.date} - ${self.amount}"



class Expense_Category(models.Model):
    expense_category = models.CharField(max_length=100)
    expense_type = models.CharField(max_length=20)
    




class Expense_Invoice(models.Model):

    invoice_number = models.CharField(max_length=10)
    invoice_date = models.DateField()
    expense_category = models.ForeignKey(Expense_Category,on_delete=models.CASCADE)
    balance = models.IntegerField(max_length=20,null=True,blank=True)
    total = models.DecimalField(max_digits=13, decimal_places=3,null=True)
    payment_type = models.CharField(max_length=20)


class Expense_inv_Item(models.Model):
    invoice = models.ForeignKey(Expense_Invoice, on_delete=models.CASCADE)
    item = models.CharField(max_length=255) 
    qty = models.DecimalField(max_digits=13, decimal_places=3)
    unit = models.CharField(max_length=13)
    price = models.DecimalField(max_digits=13, decimal_places=3)
    total = models.DecimalField(max_digits=13, decimal_places=3)




class Expense_Item(models.Model):
    item_name = models.CharField(max_length=255)

    
    price = models.DecimalField(max_digits=13, decimal_places=3)
    tax = models.DecimalField(max_digits=13, decimal_places=3)
   



class Payment_In(models.Model):
    name = models.CharField(max_length=20)
    
    payment_type = models.CharField(max_length=50)
    receipt_no = models.CharField(max_length=10)
    date = models.DateField()
    received = models.DecimalField(max_digits=10, decimal_places=2)




    
class BankAccount(models.Model):
    
    account_number = models.CharField(max_length=20, unique=True)
    balance = models.DecimalField(max_digits=13, decimal_places=3)
    as_of_date=models.DateField()



class Transaction(models.Model):
    account = models.ForeignKey(BankAccount, on_delete=models.CASCADE)
    transaction_type = models.CharField(max_length=10)  # 'Deposit' or 'Withdrawal'
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)



class SMTPServer(models.Model):
    name = models.CharField(max_length=100)
    host = models.CharField(max_length=100)
    port = models.PositiveIntegerField()
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class header(models.Model):
    name = models.CharField(max_length=20,default="Your Hospital Name")
    image = models.ImageField(upload_to='static/cms')



class Ads(models.Model):
    ads = models.ImageField(upload_to="static/ads")




class Notice(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    

class ChatRoom(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

class ChatMessages(models.Model):
    receiver = models.ForeignKey(CustomUser, on_delete=models.CASCADE,related_name='receiver_person')
    sender = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    content = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)



class Wallet(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return self.user.username
    

class Wallet_Transactions(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)


@receiver(post_save, sender=User)
def create_user_wallet(sender, instance, created, **kwargs):
    if created:
        Wallet.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_wallet(sender, instance, **kwargs):
    instance.wallet.save()