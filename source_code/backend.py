import pandas as pd
import os
import json
from sqlalchemy import create_engine
import psycopg2


def get_mean_value_from_table(col_name):
    """Compute mean_value of column <col_name>"""

    # we laoad the dblogin from the json file
    # NOTE: You need to save your login credentials in a json file to run this code
    with open("db_login.json", "r") as f:
        dblogin = json.load(f)

    # TODO Task 4: initialize database connection
    
    conn = psycopg2.connect(**dblogin)
    
    # TODO Task 4: Read column from database
    try:
        # 3. Spalte mit Pandas direkt aus der Datenbank einlesen
        query = f'SELECT "{col_name}" FROM flask_exercise.test_data'
        df = pd.read_sql(query, conn)

        # 4. Mittelwert berechnen und als Python float zurückgeben
        mean_val = float(df[col_name].mean())
        return mean_val

    finally:
        # Verbindung nach der Abfrage wieder schließen
        conn.close()
