import django_tables2 as tables
from .models import *
from django_tables2.utils import A

class ValveDetailsTable(tables.Table):
	# valvedetails_id = tables.Column(orderable=True)
	# valve_serial_number = tables.Column()
	# valve_size_in = tables.Column()
	# valve_size_dn = tables.Column()
	# valve_rating = tables.Column()
	# valve_manufacturer = tables.Column()
	# valve_item_code = tables.Column()
	# valve_type = tables.Column()
	# valve_seat_type = tables.Column()
	# valve_end_connection = tables.Column()
	# valve_operator = tables.Column()
	# valve_bore_type = tables.Column()
	# valve_seat_material = tables.Column()
	# valve_body_material = tables.Column()
	# valve_obturator_material = tables.Column()
	# valve_stem_material = tables.Column()
	view = tables.LinkColumn('view_valve_info', args=[A('pk')], orderable=False, empty_values=())
	def render_view(self):
		return 'View'
	update = tables.LinkColumn('update_valve_info', args=[A('pk')], orderable=False, empty_values=())
	def render_update(self):
		return 'Update'

	class Meta:
		model = ValveDetails
		#exclude = ('valve_serial_number', 'valve_size_in', 'valve_size_dn', 'valve_rating', 'valve_manufacturer', 'valve_item_code', 'valve_type', 'valve_seat_type', 'valve_end_connection', 'valve_operator', 'valve_bore_type', 'valve_seat_material', 'valve_body_material', 'valve_obturator_material', 'valve_stem_material',)
	


class SeatTestTable(tables.Table):

	class Meta:
		model = SeatTest


class ShellTestTable(tables.Table):

	class Meta:
		model = ShellTest


class BackSeatTestTable(tables.Table):

	class Meta:
		model = BackSeatTest


class ValveReceiptTable(tables.Table):

	class Meta:
		model = ValveReceipt


class ValveDispatchTable(tables.Table):

	class Meta:
		model = ValveDispatch


class ValveInspectionTable(tables.Table):

	class Meta:
		model = ValveInspection


class ValvePreservationTable(tables.Table):

	class Meta:
		model = ValvePreservation