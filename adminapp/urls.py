

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
    path('show/', views.show, name='show'),
    path('issue_blood/', views.add_blood_donation, name='issue_blood'),
    path('issue_comp/', views.issue_comp, name='issue_comp'),
    path('add_charge/', views.add_charge, name='add_charge'),
    path('charge_name/', views.charge_name, name='charge_name'),
    path('tax_cat/', views.tax_category, name='tax_cat'),
    path('path_test/', views.path_test, name='path_test'),
    path('pathology/', views.Pathology_Index, name='path'),
    path('ipd_dash',views.ipd_dash,name="ipd_dashboard"),
    path('ipd/<int:ipd_id>/', views.ipd_dashboard, name='ipd_dashboard'),
    path('opd/<int:ipd_id>/', views.opd_dashboard, name='opd_dashboard'),
    path('ipd_pat',views.ipd_pat,name="ipd_pat"),

    path('medicine-categories/', views.process_medicine_category, name='medicine_category_list'),
    path('pre/', views.pre, name='pre'),
    path('add_income',views.create_income,name="add_income"),
    path('add_expense',views.create_expense,name="add_expense"),
    path('income_head',views.income_head,name="income_head"),
    path('expense_head',views.expense_head,name="expense_head"),
    path('add_tpa',views.add_tpa,name="add_tpa"),
    path('add_child',views.create_child,name="add_child"),
    path('add_death',views.create_death_record,name='add_death'),
    path('fetch_case_details/', views.fetch_case_details, name='fetch_case_details'),
    
    path('add_referral_cate',views.add_referral_cate,name="add_referral_cate"),
    path('referral_person',views.create_referralperson,name="referral_person"),
    path('referral',views.create_referre,name="referral"),
    path('add_ambulance',views.create_vehicle,name="add_ambulance"),
    path('ambulance_call',views.ambulance_call,name="ambulance_call"),
    path('get_driver_name',views.get_driver_name,name="get_driver_name"),
    path('add_itemcat',views.add_itemcat,name="add_itemcat"),
    path('add_store',views.add_store,name="add_store"),
    path('add_supplierdet',views.add_supplierdet,name="add_supplierdet"),
    path('add_item/', views.add_item, name='add_item'),
    path('add_itemstock/', views.add_itemstock, name='add_itemstock'),
    path('fetch_items_by_category/',views.fetch_items_by_category, name='fetch_items_by_category'),
    path('path_category', views.path_category, name='path_category'),
    path('path_parameter', views.path_parameter, name='path_parameter'),
    path('path_test/get-parameter-details', views.get_parameter_details, name='get_parameter_details'),
    path('radiology', views.radiology, name='radiology'),
    path('radio_category', views.rado_category, name='radio_category'),
    path('radio_parameter', views.radio_parameter, name='radio_parameter'),
    path('radio_test', views.radio_test, name='radio_test'),
    path('pathology/get_tax_info', views.get_tax_info, name='get_tax_info'),
    path('get_tax', views.get_tax, name='get_tax'),
    path('opd',views.opd,name='opd'),
    path('purchase_med',views.purchase_med,name='purchase_med'),
    path('nurse/<int:id>/',views.add_nursing_record,name='nurse'),
    path('doctor/<int:id>/',views.add_doctor_record,name='doctor'),
    path('blood_donation',views.blood_donation_form,name='blood_donation'),
    path('charge_type',views.create_charge_type,name='charge_type'),
    path('get_related_categories/', views.get_related_categories, name='get_related_categories'),
    path('get_tax_percentage', views.get_tax_percentage, name='get_tax_percentage'),
    path('profile/<int:id>',views.profile,name='profile'),
    path('login/', views.login, name='login'),
    path('doctor', views.doctor, name='doctor'),
    path('referral_commission/', views.commission_form, name='referral_commission'),
    path('add_task/', views.add_task, name='add_task'),
    path('get_selected_role_data/', views.get_selected_role_data, name='get_selected_role_data'),
    path('payroll/', views.payroll, name='payroll'),
    path('payroll/<int:id>', views.payroll_id, name='payroll_id'),
    path('meeting/', views.create_meeting, name='meeting'),
    path('party',views.party_create,name="party"),
    path('add_category/', views.add_category, name='add_category'),
    path('item_acc/', views.manage_items, name='item_acc'),
    path('unit/', views.unit, name='unit'),
    path('sales_invoice', views.sales_invoice, name='sales_invoice'),
    path('purchase_invoice', views.purchase_invoice, name='purchase_invoice'),
    path('Sales_Party', views.Party_User, name='Sales_Party'),
    path('item_details', views.Item_Details, name='item_details'),
    path('medicine_details', views.Medicine_Details, name='medicine_details'),
    path('path_details', views.path_details, name='path_details'),
    path('medicine-det', views.Med_det, name='medicine_det'),
    path('pos_details', views.POS_Details, name='pos_details'),
    path('generate_invoice_pdf/<int:id>/', views.generate_invoice_pdf, name='generate_invoice_pdf'),
    path('generate_purchase_pdf/<int:id>/', views.generate_purchase_pdf, name='generate_purchase_pdf'),
    path('edit_sales/<int:id>/', views.edit_sales, name='edit_sales'),
    path('dosage/<int:id>/', views.add_medication_dose, name='dosage'),
    path('edit_purchase/<int:id>/', views.edit_purchase, name='edit_purchase'),
    path('sale', views.invoice, name='sale'),
    path('purchase', views.purchase, name='purchase'),
    path('balance_sheet/', views.balance_sheet, name='balance_sheet'),
    path('create_asset/', views.create_asset, name='create_asset'),
    path('create_liablity/', views.create_liablity, name='create_liablity'),
    path('purchase_report/', views.purchase_report, name='purchase_report'),
    path('sales_report/', views.sales_report, name='sales_report'),
    path('search_appointment/', views.search_appointments, name='search_appointments'),
    path('search_opd/', views.search_OPD, name='search_opd'),
    path('search_opdblance/', views.search_OPDBalance, name='search_opdbalance'),
    path('search_ipdblance/', views.search_IPDBalance, name='search_ipdbalance'),
    path('search_ipd/', views.search_IPD, name='search_ipd'),
    path('search_tpa/', views.search_tpa, name='search_tpa'),
    path('search_medicine/', views.search_medicine, name='search_medicine'),
    path('search_patient/', views.search_patient, name='search_patient'),
    path('report_appointment/', views.report_appointment, name='report_appointment'),
    path('consultant_register/<int:id>/', views.consultant_register, name='consultant_register'),
    path('ipd_operation/<int:id>/', views.operation_create, name='ipd_operation'),
    path('ipd_payment/<int:id>/', views.ipd_payment, name='ipd_payment'),
    path('ipd_prep/<int:id>/', views.prescription, name='ipd_prep'),
    path('transcations/', views.all_transcation, name='transcation'),
    path('all_party/',views.all_party,name="all_party"),
    path('expense_category/',views.create_expense_category,name="expense_category"),
    path('expense_item/',views.expense_item,name="expense_item"),
    path('expense_invoice/',views.expense_invoice,name="expense_invoice"),
    path('expense_details/',views.Expense_details,name="expense_details"),
    path('sales_order/',views.sales_order,name="sales_order"),
    path('cash_flow/',views.cash_flow,name="cash_flow"),
    path('deposit/<int:id>',views.deposit,name="deposit"),
    path('payment_in/',views.payment_in,name="payment_in"),
    path('sales_estimate/',views.sales_estimate,name="sales_estimate"),
    path('download/',views.download,name="download"),
    path('download_ipd/<int:id>',views.IPD_pdf,name="download_ipd"),
    path('download_opd/<int:id>',views.IPD_pdf,name="download_opd"),
    path('bank_accountlist/<int:id>', views.bank_account_list, name='bank_accountlist'),
    path('bank_account/',views.bank_account,name="bank_account"),
    path('delivery_challan/',views.delivery_challan,name="delivery_challan"),
    path('credit_note',views.credit_note,name="credit_note"),
    path('profit_loss',views.profit_and_loss_statement,name="profit"),
    path('edit_creditnote/<int:id>',views.edit_credit_note,name="edit_credit_note"),
    path('edit_challan/<int:id>',views.edit_delivery_challan,name="edit_challan"),
    path('edit_salesorder/<int:id>',views.edit_sales_order,name="edit_sales_order"),
    path('edit_salesestimate/<int:id>',views.edit_sales_estimate,name="edit_sales_estimate"),
    path('get_bed_details/', views.get_bed_details, name='get_bed_details'),
    path('expense_list/', views.expense_list, name='expense_list'),
    path('send_test', views.send_test, name='send_test'),
    path('saleorder_list/', views.sales_orderlist, name='sale_order_list'),
    path('sales_invoicelist/', views.sales_invoice_list, name='sale_invoice_list'),
    path('estimate_list/', views.estimate_list, name='estimate_list'),
    path('delivery_list/', views.challan_list, name='challan_list'),
    path('sales_returnlist/', views.return_list, name='sales_returnlist'),
    path('payment_inlist/', views.payment_list, name='payment_list'),
    path('edit_party/<int:party_id>',views.edit_party,name="edit_party"),
    path('smtp',views.add_smtp_server,name="smtp"),
    path('search_patient/', views.search_patient, name='search_patient'),
    path('edit_staff/<int:id>/', views.edit_staff, name='edit_staff'),
    path('logout/', views.user_logout, name='logout'),
    path('add_hospital/', views.add_hospital, name='add_hospital'),
    path('add_ads/', views.add_ads, name='add_ads'),
    path('add_ads/<int:id>', views.edit_ads, name='edit_ads'),
    path('get_header_data/', views.get_header_data, name='get_header_data'),
    path('gst/', views.gstreport, name='gst'),
    path('get_ads_data/', views.get_ads_data, name='get_ads_data'),
    path('get_bed_data/', views.get_bed_data, name='get_bed_data'),
    path('admin_notice/', views.admin_notice_board, name='admin_notice'),
    path('public_notice/', views.public_notice_board, name='public_notice'),
    path('send_message/<int:receiver_id>/', views.send_message, name='send_message'),
    path('calculator/', views.calculator_view, name='calculator'),
    path('chat_list/', views.chat_list, name='chat_list'),
    path('send_emails/', views.send_email, name='send_email'),
    path('chat/<str:room_name>', views.chat_room, name='room'),
    path('chat/<int:receiver_id>/<int:sender_id>',views.send_message,name="send"),
    path('delete_staff/<int:user_id>',views.deletestaff,name="staff_delete"),
    path('pos',views.pos,name="pos"),
    path('add_to_cart/', views.add_to_cart, name='add_to_cart'),
    path('remove_from_cart/', views.remove_from_cart, name='remove_from_cart'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add-funds/', views.add_funds, name='add_funds'),
    path('make-payment/', views.make_payment, name='make_payment'),
    path('items/', views.item_list, name='item_list'),
    path('add_to_cart/<int:item_id>/', views.add_to_cart, name='add_to_cart'),
    path('view_cart/', views.view_cart, name='view_cart'),
    path('pos_pdf/', views.pos_pdf, name='pos_pdf'),
    path('pos_pathpdf/', views.pos_pathpdf, name='pos_pathpdf'),
    path('stock_report/', views.stock_report, name='stock_report'),
    path('death/', views.death_report, name='death_report'),
    path('birth/', views.birth_report, name='birth_report'),
    path('discharge/', views.discharge, name='discharged_patient'),
    path('ipd_discharge/', views.ipd_discharge, name='ipd_discharge'),
    path('opd_discharge/', views.opd_discharge, name='opd_discharge'),
    path('refferal_report/', views.refferal_report, name='refferal_report'),
    path('ambulance_report/', views.ambulance_report, name='ambulance_report'),    
    path('blood_donor_report/', views.blood_donor_report, name='blood_donor_report'),    
    path('blood_issue_report/', views.blood_issue_report, name='blood_issue_report'),    
    path('prescreption/<int:id>', views.prescription, name='prescription'),    
    path('payroll_report', views.payroll_report, name='payroll_report'),    
    path('pos_path', views.pos_path, name='pos_path'),    
    path('pos_pathalogy', views.pos_pathalogy, name='pos_pathalogy'),    
    path('pos_radiology', views.pos_radiology, name='pos_radiology'),    
    path('pos_radio', views.pos_radio, name='pos_radio'),    
    path('pos_pharma', views.pos_pharma, name='pos_pharma'),    
    path('visitors', views.visitors, name='visitors'),    
    path('visitors_details', views.visitors_details, name='visitors_details'),    
    path('postal_receive', views.postal_receive, name='postal_receive'),    
    path('postal_dispatch', views.postal_dispatch, name='postal_dispatch'),    
    path('complain_type', views.complain_type, name='complain_type'),    
    path('complain_source', views.complain_source, name='complain_source'),    
    path('complain', views.complain, name='complain'),    
    path('operation_name', views.operation_name, name='operation_name'),    
    path('operation_cate', views.operation_cate, name='operation_cate'),    
    path('ot_report', views.ot_report, name='ot_report'),    
    path('search_case', views.search_case_id, name='search_case'),
    path('stock', views.stock, name='stock'),
    path('party/<int:id>', views.party_report, name='party_report'),
    path('approval', views.approval, name='approval'),
    path('cashbook', views.cashbook, name='cashbook'),
    path('bankbook/<int:id>', views.bankbook, name='bankbook'),
    path('bankbook', views.bankbooks, name='bankbooks'),
    path('bank_pdf/<int:id>', views.bank_pdf, name='bank_pdf'),
    path('pos_bank', views.pos_bank, name='pos_bank'),
    path('pos_blood', views.pos_blood, name='pos_blood'),
    path('leaves', views.leaves, name='leaves'),
    path('birth_certificate', views.birth_certificate, name='birth_certificate'),
    path('bank', views.bank, name='bank'),
    path('bankpdf', views.pos_bankpdf, name='bankpdf'),
    path('cash_pdf', views.cash_pdf, name='cash_pdf'),
    path('pdf_blood', views.pdf_blood, name='pdf_blood'),
    path('birth_pdf/<int:id>', views.birth_pdf, name='birth_pdf'),
    path('bankorigin', views.bankorigin, name='bankorigin'),
    path('brs', views.brs, name='brs'),
    path('blood_setup', views.blood_setup, name='blood_setup'),
    path('blood_component', views.blood_component, name='blood_component'),
    path('house_blood', views.house_blood, name='house_blood'),
    path('depreciation', views.depreciation, name='depreciation'),
    path('appointment_letter', views.appointment_letter, name='appointment_letter'),
    path('resign_letter', views.resign_letter, name='resign_letter'),
    path('leave_letter', views.leave_letter, name='leave_letter'),
    path('sampleappointment_letter', views.sampleappointment_letter, name='sampleappointment_letter'),
    path('sampleresign_letter', views.sampleresign_letter, name='sampleresign_letter'),
    path('notification', views.send_notification_push, name='send_notification'),
    path('certificate', views.certificate, name='certificate'),
    path('death_pdf/<int:id>', views.death_pdf, name='death_pdf'),
    path('send_mail', views.send, name='send_mail'),
    path('medicine_composition', views.medicine_composition, name='medicine_composition'),
    path('approval/<int:id>', views.approval_path, name='approval_path'),



]   