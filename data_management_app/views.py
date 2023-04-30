from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from django.contrib.auth import logout, authenticate, login
from .models import *
from .forms import *
from django.contrib import messages
from django.http import HttpResponse
from django.db import connection
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from django.utils.decorators import method_decorator
import pandas as pd
from django.http import JsonResponse
import json
from django.db.models import Count
from collections import Counter
import django_tables2 as tables
from django.views.generic import ListView
from django_tables2.views import SingleTableView
from .tables import *
from .filters import *
from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin
from rest_framework import viewsets, filters, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .serializers import *
from django.db.models import Q

#from django.views.decorators.cache import cache_control

# Import Pagination Stuff
from django.core.paginator import Paginator


def login_page(request):
	return render(request, 'login.html')

#@cache_control(no_cache=True, must_revalidate=True)
@login_required(login_url='login_page')
def main_page(request):
	return render(request, 'main_page.html')


@login_required(login_url='login_page')
def charts(request):
		# cursor=connection.cursor()
		# cursor.execute('select data_management_app_valvedetails.valve_serial_number, data_management_app_valvedetails.valve_size_in, data_management_app_valvedetails.valve_rating, data_management_app_valvedetails.valve_manufacturer, data_management_app_seattest.test_result from data_management_app_valvedetails join data_management_app_seattest on data_management_app_valvedetails.valve_serial_number=data_management_app_seattest.serial_number')
		# results=cursor.fetchall()
		#seattests = SeatTest.objects.all()

	################Valve Type Chart######################
		type_input_data = ValveDetails.objects.values('valve_type')
		#dataset = ValveDetails.objects.values('valve_type')

		# First, create an empty dictionary to store the unique labels and their counts
		label_counts = {}

		# Loop through the input data and count the occurrences of each label
		for item in type_input_data:
			if item['valve_type'] in label_counts:
				label_counts[item['valve_type']] += 1
			else:
				label_counts[item['valve_type']] = 1

		# Now create the label and data arrays for the chart
		type_labels = list(label_counts.keys())
		type_dataset = list(label_counts.values())
	################end######################

	################Valve Manufacturer Chart######################
		manufacturer_input_data = ValveDetails.objects.values('valve_manufacturer')

		# First, create an empty dictionary to store the unique labels and their counts
		man_label_counts = {}

		# Loop through the input data and count the occurrences of each label
		for man_item in manufacturer_input_data:
			if man_item['valve_manufacturer'] in man_label_counts:
				man_label_counts[man_item['valve_manufacturer']] += 1
			else:
				man_label_counts[man_item['valve_manufacturer']] = 1

		# Now create the label and data arrays for the chart
		man_labels = list(man_label_counts.keys())
		man_dataset = list(man_label_counts.values())
	################end######################

	################Valve Test Result Chart######################
		# Get the input data for the chart
		omb_seat_types = ValveDetails.objects.filter(valve_manufacturer='OMB').values('valve_seat_type')
		
		# First, create empty lists to store the "Fail" and "Pass" results
		omb_metal_list = []
		omb_soft_list = []

		# Loop through the input data and append the "Fail" and "Pass" results to their respective lists
		for item in omb_seat_types:
			if item['valve_seat_type'] == 'METAL':
				omb_metal_list.append(item['valve_seat_type'])
			elif item['valve_seat_type'] == 'SOFT':
				omb_soft_list.append(item['valve_seat_type'])

		# Now create the fail_dataset and pass_dataset for the chart
		omb_metal_dataset = [len(omb_metal_list)]
		omb_soft_dataset = [len(omb_soft_list)]



		#PERAR
		perar_seat_types = ValveDetails.objects.filter(valve_manufacturer='PERAR').values('valve_seat_type')
		
		# First, create empty lists to store the "Fail" and "Pass" results
		perar_metal_list = []
		perar_soft_list = []

		# Loop through the input data and append the "Fail" and "Pass" results to their respective lists
		for item in perar_seat_types:
			if item['valve_seat_type'] == 'METAL':
				perar_metal_list.append(item['valve_seat_type'])
			elif item['valve_seat_type'] == 'SOFT':
				perar_soft_list.append(item['valve_seat_type'])

		# Now create the fail_dataset and pass_dataset for the chart
		perar_metal_dataset = [len(perar_metal_list)]
		perar_soft_dataset = [len(perar_soft_list)]

		#GOODWIN
		goodwin_seat_types = ValveDetails.objects.filter(valve_manufacturer='GOODWIN').values('valve_seat_type')
		
		# First, create empty lists to store the "Fail" and "Pass" results
		goodwin_metal_list = []
		goodwin_soft_list = []

		# Loop through the input data and append the "Fail" and "Pass" results to their respective lists
		for item in goodwin_seat_types:
			if item['valve_seat_type'] == 'METAL':
				goodwin_metal_list.append(item['valve_seat_type'])
			elif item['valve_seat_type'] == 'SOFT':
				goodwin_soft_list.append(item['valve_seat_type'])

		# Now create the fail_dataset and pass_dataset for the chart
		goodwin_metal_dataset = [len(goodwin_metal_list)]
		goodwin_soft_dataset = [len(goodwin_soft_list)]

		#GALPERTI
		galperti_metal_dataset = ValveDetails.objects.filter(valve_manufacturer='GALPERTI', valve_seat_type='METAL').count()
		galperti_soft_dataset = ValveDetails.objects.filter(valve_manufacturer='GALPERTI', valve_seat_type='SOFT').count()
	

		
	#################SIZE COUNT Chart######################
		size_input_data = ValveDetails.objects.values('valve_size_in')

		# First, create an empty dictionary to store the unique labels and their counts
		size_label_counts = {}

		# Loop through the input data and count the occurrences of each label
		for man_item in size_input_data:
			if man_item['valve_size_in'] in size_label_counts:
				size_label_counts[man_item['valve_size_in']] += 1
			else:
				size_label_counts[man_item['valve_size_in']] = 1

		# Now create the label and data arrays for the chart
		size_labels = list(size_label_counts.keys())
		size_dataset = list(size_label_counts.values())
	################end######################

		#TOTAL VALVES
		total_valves = total_valves = ValveDetails.objects.filter(valve_serial_number__isnull=False).count()
		total_soft = ValveDetails.objects.filter(valve_seat_type='SOFT').count()
		total_metal = ValveDetails.objects.filter(valve_seat_type='METAL').count()

		#SEAT TESTS
		unique_seattests = SeatTest.objects.all().distinct('serial_number').order_by('serial_number','-seattest_id')
		seat_tests = unique_seattests.filter(serial_number__isnull=False).count()
		seattest_pass = unique_seattests.filter(test_result='PASS').count()
		seattest_fail = seat_tests - seattest_pass

		#SHELL TESTS
		unique_shelltests = ShellTest.objects.all().distinct('serial_number').order_by('serial_number','-shelltest_id')
		shell_tests = unique_shelltests.filter(serial_number__isnull=False).count()
		shelltest_pass = unique_shelltests.filter(test_result='PASS').count()
		shelltest_fail = shell_tests - shelltest_pass

		#BACKSEAT TESTS
		unique_backseattests = BackSeatTest.objects.all().distinct('serial_number').order_by('serial_number','-backseattest_id')
		backseat_tests = unique_backseattests.filter(serial_number__isnull=False).count()
		backseat_pass = unique_backseattests.filter(test_result='PASS').count()
		backseat_fail = backseat_tests - backseat_pass
	

		context = {
			#'seattests':seattests,
			'type_labels': type_labels,
			'type_dataset': type_dataset,
			'man_labels': man_labels,
			'man_dataset': man_dataset,
			'omb_metal_dataset': omb_metal_dataset,
			'omb_soft_dataset': omb_soft_dataset,
			'perar_metal_dataset': perar_metal_dataset,
			'perar_soft_dataset': perar_soft_dataset,
			'goodwin_metal_dataset': goodwin_metal_dataset,
			'goodwin_soft_dataset': goodwin_soft_dataset,
			'galperti_metal_dataset': galperti_metal_dataset,
			'galperti_soft_dataset': galperti_soft_dataset,
			'size_labels': size_labels,
			'size_dataset': size_dataset,
			'total_valves': total_valves,
			'total_soft': total_soft,
			'total_metal': total_metal,
			'seat_tests': seat_tests,
			'seattest_pass': seattest_pass,
			'seattest_fail':seattest_fail,
			'shell_tests': shell_tests,
			'shelltest_pass':shelltest_pass,
			'shelltest_fail':shelltest_fail,
			'backseat_tests':backseat_tests,
			'backseat_pass':backseat_pass,
			'backseat_fail':backseat_fail,


		}

		return render(request, 'dashboard.html', context)


