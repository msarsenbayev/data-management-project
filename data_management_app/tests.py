from django.test import TestCase, RequestFactory
from http import HTTPStatus
from data_management_app.models import *
from data_management_app.forms import *
from data_management_app.views import *


class ValveDetailsFormTest(TestCase):
    def test_is_invalid(self):
        form = ValveDetailsForm(data={"valve_serial_number": "123456789",
        "valve_size_in": "3/4",
        "valve_size_dn": "Twenty",
        "valve_rating": "150",
        "valve_manufacturer": "PERAR",
        "valve_item_code": "10AB160B",
        "valve_type": "BALL - FLOATING",
        "valve_seat_type": "SOFT",
        "valve_end_connection": "RF",
        "valve_operator": "LEVER",
        "valve_bore_type": "FB",
        "valve_seat_material": "F22",
        "valve_body_material": "F16",
        "valve_obturator_material": "316F",
        "valve_stem_material": "F22",
        })
        self.assertFalse(form.is_valid())
        self.assertFalse(form.save())

    def test_form_is_valid(self):
        form = ValveDetailsForm(data={"valve_serial_number": "123456789",
        "valve_size_in": "3/4",
        "valve_size_dn": "20",
        "valve_rating": "150",
        "valve_manufacturer": "PERAR",
        "valve_item_code": "10AB160B",
        "valve_type": "BALL - FLOATING",
        "valve_seat_type": "SOFT",
        "valve_end_connection": "RF",
        "valve_operator": "LEVER",
        "valve_bore_type": "FB",
        "valve_seat_material": "F22",
        "valve_body_material": "F16",
        "valve_obturator_material": "316F",
        "valve_stem_material": "F22",
        })
        form.save()
        self.assertTrue(form.is_valid())
        self.assertTrue(form.save())

class SeatTestFormTest(TestCase):
    def test_is_invalid(self):
        form = SeatTestForm(data={'serial_number': '1234',
        'test_medium': 'WATER',
        'test_pressure': '281',
        'test_duration': '15',
        'gauge_serial_number': '125SDF',
        'test_requirements': 'API6A',
        'allowable_leak_rate': '36',
        'seat_a_rlr': '0',
        'seat_b_rlr': '0',
        'seat_c_rlr': '',
        'seat_d_rlr': '',
        'test_date': '2023-04-28',
        'test_result': 'PASS',
        'comments': '',
        })
        self.assertFalse(form.is_valid())

    def test_form_is_valid(self):
        form = SeatTestForm(data={'serial_number': '',
        'test_medium': 'WATER',
        'test_pressure': '281',
        'test_duration': '15',
        'gauge_serial_number': '125SDF',
        'test_requirements': 'API6A',
        'allowable_leak_rate': '36',
        'seat_a_rlr': '0',
        'seat_b_rlr': '0',
        'seat_c_rlr': '',
        'seat_d_rlr': '',
        'test_date': '2023-04-28',
        'test_result': 'PASS',
        'comments': '',
        })
        self.assertTrue(form.is_valid())


# class AddBookViewTests(TestCase):
#     def test_get(self):
#         response = self.client.get('/submit_valve_details')

#         self.assertEqual(response.status_code, HTTPStatus.OK)
#         self.assertContains(response, "<h1>Add Book</h1>", html=True)

#     def test_post_success(self):
#         response = self.client.post('/submit_valve_details', data={
#         "valve_serial_number": "123456789",
#         "valve_size_in": "3/4",
#         "valve_size_dn": "20",
#         "valve_rating": "150",
#         "valve_manufacturer": "PERAR",
#         "valve_item_code": "10AB160B",
#         "valve_type": "BALL - FLOATING",
#         "valve_seat_type": "SOFT",
#         "valve_end_connection": "RF",
#         "valve_operator": "LEVER",
#         "valve_bore_type": "FB",
#         "valve_seat_material": "F22",
#         "valve_body_material": "F16",
#         "valve_obturator_material": "316F",
#         "valve_stem_material": "F22"
#         })

#         self.assertEqual(response.status_code, HTTPStatus.FOUND)
#         self.assertEqual(response["Location"], "/books/")

#     def test_post_error(self):
#         response = self.client.post('/submit_valve_details', data={"title": "Dombey & Son"})

#         self.assertEqual(response.status_code, HTTPStatus.OK)
#         self.assertContains(response, "Use 'and' instead of '&'", html=True)


# class TestCalls(TestCase):
#     def test_forms(self):
#         sn = handle_form_valvedetails()
#         sn.valve_serial_number = '1234'
#         sn.valve_size_in = '3/4"'
#         sn.valve_size_dn = '20'
#         sn.valve_rating = '150'
#         sn.valve_manufacturer = 'PERAR'
#         sn.valve_item_code = '10AB160B'
#         sn.valve_type = 'BALL - FLOATING'
#         sn.valve_seat_type = 'SOFT'
#         sn.valve_end_connection = 'RF'
#         sn.valve_operator = 'LEVER'
#         sn.valve_bore_type = 'FB'
#         sn.valve_seat_material = 'F22'
#         sn.valve_body_material = 'F16'
#         sn.valve_obturator_material = '316F'
#         sn.valve_stem_material = 'F22'
#         sn.save()

#         record=ValveDetails.objects.get(pk=sn.valvedetails_id)
#         self.assertEqual(record, sn)

# class TestValveDetailsForm(TestCase):
#     def setUp(self):
#         self.factory = RequestFactory()
    
#     def test_valid_form_submission(self):
        # request = self.factory.post('/submit_valve_details', {
        # "valve_serial_number": "123456789",
        # "valve_size_in": "3/4",
        # "valve_size_dn": "20",
        # "valve_rating": "150",
        # "valve_manufacturer": "PERAR",
        # "valve_item_code": "10AB160B",
        # "valve_type": "BALL - FLOATING",
        # "valve_seat_type": "SOFT",
        # "valve_end_connection": "RF",
        # "valve_operator": "LEVER",
        # "valve_bore_type": "FB",
        # "valve_seat_material": "F22",
        # "valve_body_material": "F16",
        # "valve_obturator_material": "316F",
        # "valve_stem_material": "F22"
        # })
#         response = handle_form_valvedetails(request)
#         self.assertEqual(response.status_code, 302)
#         self.assertRedirects(response, '/valve_database')
    
    # def test_invalid_form_submission(self):
    #     request = self.factory.post('/submit_valve_details', {
    #     "valve_serial_number": "1234",
    #     "valve_size_in": "3/4",
    #     "valve_size_dn": "20",
    #     "valve_rating": "150",
    #     "valve_manufacturer": "PERAR",
    #     "valve_item_code": "10AB160B",
    #     "valve_type": "BALL - FLOATING",
    #     "valve_seat_type": "SOFT",
    #     "valve_end_connection": "RF",
    #     "valve_operator": "LEVER",
    #     "valve_bore_type": "FB",
    #     "valve_seat_material": "F22",
    #     "valve_body_material": "F16",
    #     "valve_obturator_material": "316F",
    #     "valve_stem_material": "F22"
    #     })
    #     response = handle_form_valvedetails(request)
    #     self.assertEqual(response.status_code, 302)
    #     self.assertRedirects(response, '/valve_database')
    #     messages = list(response.context['messages'])
    #     self.assertEqual(len(messages), 1)
    #     self.assertEqual(str(messages[0]), "Please enter correct data (One serial number cannot be submitted twice!)")