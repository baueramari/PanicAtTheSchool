import pandas as pd

colnames = ['id', 'case_number', 'date', 'iucr',
       'primary_type', 'description', 'arrest',
       'domestic', 'district', 'ward', 'community_area', 'fbi_code',
        'year', 'updated_on']
crime = pd.read_csv('raw_data/crimes.csv', usecols = colnames)
#clean columns, subset to years that we're interested in
#create subset with crime counts and averages by ward