@method_decorator(login_required(login_url='login_page'), name='dispatch')
class valve_details(SingleTableView):
		model = ValveDetails
		table_class = ValveDetailsTable
		#template_name = 'submitted_valvedetails.html'
		paginate_by = 50
		ordering = ['-valvedetails_id']


@method_decorator(login_required(login_url='login_page'), name='dispatch')
class FilteredValveDetailsView(SingleTableMixin, FilterView):
	model = ValveDetails
	table_class = ValveDetailsTable
	filterset_class = ValveDetailsFilter
	template_name = "all_valve_info.html"


@method_decorator(login_required(login_url='login_page'), name='dispatch')
class seattesttable(SingleTableView):
	model = SeatTest
	table_class = SeatTestTable
	paginate_by = 20
	#template_name = "submitted_seattesting.html"
	


@method_decorator(login_required(login_url='login_page'), name='dispatch')
class FilteredSeatTestView(SingleTableMixin, FilterView):
	model = SeatTest
	table_class = SeatTestTable
	filterset_class = SeatTestFilter
	template_name = "submitted_seattesting.html"
	ordering = ['-seattest_id']


@method_decorator(login_required(login_url='login_page'), name='dispatch')
class uniqueseattesttable(SingleTableView):
    model = SeatTest
    template_name = "distinct_seattests.html"
    def get_queryset(self):
        distinct_seattests = SeatTest.objects.all().distinct('serial_number').order_by('serial_number','-seattest_id')#SeatTest.objects.distinct('serial_number')
        return distinct_seattests


