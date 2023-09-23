from django.db import models
from django.contrib.contenttypes.fields import GenericRelation

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
# Create your models here.
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
    photo = models.ImageField(upload_to='staff_photos/', blank=True, null=True)
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
    payroll = models.CharField(max_length=100, blank=True, null=True)
    epf_no = models.CharField(max_length=20, blank=True, null=True)
    basic_salary = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    contract_type = models.CharField(max_length=100, blank=True, null=True)

    # Work Details
    work_shift = models.CharField(max_length=100, blank=True, null=True)
    work_location = models.CharField(max_length=100, blank=True, null=True)

    # Leave Information
    paid_leave = models.BooleanField(default=False)
    number_of_leaves = models.PositiveIntegerField(blank=True, null=True)

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
    patient = models.CharField(max_length=100,default=0)
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
    min_level = models.DecimalField(max_digits=10, decimal_places=2,blank=True,null=True)
    reorder_level = models.DecimalField(max_digits=10, decimal_places=2,blank=True,null=True)
    tax = models.DecimalField(max_digits=5, decimal_places=2,blank=True,null=True)
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


class Purchase_Med(models.Model):
    category = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    batch_no = models.CharField(max_length=50)
    expiry_date = models.DateField()
    mrp = models.DecimalField(max_digits=10, decimal_places=2)
    batch_amount = models.DecimalField(max_digits=10, decimal_places=2,blank=True,null=True)
    sale_price = models.DecimalField(max_digits=10, decimal_places=2)
    packing_qty = models.IntegerField(blank=True,null=True)
    quantity = models.IntegerField()
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2)
    tax_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

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
    
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2 ,default=0,)
    discount = models.DecimalField(max_digits=10,  default=0, decimal_places=2 )
    tax = models.DecimalField(max_digits=10,  default=0,  decimal_places=2)
    net_amount = models.DecimalField(max_digits=10,  default=0, decimal_places=2)
    payment_mode = models.CharField(max_length=255, choices=(('Cash', 'Cash'),))
    payment_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Donors'



class BloodDonation_component(models.Model):

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
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2 ,default=0,)
    discount = models.DecimalField(max_digits=10,  default=0, decimal_places=2 )
    tax = models.DecimalField(max_digits=10,  default=0,  decimal_places=2)
    net_amount = models.DecimalField(max_digits=10,  default=0, decimal_places=2)
    payment_mode = models.CharField(max_length=255, choices=(('Cash', 'Cash'),))
    payment_amount = models.DecimalField(max_digits=10, decimal_places=2)


  

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
    tax_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    standard_charge = models.DecimalField(max_digits=10, decimal_places=2)
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
        return "Service Type"
    

class Tax_cat(models.Model):
    tax_category = models.CharField(max_length=100,blank=True,null=True)
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
    payment_mode = models.CharField(max_length=255, choices=(('Cash', 'Cash'),))
    payment_amount = models.IntegerField(max_length=10)


    def __str__(self):
        return self.test_name
    

class MedicineCategory(models.Model):
    category_name = models.CharField(max_length=255)
    medicine = models.ForeignKey('Medicine', on_delete=models.CASCADE)
    dosage = models.CharField(max_length=255)
    dose_interval = models.CharField(max_length=255)
    dose_duration = models.CharField(max_length=255)
    instruction = models.CharField(max_length=255)

    def __str__(self):
        return self.category_name