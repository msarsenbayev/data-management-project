# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class ValveDetails(models.Model):
    valvedetails_id = models.AutoField(primary_key=True)
    valve_serial_number = models.CharField(unique=True, max_length=25, blank=False, null=False)
    valve_size_in = models.CharField(max_length=255, blank=False, null=False)
    valve_size_dn = models.IntegerField(blank=False, null=False)
    valve_rating = models.IntegerField(blank=False, null=False)
    valve_manufacturer = models.CharField(max_length=255, blank=False, null=False)
    valve_item_code = models.CharField(max_length=255, blank=False, null=False)
    valve_type = models.CharField(max_length=255, blank=False, null=False)
    valve_seat_type = models.CharField(max_length=255, blank=False, null=False)
    valve_end_connection = models.CharField(max_length=255, blank=False, null=False)
    valve_operator = models.CharField(max_length=255, blank=False, null=False)
    valve_bore_type = models.CharField(max_length=255, blank=False, null=False)
    valve_seat_material = models.CharField(max_length=255, blank=False, null=False)
    valve_body_material = models.CharField(max_length=255, blank=False, null=False)
    valve_obturator_material = models.CharField(max_length=255, blank=False, null=False)
    valve_stem_material = models.CharField(max_length=255, blank=False, null=False)

    def __str__(self):
        return self.valve_serial_number   
 

class SeatTest(models.Model):
    seattest_id = models.AutoField(primary_key=True)
    serial_number = models.ForeignKey(ValveDetails, blank=True, null=True, on_delete=models.CASCADE)
    test_medium = models.CharField(max_length=100, blank=False, null=False)
    test_pressure = models.FloatField(blank=False, null=False)
    test_duration = models.IntegerField(blank=False, null=False)
    gauge_serial_number = models.CharField(max_length=100, blank=False, null=False)
    test_requirements = models.CharField(max_length=100, blank=False, null=False)
    allowable_leak_rate = models.CharField(max_length=100, blank=False, null=False)
    seat_a_rlr = models.CharField(max_length=100, blank=False, null=False)
    seat_b_rlr = models.CharField(max_length=100, blank=False, null=False)
    seat_c_rlr = models.CharField(max_length=100, blank=True, null=True)
    seat_d_rlr = models.CharField(max_length=100, blank=True, null=True)
    test_date = models.DateField(blank=False, null=False)
    test_result = models.CharField(max_length=100, blank=False, null=False)
    comments = models.TextField(max_length=100, blank=True, null=True)

    def __str__(self):
        return str(self.serial_number)


class ShellTest(models.Model):
    shelltest_id = models.AutoField(primary_key=True)
    serial_number = models.ForeignKey(ValveDetails, blank=True, null=True, on_delete=models.CASCADE)
    test_medium = models.CharField(max_length=100, blank=False, null=False)
    test_pressure = models.IntegerField(blank=False, null=False)
    test_duration = models.IntegerField(blank=False, null=False)
    gauge_serial_number = models.CharField(max_length=100, blank=False, null=False)
    test_requirements = models.CharField(max_length=100, blank=False, null=False)
    allowable_leak_rate = models.IntegerField(blank=False, null=False)
    recorded_leak_rate = models.IntegerField(blank=False, null=False)
    test_date = models.DateField(blank=False, null=False)
    test_result = models.CharField(max_length=100, blank=False, null=False)
    comments = models.TextField(max_length=100, blank=True, null=True)

    def __str__(self):
        return str(self.serial_number)


class BackSeatTest(models.Model):
    backseattest_id = models.AutoField(primary_key=True)
    serial_number = models.ForeignKey(ValveDetails, blank=True, null=True, on_delete=models.CASCADE)
    test_medium = models.CharField(max_length=100, blank=False, null=False)
    test_pressure = models.IntegerField(blank=False, null=False)
    test_duration = models.IntegerField(blank=False, null=False)
    gauge_serial_number = models.CharField(max_length=100, blank=False, null=False)
    test_requirements = models.CharField(max_length=100, blank=False, null=False)
    allowable_leak_rate = models.IntegerField(blank=False, null=False)
    recorded_leak_rate = models.IntegerField(blank=False, null=False)
    test_date = models.DateField(blank=False, null=False)
    test_result = models.CharField(max_length=100, blank=False, null=False)
    comments = models.TextField(max_length=100, blank=True, null=True)

    def __str__(self):
        return str(self.serial_number)


