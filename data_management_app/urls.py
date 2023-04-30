from django.urls import path, include
from .views import *
from . import views
from django.contrib.auth import views as auth_views
from .models import *
# from rest_framework import routers

# router = routers.DefaultRouter()
# router.register(r'seattest', uniqueseattesttable)

urlpatterns = [
    # path('', include(router.urls)),

    path('login/', include("django.contrib.auth.urls")),
    
	path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

	path('submit_valve_details/', handle_form_valvedetails, name='submit_valve_details'),
    path('submit_valve_inspection/', handle_form_valveinspection, name='submit_valve_inspection'),
    path('submit_valve_preservation/', handle_form_valvepreservation, name='submit_valve_preservation'),
    path('handle_login/', handle_login, name='handle_login'),
    path('handle_logout/', handle_logout, name='handle_logout'),
    path('submit_seattest/', handle_form_seattest, name='submit_seattest'),
    path('submit_backseattest/', handle_form_backseattest, name='submit_backseattest'),
    path('submit_shelltest/', handle_form_shelltest, name='submit_shelltest'),
    path('submit_valvereceipt/', handle_form_valvereceipt, name='submit_valvereceipt'),
    path('submit_valvedispatch/', handle_form_valvedispatch, name='submit_valvedispatch'),
    #path('submit_valvetestingfacttable/', handle_form_valvetestingfacttable, name='submit_valvetestingfacttable'),

    path('update_valvedetails.html/<valvedetails_id>', views.update_valve_info, name='update_valve_info'),
    path('total_valve_info.html/<valvedetails_id>', views.view_valve_info, name='view_valve_info'),
    #path('total_valve_info.html/<valvedetails_id>', views.view_seattests, name='view_seattests'),
    
    path('dashboard.html/', views.charts, name="dashboard"),
    path('submitted_seattesting.html/', views.seattesttable.as_view(), name="seattests"),
    path('submitted_shelltesting.html/', views.shelltesttable.as_view(), name="shelltests"),
    path('submitted_backseattesting.html/', views.backseattesttable.as_view(), name="backseattests"),
    path('submitted_valvereceipt.html/', views.valvereceipttable.as_view(), name="valvereceipttable"),
    path('submitted_valvedispatch.html/', views.valvedispatchtable.as_view(), name="valvedispatchtable"),
	path('', views.login_page, name='login_page'),
	path('main_page.html', views.main_page, name="main_page"),
	path('valve_database.html', views.valve_database, name="valve_database"),
	path('valve_repair_mods.html', views.valve_repair_mods, name="valve_repair_mods"),
	path('valve_testing.html', views.valve_testing, name="valve_testing"),
    path('valve_inspection.html', views.valve_inspection, name="valve_inspection"),
    path('valve_preservation.html', views.valve_preservation, name="valve_preservation"),
    path('seattest_form.html', views.seattest_page, name="seattest_page"),
    path('backseattest_form.html', views.backseattest_page, name="backseattest_page"),
    path('shelltest_form.html', views.shelltest_page, name="shelltest_page"),
    path('valvereceipt_form.html', views.valvereceipt_page, name="valvereceipt_page"),
    path('valvedispatch_form.html', views.valvedispatch_page, name="valvedispatch_page"),
    #path('serialnumber_form.html', views.serialnumber_page, name="serialnumber_page"),
    #path('valvetestingfacttable_form.html', views.valvetestingfacttable_page, name="valvetestingfacttable_page"),

    #path('submitted_valvedetails.html/', views.valve_details, name="submitted_valvedetails"),
    #path('new_dashboard.html/', views.SeatTestTableView, name="SeatTestTableView"),
    path('all_valve_info.html/', views.FilteredValveDetailsView.as_view(), name="valvedetails_filter"),
    path('submitted_seattesting.html', views.FilteredSeatTestView.as_view(), name="submitted_valvetesting"),
    path('submitted_valveinspection.html', views.submitted_valveinspection.as_view(), name="submitted_valveinspection"),
    path('submitted_valvepreservation.html', views.submitted_valvepreservation.as_view(), name="submitted_valvepreservation"),
    path('submitted_valvetesting.html', views.myfacttable, name="myfacttable"),
    
    path('distinct_seattests.html', views.uniqueseattesttable.as_view(), name="uniqueseattesttable"),
]