@method_decorator(login_required(login_url='login_page'), name='dispatch')
class shelltesttable(SingleTableView):
	model = ShellTest
	table_class = ShellTestTable
	paginate_by = 20
	template_name = "submitted_shelltesting.html"


@method_decorator(login_required(login_url='login_page'), name='dispatch')
class backseattesttable(SingleTableView):
	model = BackSeatTest
	table_class = BackSeatTestTable
	paginate_by = 20
	template_name = "submitted_backseattesting.html"


@method_decorator(login_required(login_url='login_page'), name='dispatch')
class valvereceipttable(SingleTableView):
	model = ValveReceipt
	table_class = ValveReceiptTable
	paginate_by = 20
	template_name = "submitted_valvereceipt.html"


@method_decorator(login_required(login_url='login_page'), name='dispatch')
class valvedispatchtable(SingleTableView):
	model = ValveDispatch
	table_class = ValveDispatchTable
	paginate_by = 20
	template_name = "submitted_valvedispatch.html"

############
@login_required(login_url='login_page')
def submitted_valvetesting(request):
	formvalvedetails = ValveDetails.objects.all()
	formseattest = SeatTest.objects.all()
	formbackseat = BackSeatTest.objects.all()
	formshell = ShellTest.objects.all()
	return render(request, 'submitted_valvetesting.html', 
	       {"formvalvedetails": formvalvedetails,
	 		"formseattest": formseattest,
			"formbackseat": formbackseat,
			"formshell": formshell})