class ValveReceipt(models.Model):
    valvereceipt_id = models.AutoField(primary_key=True)
    serial_number = models.ForeignKey(ValveDetails, blank=True, null=True, on_delete=models.CASCADE)
    camserv_tagnumber = models.CharField(max_length=100, blank=False, null=False)
    #valve_serial_number = models.CharField(max_length=100, blank=False, null=False)
    box_number = models.CharField(max_length=100, blank=False, null=False)
    received_date = models.DateField(blank=False, null=False)
    comments = models.TextField(max_length=100)

    def __str__(self):
        return str(self.serial_number)
    

class ValveDispatch(models.Model):
    valvedispatch_id = models.AutoField(primary_key=True)
    serial_number = models.ForeignKey(ValveDetails, blank=True, null=True, on_delete=models.CASCADE)
    camserv_tagnumber = models.CharField(max_length=100, blank=False, null=False)
    #valve_serial_number = models.CharField(max_length=100, blank=False, null=False)
    box_number = models.CharField(max_length=100, blank=False, null=False)
    dispatch_date = models.DateField(blank=False, null=False)
    comments = models.TextField(max_length=100)

    def __str__(self):
        return str(self.serial_number)


class ValveInspection(models.Model):
    valveinspection_id = models.AutoField(primary_key=True)
    serial_number = models.ForeignKey(ValveDetails, blank=True, null=True, on_delete=models.CASCADE)
    #valve_serial_number = models.CharField(max_length=100, blank=False, null=False)
    inspection_codes = models.CharField(max_length=100, blank=False, null=False)
    inspected_date = models.DateField(blank=False, null=False)
    inspected_by = models.CharField(max_length=100, blank=False, null=False)
    issues_identified = models.TextField(max_length=200, blank=False, null=False)

    def __str__(self):
        return str(self.serial_number)


class ValvePreservation(models.Model):
    valvepreservation_id = models.AutoField(primary_key=True)
    serial_number = models.ForeignKey(ValveDetails, blank=True, null=True, on_delete=models.CASCADE)
    #valve_serial_number = models.CharField(max_length=100, blank=False, null=False)
    preservation_codes = models.CharField(max_length=100, blank=False, null=False)
    preservation_date = models.DateField(blank=False, null=False)
    preservation_by = models.CharField(max_length=100, blank=False, null=False)
    comments = models.TextField(max_length=200, blank=False, null=False, default='None')

    def __str__(self):
        return str(self.serial_number)
    

class myjoinedtable(models.Model):
    valve_serial_number = models.CharField(max_length=100, blank=False, null=False)
    valve_size_in = models.IntegerField(blank=False, null=False)
    valve_rating = models.IntegerField(blank=False, null=False)
    valve_manufacturer = models.CharField(max_length=100, blank=False, null=False)
    seattest_result = models.CharField(max_length=100, blank=False, null=False)
    shelltest_result = models.CharField(max_length=100, blank=False, null=False)
    backtest_result = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.valve_serial_number


# class valvetestingfacttable(models.Model):
#     valvetestingfacttable_id = models.AutoField(primary_key=True)
#     valve_sn = models.ForeignKey(ValveDetails, blank=True, null=True, on_delete=models.CASCADE)
#     seattest = models.ForeignKey(SeatTest, blank=True, null=True, on_delete=models.CASCADE)
#     shelltest = models.ForeignKey(ShellTest, blank=True, null=True, on_delete=models.CASCADE)
#     backseattest = models.ForeignKey(BackSeatTest, blank=True, null=True, on_delete=models.CASCADE)
#     final_test_result = models.CharField(max_length=100, blank=False, null=False)

#     def __str__(self):
#         return str(self.valve_sn)