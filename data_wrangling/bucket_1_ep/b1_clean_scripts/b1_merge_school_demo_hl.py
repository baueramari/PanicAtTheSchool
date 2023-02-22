# Objective of this file is to merge all data for bucket-1 analysis;
# File owner: Eshan
# Pending: Teacher data

import pandas as pd

school_profile = pd.read_csv(
    "/home/eshanprashar/PanicAtTheSchool/data_wrangling/bucket_1_ep/b_1_clean_data/clean_school_admin_ep.csv"
)
school_att = pd.read_csv(
    "/home/eshanprashar/PanicAtTheSchool/data_wrangling/bucket_1_ep/b_1_clean_data/clean_attendance_ep.csv"
)
sch_finance = pd.read_csv(
    "/home/eshanprashar/PanicAtTheSchool/data_wrangling/bucket_1_ep/b_1_clean_data/clean_school_budget.csv"
)
demog_info = pd.read_csv(
    "/home/eshanprashar/PanicAtTheSchool/data_wrangling/bucket_1_ep/b_1_clean_data/clean_demog.csv"
)
health_info = pd.read_csv(
    "/home/eshanprashar/PanicAtTheSchool/data_wrangling/bucket_1_ep/b_1_clean_data/clean_health_atlas.csv"
)

# Note: Check the keys in each file before merging
merged_df = school_profile.merge(school_att, left_on="sch_id", right_on="School ID")
merged_df = merged_df.merge(sch_finance, left_on="fin_id", right_on="finance_id")

# To group this data at community level, we don't need school-specific, so drop cols
merged_df["dolla_per_student"] = (
    merged_df["fy_2022_proposed_budget"] / merged_df["tot_student"]
)
cols_to_drop = [
    "sch_id",
    "fin_id",
    "School Name",
    "School ID",
    "finance_id",
    "fy_2022_proposed_budget",
]
merged_df = merged_df.drop(cols_to_drop, axis=1)

# Now group data by ca_id but also take count of schools for each ca_id
cols_grouping = {"ca_id": "count"}
cols_grouping.update({col: "mean" for col in merged_df.columns if col != "ca_id"})
merged_df = merged_df.groupby("ca_id").agg(cols_grouping)
merged_df = merged_df.rename(columns={"ca_id": "count_schools"})
merged_df = merged_df.reset_index()

# Threshold for number of schools
num_schools = 0
merged_df = merged_df[merged_df["count_schools"] >= num_schools]

# School data ready, now merge demographic and health data with this
merged_df = pd.merge(merged_df, demog_info, on="ca_id")
merged_df = pd.merge(merged_df, health_info, on="ca_id")
cols_to_drop = ["comm_area_y"]
merged_df = merged_df.drop(cols_to_drop, axis=1)
# print(merged_df.columns)
merged_df.to_csv("school_demo_hl_merged.csv", index=False)