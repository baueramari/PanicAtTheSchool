#Objective of this file is to merge all school data to show relationship of attendance with school variables
import pandas as pd

sch_geo = pd.read_csv(
    "/home/eshanprashar/PanicAtTheSchool/raw_data/geo_map_ep/school_locs_polygon_shape.csv"
)
sch_profile = pd.read_csv(
    "/home/eshanprashar/PanicAtTheSchool/data_wrangling/bucket_1_2/b_1_2_clean_data/clean_school_admin_ep.csv"
)
sch_att = pd.read_csv(
    "/home/eshanprashar/PanicAtTheSchool/data_wrangling/bucket_1_2/b_1_2_clean_data/clean_attendance_ep.csv"
)
sch_finance = pd.read_csv(
    "/home/eshanprashar/PanicAtTheSchool/data_wrangling/bucket_1_2/b_1_2_clean_data/clean_school_budget.csv"
)
sch_teachers = pd.read_csv("/home/eshanprashar/PanicAtTheSchool/data_wrangling/bucket_1_2/b_1_2_clean_data//clean_teacher.csv")

school_merged = sch_geo.merge(sch_profile, left_on = "School_ID", right_on = "sch_id")
school_merged = school_merged.merge(sch_att, left_on="sch_id", right_on="School ID")
school_merged = school_merged.merge(sch_finance, left_on="fin_id", right_on="finance_id")
school_merged = school_merged.merge(sch_teachers, how = "left", left_on = "sch_id", right_on = "School_ID")

#Standardizing data and removing additional columns
school_merged["dolla_per_student"] = (school_merged["fy_2022_proposed_budget"] / school_merged["tot_student"])
school_merged["salary_per_teacher"] = school_merged["teacher_salary"].divide(school_merged["teachers"])
cols_to_drop = [
    "sch_id",
    "School Name",
    "Unnamed: 0",
    "School ID",
    "finance_id",
    "fy_2022_proposed_budget",
    "teacher_salary"
]
school_merged = school_merged.drop(cols_to_drop, axis=1)
school_merged.to_csv("/home/eshanprashar/PanicAtTheSchool/data_wrangling/bucket_1_2/b1_2_analysis/b2_school_merged.csv")