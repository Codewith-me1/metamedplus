

from django.urls import path
from . import views

urlpatterns = [
    path('members/', views.adminapp, name='members'),
    path("app/",views.appointment,name="appointment"),
    path("index/",views.index,name="index"),
    path("appForm/",views.appointmentForm,name="appointmentForm"),
    path('appointment_details_form/', views.appointment_details_form_view, name='appointment_details_form'),
    path('patient/form/', views.patient_form, name='patient_form'),
    path('patient/list/', views.patient_list, name='patient_list'),
    path('hr/form/', views.add_staff, name='add_staff'),
    path('hr/list/', views.staff, name='staff_list'),
    path('hr/role/', views.role, name='role'),
    path('hr/role/form/', views.role_form, name='role_form'),
    path('search/', views.search_staff, name='search-staff'),
    path('add_bed/', views.add_bed, name='add_bed'),
    path('add_group/', views.add_bedGroup, name='add_bed_group'),
    path('add_purpose/', views.add_purpose, name='add_purpose'),
    path('add_floor/', views.add_floor, name='add_floor'),
    path('patient/dashboard',views.ipd_dash,name="ipd_dash"),
    path('systoms/', views.submit_symptom, name='submit_symptom'),
    path('ipd/',views.ipd_patient,name="ipd_patient"),
    path('add_med',views.submit_medicine,name="add_med"),
    path('supplier-form/', views.supplier_form, name='supplier_form'),
    path('med-det/', views.medicationDetails_form, name='med_det'),
    path('med-cat/', views.medicineCategory, name='med_cat'),
    path('add_donor/', views.add_donor, name='add_donor'),
    path('show/', views.show, name='s   ow'),
    path('issue_blood/', views.add_blood_donation, name='issue_blood'),
    path('issue_comp/', views.issue_comp, name='issue_comp'),
    path('add_charge/', views.add_charge, name='add_charge'),
    path('charge_name/', views.charge_name, name='charge_name'),
    path('tax_cat/', views.tax_category, name='tax_cat'),
    path('path_test/', views.path_test, name='path_test'),
    path('pathology/', views.Pathology_Index, name='path'),
    path('ipd_dash',views.ipd_dash,name="ipd_dashboard"),
    path('ipd/<int:ipd_id>/', views.ipd_dashboard, name='ipd_dashboard'),
    path('ipd_pat',views.ipd_pat,name="ipd_pat"),

    path('medicine-categories/', views.process_medicine_category, name='medicine_category_list'),
    path('pre/', views.pre, name='pre'),
    
    
]   