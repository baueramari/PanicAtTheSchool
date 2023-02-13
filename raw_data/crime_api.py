import pandas as pd
from sodapy import Socrata

client = Socrata('data.cityofchicago.org',
                  'thcdLYLxkemKtnhH7zQBnZAc9', timeout = 1200)

results = client.get("ijzp-q8t2", limit = 8000000)

results_df = pd.DataFrame.from_records(results)
results_df.to_csv('raw_data/crimes.csv')