############


@login_required(login_url='login_page')
def valve_database(request):
	form = ValveDetailsForm
	return render(request, 'valve_database.html', {"form": form})


@login_required(login_url='login_page')
def seattest_page(request):
	form = SeatTestForm
	return render(request, 'seattest_form.html', {"form": form})

@login_required(login_url='login_page')
def backseattest_page(request):
	form = BackSeatTestForm
	return render(request, 'backseattest_form.html', {"form": form})

@login_required(login_url='login_page')
def shelltest_page(request):
	form = ShellTestForm
	return render(request, 'shelltest_form.html', {"form": form})

@login_required(login_url='login_page')
def valvereceipt_page(request):
	form = ValveReceiptForm
	return render(request, 'valvereceipt_form.html', {"form": form})

@login_required(login_url='login_page')
def valvedispatch_page(request):
	form = ValveDispatchForm
	return render(request, 'valvedispatch_form.html', {"form": form})

# @login_required(login_url='login_page')
# def serialnumber_page(request):
# 	form = SerialNumberForm
# 	return render(request, 'serialnumber_form.html', {"form": form})

# @login_required(login_url='login_page')
# def valvetestingfacttable_page(request):
# 	form = ValveTestingFactTableForm
# 	return render(request, 'valvetestingfacttable_form.html', {"form": form})

@login_required(login_url='login_page')
def valve_repair_mods(request):
	return render(request, 'valve_repair_mods.html')

@login_required(login_url='login_page')
def valve_testing(request):
	return render(request, 'valve_testing.html')

@login_required(login_url='login_page')
def valve_inspection(request):
	return render(request, 'valve_inspection.html')

@login_required(login_url='login_page')
def valve_preservation(request):
	return render(request, 'valve_preservation.html')

@login_required(login_url='login_page')
def valve_preservation(request):
	return render(request, 'valve_preservation.html')


@login_required(login_url='login_page')
def submitted_valvedetails(request):
    return render(request, 'submitted_valvedetails.html')


# @login_required(login_url='login_page')
# def submitted_valvetesting(request):
#     valve_testing = SeatTest.objects.all()
#     return render(request, 'submitted_valvetesting.html', {'valve_testing': valve_testing})

# @login_required(login_url='login_page')
# def submitted_valveinspection(request):
#     valve_inspection = ValveInspection.objects.all()
#     return render(request, 'submitted_valveinspection.html', {'valve_inspection': valve_inspection})

# @login_required(login_url='login_page')
# def submitted_valvepreservation(request):
#     valve_preservation = ValvePreservation.objects.all()
#     return render(request, 'submitted_valvepreservation.html', {'valve_preservation': valve_preservation})

@method_decorator(login_required(login_url='login_page'), name='dispatch')
class submitted_valvepreservation(SingleTableView):
	model = ValveDispatch
	table_class = ValvePreservationTable
	paginate_by = 20
	template_name = "submitted_valvepreservation.html"

@method_decorator(login_required(login_url='login_page'), name='dispatch')
class submitted_valveinspection(SingleTableView):
	model = ValveInspection
	table_class = ValveInspectionTable
	paginate_by = 20
	template_name = "submitted_valveinspection.html"

def handle_form_valvedetails(request):
	if request.method == 'POST':
		form = ValveDetailsForm(request.POST)
		if form.is_valid():
			valve = form.save()
			valve.save()
			# Do something with the form data here	
			messages.success(request, "Successfully submitted")
			return redirect('valve_database')
		else:
			messages.warning(request, "Please enter correct data (One serial number cannot be submitted twice!)")
			return redirect('valve_database')
	else:
		return render(request, 'valve_database.html', {'valve': valve})


