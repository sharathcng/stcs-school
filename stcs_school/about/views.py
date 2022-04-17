from django.shortcuts import render
from django.http import FileResponse


#public disclosure
def public_disclosure(request):
    return render(request,'user-view/about/public_disclosure.html',{})

#general_info
def general_info(request):
    return render(request,'user-view/about/generalInfo.html',{})

#documents_info
def documents_info(request):
    return render(request,'user-view/about/document_info.html',{})

#results_academic
def resultsAcademic(request):
    return render(request,'user-view/about/results_&_academic.html',{})

# affiliation_letter
def affiliation_letter(request):
    return FileResponse(open('templates/user-view/about/documents and information/copies_of_recent_extension_of_affiliation.pdf', 'rb'), content_type='application/pdf')

#society_registration
def society_registration(request):
    return FileResponse(open('templates/user-view/about/documents and information/copies_of_society_registration.pdf', 'rb'), content_type='application/pdf')

# copy_of_no_objection_certificate_noc_issued
def noc_certificate(request):
    return FileResponse(open('templates/user-view/about/documents and information/copy_of_no_objection_certificate_noc_issued.pdf', 'rb'), content_type='application/pdf')

# copy_of_no_objection_certificate_noc_issued
def recognition_certificate(request):
    return FileResponse(open('templates/user-view/about/documents and information/copies_of_recognition_certificate_under_rte_act_2009_and_renewal.pdf', 'rb'), content_type='application/pdf')

# building_safety_certificate
def building_safety_certificate(request):
    return FileResponse(open('templates/user-view/about/documents and information/copy_of_valid_building_safety_certificate.pdf', 'rb'), content_type='application/pdf')

# fire_safety_certificate
def fire_safety_certificate(request):
    return FileResponse(open('templates/user-view/about/documents and information/copy_of_valid_fire_safety_certificate.pdf', 'rb'), content_type='application/pdf')

# copy_of_no_objection_certificate_noc_issued
def deo_certificate(request):
    return FileResponse(open('templates/user-view/about/documents and information/copy_of_the_deo_certificate.pdf', 'rb'), content_type='application/pdf')


# copy_of_no_objection_certificate_noc_issued
def sanitation_certificate(request):
    return FileResponse(open('templates/user-view/about/documents and information/copy_of_valid_water_health_and_sanitation_certificate.pdf', 'rb'), content_type='application/pdf')


# copy_of_no_objection_certificate_noc_issued
def fee_structure(request):
    return FileResponse(open('templates/user-view/about/results and academic/fee_structure.pdf', 'rb'), content_type='application/pdf')


# copy_of_no_objection_certificate_noc_issued
def academic_calendar(request):
    return FileResponse(open('templates/user-view/about/results and academic/academic_calendar.pdf', 'rb'), content_type='application/pdf')


# copy_of_no_objection_certificate_noc_issued
def management_committee(request):
    return FileResponse(open('templates/user-view/about/results and academic/management_committee.pdf', 'rb'), content_type='application/pdf')

# parents_teacher_association
def parents_teacher_association(request):
    return FileResponse(open('templates/user-view/about/results and academic/parents_teacher_association.pdf', 'rb'), content_type='application/pdf')


# three_year_board_results
def three_year_board_results(request):
    return FileResponse(open('templates/user-view/about/results and academic/three_year_board_results.pdf', 'rb'), content_type='application/pdf')

# appendix_IX
def appendix_IX(request):
    return FileResponse(open('templates/user-view/about/appendix_IX.pdf', 'rb'), content_type='application/pdf')


