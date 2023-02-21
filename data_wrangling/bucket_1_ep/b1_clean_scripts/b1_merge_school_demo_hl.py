#Objective of this file is to merge all data for bucket-1 analysis;
#Pending: Teacher data

import pandas as pd

school_profile = pd.read_csv("/home/eshanprashar/PanicAtTheSchool/data_wrangling/bucket_1_ep/b_1_clean_data/clean_school_admin_ep.csv")
school_att = pd.read_csv("/home/eshanprashar/PanicAtTheSchool/data_wrangling/bucket_1_ep/b_1_clean_data/clean_attendance_ep.csv")
sch_finance = pd.read_csv("/home/eshanprashar/PanicAtTheSchool/data_wrangling/bucket_1_ep/b_1_clean_data/clean_school_budget.csv")
demog_info = pd.read_csv("/home/eshanprashar/PanicAtTheSchool/data_wrangling/bucket_1_ep/b_1_clean_data/clean_demog.csv")
health_info = pd.read_csv("/home/eshanprashar/PanicAtTheSchool/data_wrangling/bucket_1_ep/b_1_clean_data/clean_health_atlas.csv")

#Note: Check the keys in each file before merging
merged_df = school_profile.merge(school_att, left_on ='sch_id', right_on = "School ID")
merged_df = merged_df.merge(sch_finance, left_on = "fin_id", right_on = "finance_id")
#merged_df = pd.merge(merged_df, demog_info, on = "ca_id")
#merged_df = pd.merge(merged_df, health_info, on = "ca_id")
#merged_df.to_csv("school_demo_hl_merged.csv", index=False)
print(merged_df.columns)