#seat test handler
def handle_form_seattest(request):
	if request.method == 'POST':
		form = SeatTestForm(request.POST)
		if form.is_valid():
			seattest = form.save()
			seattest.save()
			# Do something with the form data here	
			messages.success(request, "Successfully submitted")
			return redirect('valve_testing')
		else:
			messages.warning(request, "Please enter correct data")
			return redirect('valve_testing')
	else:
		return render(request, 'seattest_form.html', {'seattest': seattest})


#backseat test handler
def handle_form_backseattest(request):
	if request.method == 'POST':
		form = BackSeatTestForm(request.POST)
		if form.is_valid():
			backseattest = form.save()
			backseattest.save()
			# Do something with the form data here	
			messages.success(request, "Successfully submitted")
			return redirect('valve_testing')
		else:
			messages.warning(request, "Please enter correct data")
			return redirect('valve_testing')
	else:
		return render(request, 'backseattest_form.html', {'backseattest': backseattest})


#shell test handler
def handle_form_shelltest(request):
	if request.method == 'POST':
		form = ShellTestForm(request.POST)
		if form.is_valid():
			shelltest = form.save()
			shelltest.save()
			# Do something with the form data here	
			messages.success(request, "Successfully submitted")
			return redirect('valve_testing')
		else:
			messages.warning(request, "Please start new test with Seat Test or Please enter correct data")
			return redirect('valve_testing')
	else:
		return render(request, 'shelltest_form.html', {'shelltest': shelltest})


#valve receipt handler
def handle_form_valvereceipt(request):
	if request.method == 'POST':
		form = ValveReceiptForm(request.POST)
		if form.is_valid():
			valvereceipt = form.save()
			valvereceipt.save()
			# Do something with the form data here	
			messages.success(request, "Successfully submitted")
			return redirect('valvereceipt_page')
		else:
			messages.warning(request, "Please enter correct data")
			return redirect('valvereceipt_page')
	else:
		return render(request, 'valvereceipt_form.html', {'valvereceipt': valvereceipt})

#valve dispatch handler
def handle_form_valvedispatch(request):
	if request.method == 'POST':
		form = ValveDispatchForm(request.POST)
		if form.is_valid():
			valvedispatch = form.save()
			valvedispatch.save()
			# Do something with the form data here	
			messages.success(request, "Successfully submitted")
			return redirect('valvedispatch_page')
		else:
			messages.warning(request, "Please enter correct data")
			return redirect('valvedispatch_page')
	else:
		return render(request, 'valvedispatch_form.html', {'valvedispatch': valvedispatch})

#serial number form test handler
# def handle_form_valvetestingfacttable(request):
# 	if request.method == 'POST':
# 		form = ValveTestingFactTableForm(request.POST)
# 		if form.is_valid():
# 			vtfacttable = form.save()
# 			vtfacttable.save()
# 			# Do something with the form data here	
# 			messages.success(request, "Successfully submitted")
# 			return redirect('valve_testing')
# 		else:
# 			messages.warning(request, "Please enter correct data")
# 			return redirect('valve_testing')
# 	else:
# 		return render(request, 'valvetestingfacttable_form.html', {'vtfacttable': vtfacttable})

def handle_form_valveinspection(request):
	if request.method == 'POST':
		valveinspection = ValveInspection(
			valve_serial_number = request.POST.get('Valve Serial Number'),
			inspection_codes = request.POST.get('Inspection Codes'),
			inspected_date = request.POST.get('Inspected Date'),
			inspected_by = request.POST.get('Inspected By'),
			issues_identified = request.POST.get('Issues Identified'),
		)
		valveinspection.save()
		# Do something with the form data here
		return render(request, 'handle_form_submission.html', {'valveinspection': valveinspection})
	else:
		return render(request, 'handle_form_submission.html')
	

