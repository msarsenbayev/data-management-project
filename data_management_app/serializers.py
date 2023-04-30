from rest_framework import serializers
from .models import *

class ValveDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ValveDetails
        fields = '__all__'


class SeatTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = SeatTest
        fields = '__all__'


class ShellTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShellTest
        fields = '__all__'


class BackSeatTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = BackSeatTest
        fields = '__all__'