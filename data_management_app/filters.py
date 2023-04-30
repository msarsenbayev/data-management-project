from django_filters import rest_framework as filters
from django.db.models import Count
from .models import *

class ValveDetailsFilter(filters.FilterSet):

    valve_serial_number = filters.CharFilter()
    valve_manufacturer = filters.ChoiceFilter(choices=[])
    valve_type = filters.ChoiceFilter(choices=[])
    valve_seat_type = filters.ChoiceFilter(choices=[])
    valve_size_in = filters.ChoiceFilter(choices=[])
    valve_rating = filters.ChoiceFilter(choices=[])

    class Meta:
        model = ValveDetails
        fields = ['valve_manufacturer', 'valve_type', 'valve_seat_type', 'valve_size_in', 'valve_rating']

    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        ###
        # Get a list of unique values for the my_field field
        queryset = ValveDetails.objects.order_by().values_list('valve_manufacturer', flat=True).distinct()

        # Create a list of tuples for the filter choices
        choices = [(value, value) for value in queryset]

        # Set the filter choices
        self.filters['valve_manufacturer'].field.choices = choices
        self.filters['valve_manufacturer'].label = 'valve_manufacturer'

        ###
        # Get a list of unique values for the my_field field
        queryset = ValveDetails.objects.order_by().values_list('valve_type', flat=True).distinct()

        # Create a list of tuples for the filter choices
        choices = [(value, value) for value in queryset]

        # Set the filter choices
        self.filters['valve_type'].field.choices = choices
        self.filters['valve_type'].label = 'valve_type'

        ###
        # Get a list of unique values for the my_field field
        queryset = ValveDetails.objects.order_by().values_list('valve_seat_type', flat=True).distinct()

        # Create a list of tuples for the filter choices
        choices = [(value, value) for value in queryset]

        # Set the filter choices
        self.filters['valve_seat_type'].field.choices = choices
        self.filters['valve_seat_type'].label = 'valve_seat_type'

        ###
        # Get a list of unique values for the my_field field
        queryset = ValveDetails.objects.order_by().values_list('valve_size_in', flat=True).distinct()

        # Create a list of tuples for the filter choices
        choices = [(value, value) for value in queryset]

        # Set the filter choices
        self.filters['valve_size_in'].field.choices = choices
        self.filters['valve_size_in'].label = 'Valve Size (in)'

        ###
        # Get a list of unique values for the my_field field
        queryset = ValveDetails.objects.order_by().values_list('valve_rating', flat=True).distinct()

        # Create a list of tuples for the filter choices
        choices = [(value, value) for value in queryset]

        # Set the filter choices
        self.filters['valve_rating'].field.choices = choices
        self.filters['valve_rating'].label = 'Valve Rating'


class SeatTestFilter(filters.FilterSet):

    serial_number = filters.CharFilter()
    test_medium = filters.ChoiceFilter(choices=[])
    test_date = filters.DateFilter()
    test_result = filters.ChoiceFilter(choices=[])


    class Meta:
        model = SeatTest
        fields = ['serial_number', 'test_medium', 'test_date', 'test_result']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        ###
        # Get a list of unique values for the my_field field
        queryset = SeatTest.objects.order_by().values_list('test_medium', flat=True).distinct()

        # Create a list of tuples for the filter choices
        choices = [(value, value) for value in queryset]

        # Set the filter choices
        self.filters['test_medium'].field.choices = choices

        ###
        # Get a list of unique values for the my_field field
        queryset = SeatTest.objects.order_by().values_list('test_result', flat=True).distinct()

        # Create a list of tuples for the filter choices
        choices = [(value, value) for value in queryset]

        # Set the filter choices
        self.filters['test_result'].field.choices = choices


        