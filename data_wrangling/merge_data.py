from pathlib import Path
import pandas as pd
cwd = Path.cwd()
parent_dir = cwd.parent

avg_attend = pd.read_csv(parent_dir/"data_wrangling/cleaned_data/avg_attend.csv")
crime_by_ward = pd.read_csv(parent_dir/"data_wrangling/cleaned_data/crime_by_ward.csv")
schoolid_ward_map = pd.read_csv(parent_dir/"data_wrangling/cleaned_data/schoolid_ward_map.csv")

low_crime = crime_by_ward["crime_capita"].quantile(0.25)
medium_crime = crime_by_ward["crime_capita"].quantile(0.75)
high_crime = float("inf")
crime_by_ward["crime_class"] = pd.cut(
    crime_by_ward["crime_capita"],
    bins=[0, low_crime, medium_crime, high_crime],
    labels=["Low", "Medium", "High"],
)
id_crime_merge = crime_by_ward.merge(
    schoolid_ward_map, how="left", left_on="ward", right_on="Wards"
)
attend_id_crime = id_crime_merge.merge(
    avg_attend,
    how="left",
    left_on=["School_ID", "year"],
    right_on=["School ID", "Year"],
)
attend_id_crime.dropna(how="all", subset=["Year", "Attendance"], inplace=True)

attend_id_crime = attend_id_crime[
    [
        "School_ID",
        "Wards",
        "crime_capita",
        "crime_class",
        "Year",
        "Attendance",
        "Network",
    ]
]
attend_id_crime["Year"] = attend_id_crime["Year"].astype(int)

attend_by_crime = attend_id_crime.groupby(
    by=["crime_class", "Year"], as_index=False
).mean("Attendance")
attend_by_crime = attend_by_crime[["crime_class", "Year", "Attendance"]]

attend_id_crime.to_csv(parent_dir/"data_wrangling/merged_data/attend_id_crime.csv")
attend_by_crime.to_csv(parent_dir/"data_wrangling/merged_data/attend_by_crime.csv")


# Sarah's data merge needed for her visuals

crime_cols = [
    "School_ID",
    "crime_class",
    "Attendance",
]
ID_crimeclass = pd.read_csv(
    parent_dir/"data_wrangling/merged_data/attend_id_crime.csv", usecols=crime_cols
)
suspensions = pd.read_csv(parent_dir/"data_wrangling/cleaned_data/suspension_data.csv")

high_schools = suspensions["School ID"].unique().tolist()
ID_crimeclass = ID_crimeclass[ID_crimeclass["School_ID"].isin(high_schools)]

# merge csv to compare suspensions and crime_class
suspension_crime_merge = pd.merge(
    suspensions, ID_crimeclass, left_on="School ID", right_on="School_ID"
)
suspension_crime_merge.drop("School_ID", axis=1, inplace=True)
suspension_crime_merge.drop("Attendance", axis=1, inplace=True)
suspension_crime_merge.drop_duplicates(inplace=True)
suspension_crime_merge.dropna(how="all", inplace=True)

avg_suspension_crime = suspension_crime_merge.groupby(
    by="crime_class", as_index=False
).mean(numeric_only=True)
avg_suspension_crime.drop("School ID", axis=1, inplace=True)
avg_suspension_crime.to_csv(parent_dir/"data_wrangling/merged_data/avg_suspension_crime.csv")

# merge csv to compare suspensions and attendance
suspension_attend_merge = pd.merge(
    suspensions, ID_crimeclass, left_on="School ID", right_on="School_ID"
)
suspension_attend_merge.drop("School_ID", axis=1, inplace=True)
suspension_attend_merge.drop("crime_class", axis=1, inplace=True)
suspension_attend_merge.drop_duplicates(inplace=True)
suspension_attend_merge.dropna(how="all", inplace=True)

avg_suspension_attend = suspension_attend_merge.groupby(
    by="School ID", as_index=False
).mean(numeric_only=True)

