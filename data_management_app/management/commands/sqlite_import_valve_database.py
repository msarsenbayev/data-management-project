import pandas as pd
import sqlite3
from data_management_app.models import *

conn = sqlite3.connect('db.sqlite3')

data = "valve_data.csv"

df = pd.read_csv(data)
df.to_sql(ValveDetails._meta.db_table, conn, if_exists='append', index=False)