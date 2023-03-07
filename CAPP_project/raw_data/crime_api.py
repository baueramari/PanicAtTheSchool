"""
Amari wrote this file.
This file requires a poetry environment and private API key.
"""
import pandas as pd
from sodapy import Socrata
import os
from dotenv import load_dotenv


def crime_extract():
    """
    Function to pull crime data from Chicago data portal API
    """
    load_dotenv()
    TOKEN = os.environ["TOKEN"]

    client = Socrata("data.cityofchicago.org", TOKEN, timeout=1200)

    results = client.get("ijzp-q8t2", limit=8000000)

    results_df = pd.DataFrame.from_records(results)
    results_df.to_csv("CAPP_project/raw_data/crime.csv")
