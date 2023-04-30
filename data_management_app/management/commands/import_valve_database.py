from django.core.management.base import BaseCommand
import pandas as pd
from data_management_app.models import ValveDetails
from sqlalchemy import create_engine
from django.conf import settings

class Command(BaseCommand):
    help = 'import data from csv file'

    def handle(self, *args, **options):
        
        csv_file = "valve_data.csv"
        df = pd.read_csv(csv_file)

        user = settings.DATABASES['default']['USER']
        password = settings.DATABASES['default']['PASSWORD']
        database_name = settings.DATABASES['default']['NAME']

        # engine = create_engine('sqlite:///db.sqlite3')
        database_url = 'postgresql://{user}:{password}@localhost:5432/{database_name}'.format( user=user,password=password,database_name=database_name,)

        engine = create_engine(database_url, echo=False)

        df.to_sql(ValveDetails._meta.db_table, if_exists='append', con=engine, index=False)

'''

    ###########import data to database##############################
    def import_valve_database(self, *args, **options):
        reader = pd.read_csv("valve_testing_register_aktau.csv")
        for row in reader:
            obj = ValveDetails(
                valve_serial_number = row["SERIAL_NUMBER"],
                valve_size_in = row["SIZE_IN"],
                valve_size_dn = row["SIZE_IN"],
                valve_rating = row["RATING"],
                valve_manufacturer = row["MANUFACTURER"],
                valve_item_code = row["ITEM_CODE"],
                valve_type = row["VALVE_TYPE"],
                valve_seat_type = row["SEAT_TYPE"],
                valve_end_connection = row["END_CONNECTION"],
                valve_operator = row["OPERATOR"],
                valve_bore_type = row["BORE"],
                valve_seat_material = row["SEAT_MATERIAL"],
                valve_body_material = row["BODY_MATERIAL"],
                valve_obturator_material = row["OBTURATOR_MATERIAL"],
                valve_stem_material = row["STEM_MATERIAL"]
            )
            # Save the instance to the database
            obj.save()

            '''