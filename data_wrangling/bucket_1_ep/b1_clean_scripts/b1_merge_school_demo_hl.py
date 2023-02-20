#Objective of this file is to merge all data for bucket-1 analysis; 
#Let's see if normalization and analysis need to be done here 

import pandas as pd

school_profile = pd.read_csv("/home/eshanprashar/PanicAtTheSchool/data_wrangling/bucket_1_ep/b_1_clean_normalized_data/clean_school_admin_ep.csv")
school_att = pd.read_csv("/home/eshanprashar/PanicAtTheSchool/data_wrangling/bucket_1_ep/b_1_clean_normalized_data/clean_attendance_ep.csv")
demog_info = pd.read_csv("/home/eshanprashar/PanicAtTheSchool/data_wrangling/bucket_1_ep/b_1_clean_normalized_data/clean_demog.csv")
health_info = pd.read_csv("/home/eshanprashar/PanicAtTheSchool/data_wrangling/bucket_1_ep/b_1_clean_normalized_data/clean_health_atlas.csv")

#Note: Check the keys in each file before merging
merged_df = school_profile.merge(school_att, left_on ='sch_id', right_on = "School ID")
merged_df = pd.merge(merged_df, demog_info, on = "ca_id")
merged_df = pd.merge(merged_df, health_info, on = "ca_id")
print(merged_df.columns)
