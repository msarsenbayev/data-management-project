import pandas as pd
import sqlite3
from django.core.management.base import BaseCommand
# from data_management_app.models import *

class Command(BaseCommand):
    help = 'import data from csv file'

    def handle(self, *args, **options):

        data = "valve_data.csv"
        df = pd.read_csv(data)
        df.columns=df.columns.str.strip()
        conn = sqlite3.connect('db.sqlite3')
        df.to_sql('data_management_app_valvedetails', conn, if_exists='append', index=False)