import pandas as pd
import sqlite3
from django.core.management.base import BaseCommand
from data_management_app.models import *

class Command(BaseCommand):
    help = 'import data from csv file'

    def handle(self, *args, **options):

        ValveDetails.objects.all().delete()