import pandas as pd
from sodapy import Socrata

client = Socrata('data.cityofchicago.org',
                  'thcdLYLxkemKtnhH7zQBnZAc9')

results = client.get("ijzp-q8t2", limit=2000)
#Eliminate limit when doing full-scale analyses

results_df = pd.DataFrame.from_records(results)
results_df.to_csv('crimes.csv')
