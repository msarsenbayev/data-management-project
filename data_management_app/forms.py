from django.forms import ModelForm
from django import forms
from .models import *
#import floppyforms 
# from django.core.validators import MinLengthValidator
# from django.core import validators

class DateInput(forms.DateInput):
    input_type = 'date'
    
class ValveDispatchForm(ModelForm): 
	class Meta:
		model = ValveDispatch
		fields = '__all__'
		widgets = {
            'dispatch_date': DateInput(),
        }

class ValveReceiptForm(ModelForm): 
	class Meta:
		model = ValveReceipt
		fields = '__all__'
		widgets = {
            'received_date': DateInput(),
        }

class ShellTestForm(ModelForm): 
	class Meta:
		model = ShellTest
		fields = '__all__'
		widgets = {
            'test_date': DateInput(),
        }

class BackSeatTestForm(ModelForm): 
	class Meta:
		model = BackSeatTest
		fields = '__all__'
		widgets = {
            'test_date': DateInput(),
        }

class SeatTestForm(ModelForm): 
	class Meta:
		model = SeatTest
		fields = '__all__'
		widgets = {
            'test_date': DateInput(),
        }

class ValveInspectionForm(ModelForm): 
	class Meta:
		model = ValveInspection
		fields = '__all__'
		widgets = {
            'inspected_date': DateInput(),
        }

class ValvePreservationForm(ModelForm): 
	class Meta:
		model = ValvePreservation
		fields = '__all__'
		widgets = {
            'preservation_date': DateInput(),
        }

# class ValveTestingFactTableForm(ModelForm): 
# 	class Meta:
# 		model = valvetestingfacttable
# 		fields = '__all__'
	


class ValveDetailsForm(ModelForm): 
	valve_serial_number = forms.CharField(max_length=15, min_length=7)
	
	class Meta:
		model = ValveDetails
		fields = (
				'valve_serial_number', 
	    		'valve_size_in', 
				'valve_size_dn', 
				'valve_size_dn', 
				'valve_rating', 
				'valve_manufacturer',
				'valve_item_code',
				'valve_type',
				'valve_seat_type',
				'valve_end_connection',
				'valve_operator',
				'valve_bore_type',
				'valve_seat_material',
				'valve_body_material',
				'valve_obturator_material',
				'valve_stem_material'
				)
		labels = {
			'valve_serial_number': "",
			'valve_size_in': "",
			'valve_size_dn': "",
			'valve_size_dn': "",
			'valve_rating': "",
			'valve_manufacturer': "",
			'valve_item_code': "",
			'valve_type': "",
			'valve_seat_type': "",
			'valve_end_connection': "",
			'valve_operator': "",
			'valve_bore_type': "",
			'valve_seat_material': "",
			'valve_body_material': "",
			'valve_obturator_material': "",
			'valve_stem_material': "",
		}
        
		widgets = {
			'valve_serial_number': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Valve Serial Number'}), 
			'valve_size_in': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Valve Size In'}), 
			'valve_size_dn': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Valve Size DN'}), 
			'valve_rating': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Valve Rating'}), 
			'valve_manufacturer': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Valve Manufacturer'}),
			'valve_item_code': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Valve Item Code'}),
			'valve_type': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Valve Type'}),
			'valve_seat_type': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Valve Seat Type'}),
			'valve_end_connection': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Valve End Connection'}),
			'valve_operator': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Valve Operator'}),
			'valve_bore_type': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Valve Bore FB/RB'}),
			'valve_seat_material': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Valve Seat Material'}),
			'valve_body_material': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Valve Body Material'}),
			'valve_obturator_material': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Valve Obturator Material'}),
			'valve_stem_material': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Valve Stem Material'}),
		}