avg_suspension_attend.to_csv(parent_dir/"data_wrangling/merged_data/suspension_attendance.csv")


#Eshan's school merge/analysis code (initially bucket-2)
#Objective is to merge all school data, then create csvs for Sarah that she can use to plot


sch_geo = pd.read_csv(parent_dir/"raw_data/geo_map/school_locs_polygon_shape.csv")
sch_profile = pd.read_csv(parent_dir/"data_wrangling/cleaned_data/clean_school_admin.csv")
sch_att = pd.read_csv(parent_dir/"data_wrangling/cleaned_data/clean_attendance.csv")
sch_finance = pd.read_csv(parent_dir/"data_wrangling/cleaned_data/clean_school_budget.csv")
sch_teachers = pd.read_csv(parent_dir/"data_wrangling/cleaned_data/clean_teacher.csv")

school_merged = sch_geo.merge(sch_profile, left_on="School_ID", right_on="sch_id")
school_merged = school_merged.merge(sch_att, left_on="sch_id", right_on="School ID")
school_merged = school_merged.merge(
    sch_finance, left_on="fin_id", right_on="finance_id"
)
school_merged = school_merged.merge(
    sch_teachers, how="left", left_on="sch_id", right_on="School_ID"
)

# Standardizing data and removing additional columns
school_merged["dolla_per_student"] = (
    school_merged["fy_2022_proposed_budget"] / school_merged["tot_student"]
)
school_merged["salary_per_teacher"] = school_merged["teacher_salary"].divide(
    school_merged["teachers"]
)
cols_to_drop = [
    "School_ID_x",
    "School_ID_y",
    "School Name",
    "Unnamed: 0",
    "School ID",
    "finance_id",
    "fy_2022_proposed_budget",
    "teacher_salary",
]
school_merged = school_merged.drop(cols_to_drop, axis=1)

# For Analysis:
# 1. 2*2 plotting of schools into low-high buckets
mean_pre_cov_att = school_merged["pre_cov_att"].mean()
mean_post_cov_att = school_merged["post_cov_att"].mean()

school_merged["pre_att_bucket"] = school_merged.apply(
    lambda row: "low" if row["pre_cov_att"] < mean_pre_cov_att else "high", axis=1
)
school_merged["post_att_bucket"] = school_merged.apply(
    lambda row: "low" if row["post_cov_att"] < mean_post_cov_att else "high", axis=1
)
school_merged.to_csv(parent_dir/"data_wrangling/merged_data/all_school_merged.csv")
#Eshan-Other analysis pending
#Eshan's merge/analysis of school attendance-demographic data

cols_to_keep = ["ca_id", "pre_cov_att","post_cov_att","att_diff_pp"]
att_demo = school_merged.loc[:,cols_to_keep]

demog_info = pd.read_csv(parent_dir/"data_wrangling/cleaned_data/clean_demog.csv")
health_info = pd.read_csv(parent_dir/"data_wrangling/cleaned_data/clean_health_atlas.csv")
# Note: Check the keys in each file before merging
# Now group data by ca_id but also take count of schools for each ca_id
cols_grouping = {"ca_id": "count"}
cols_grouping.update({col: "mean" for col in att_demo.columns if col != "ca_id"})
att_demo = att_demo.groupby("ca_id").agg(cols_grouping)
att_demo = att_demo.rename(columns={"ca_id": "count_schools"})
att_demo = att_demo.reset_index()

# Threshold for number of schools
num_schools = 3
att_demo = att_demo[att_demo["count_schools"] >= num_schools]

#School data ready, now merge demographic and health data with this
merged_att_demo = pd.merge(att_demo, demog_info, on="ca_id")
merged_att_demo = pd.merge(merged_att_demo, health_info, on="ca_id")
cols_to_drop = ["comm_area_y"]
merged_att_demo = merged_att_demo.drop(cols_to_drop, axis=1)
#print(merged_att_demo.columns)
merged_att_demo.to_csv(parent_dir/"data_wrangling/merged_data/school_demo_merged.csv", index=False)