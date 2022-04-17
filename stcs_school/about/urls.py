from django.urls import path
from . import views

urlpatterns = [

    path('mandatory-public-disclosures',views.public_disclosure,name='public_disclosure'),
    path('documents-information',views.documents_info,name='documents_info'),
    path('results-and-academic',views.resultsAcademic,name='results_&_academic'),

    path('copies_of_recent_extension_of_affiliation',views.affiliation_letter,name='copies_of_recent_extension_of_affiliation'),
    path('copies_of_society_registration',views.society_registration,name='copies_of_society_registration'),
    path('copy_of_no_objection_certificate_noc_issued',views.noc_certificate,name='copy_of_no_objection_certificate_noc_issued'),
    path('copies_of_recognition_certificate_under_rte_act_2009_and_renewal',views.recognition_certificate,name='copies_of_recognition_certificate_under_rte_act_2009_and_renewal'),
    path('copy_of_valid_building_safety_certificate',views.building_safety_certificate,name='copy_of_valid_building_safety_certificate'),
    path('copy_of_valid_fire_safety_certificate',views.fire_safety_certificate,name='copy_of_valid_fire_safety_certificate'),
    path('copy_of_the_deo_certificate',views.deo_certificate,name='copy_of_the_deo_certificate'),
    path('copy_of_valid_water_health_and_sanitation_certificate',views.sanitation_certificate,name='copy_of_valid_water_health_and_sanitation_certificate'),
    path('fee_structure',views.fee_structure,name='fee_structure'),
    path('academic_calendar',views.academic_calendar,name='academic_calendar'),
    path('management_committee',views.management_committee,name='management_committee'),
    path('parents_teacher_association',views.parents_teacher_association,name='parents_teacher_association'),
    path('three_year_board_results',views.three_year_board_results,name='three_year_board_results'),
    path('appendix_IX',views.appendix_IX,name='appendix_IX'),

]