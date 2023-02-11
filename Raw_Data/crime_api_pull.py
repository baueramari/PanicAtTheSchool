import pandas as pd
from sodapy import Socrata

client = Socrata('data.cityofchicago.org',
                  'thcdLYLxkemKtnhH7zQBnZAc9')

# First 2000 results, returned as JSON from API / converted to Python list of
# dictionaries by sodapy.
results = client.get("ijzp-q8t2", limit=2000)

# Convert to pandas DataFrame
results_df = pd.DataFrame.from_records(results)
results_df.to_csv('crimes.csv')