def handle_form_valvepreservation(request):
	#valvepreservation = None  # initialize to None
	if request.method == 'POST':
			valvepreservation = ValvePreservation(
			valve_serial_number = request.POST.get('Valve Serial Number'),
			preservation_codes = request.POST.get('Preservation Codes'),
			preservation_date = request.POST.get('Preservation Date'),
			preservation_by = request.POST.get('Preservation By'),
			comments = request.POST.get('Comments'),
			)
			if len(valvepreservation.valve_serial_number)!="" and valvepreservation.preservation_codes!="":
				valvepreservation.save()
				messages.success(request, "Successfully submitted")
				return redirect('valve_preservation')
			else:
				messages.warning(request, "Please enter correct data")
				return redirect('valve_preservation')
	else:
		return render(request, 'valve_preservation.html')
	


def handle_login(request):
	if request.method == 'POST':
			username = request.POST['Username']
			password = request.POST['Password']
			user = authenticate(request, username=username, password=password)
			if user is not None and user.is_superuser:
				login(request, user)
				return redirect('main_page')
			elif user is not None and user.is_staff:
				login(request, user)
				return redirect('dashboard')
			else:
				messages.warning(request, "Username or password is not correct")
				return redirect('login_page')
	else:
		return render(request, 'login.html')


def handle_logout(request):
		logout(request)
		messages.success(request, ("You Were Logged Out!"))
		return redirect('login_page')


def update_valve_info(request, valvedetails_id):
		valve_info = ValveDetails.objects.get(pk=valvedetails_id)
		form = ValveDetailsForm(request.POST or None, instance=valve_info)
		if 	form.is_valid():
			form.save()
			messages.success(request, "Successfully updated")
			return redirect("valvedetails_filter")
		return render(request, 'update_valvedetails.html', { "valve_info": valve_info, "form": form})


def view_valve_info(request, valvedetails_id):
		view_valvedetails = ValveDetails.objects.get(pk=valvedetails_id)
		seattests = view_valvedetails.seattest_set.all().order_by('-seattest_id')
		shelltests = view_valvedetails.shelltest_set.all().order_by('-shelltest_id')
		backseattests = view_valvedetails.backseattest_set.all().order_by('-backseattest_id')
		context = {
				"view_valvedetails": view_valvedetails,
				'seattests':seattests,
				'shelltests':shelltests,
				'backseattests':backseattests,
			}
		if seattests:
			return render(request, 'total_valve_info.html', context)
		else:
			messages.warning(request, ("This Valve Has Not Been Tested..."))
			return redirect('valvedetails_filter')
			


@login_required(login_url='login_page')
def myfacttable(request):
	# cursor=connection.cursor()
	# cursor.execute('select data_management_app_valvedetails.valve_serial_number, data_management_app_valvedetails.valve_size_in, data_management_app_valvedetails.valve_rating, data_management_app_valvedetails.valve_manufacturer, data_management_app_valvedetails.valve_item_code, data_management_app_valvedetails.valve_type, data_management_app_seattest.test_medium, data_management_app_seattest.test_date, data_management_app_seattest.test_result, data_management_app_shelltest.test_medium, data_management_app_shelltest.test_date, data_management_app_shelltest.test_result, data_management_app_backseattest.test_medium, data_management_app_backseattest.test_date, data_management_app_backseattest.test_result from data_management_app_valvedetails join data_management_app_seattest on data_management_app_valvedetails.valve_serial_number=data_management_app_seattest.serial_number join data_management_app_shelltest on data_management_app_valvedetails.valve_serial_number=data_management_app_shelltest.serial_number join data_management_app_backseattest on data_management_app_valvedetails.valve_serial_number=data_management_app_backseattest.serial_number')
	# facttableresults=cursor.fetchall()
	
	facttableresults = ValveDetails.objects.prefetch_related('seattest_set').values_list('seattest', 'shelltest')
	context = {
		'facttableresults':facttableresults}
	return render(request, 'submitted_valvetesting.html', context)
