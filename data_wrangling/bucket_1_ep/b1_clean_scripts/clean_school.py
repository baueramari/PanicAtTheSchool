# The objective of this code is to clean school data; specifically:
# 1. attendance data, 
# 2. school profile data

import pandas as pd

# Check final location and name of file- will definitely lead to bugs in case of incorrect pathname
att_df = pd.read_csv("/home/eshanprashar/PanicAtTheSchool/raw_data/attendance.csv")
att_df = att_df.loc[
    :,
    ["School ID", "School Name", "Network", "Grade", "2018", "2019", "2021", "2022"],
]
#Clean dataset
#Too many values to impute; will drop rows with NAs. But first, extract columns that make sense
grades_to_filter = ["Pre-K", "9", "10", "11", "12"]
att_df = att_df.loc[att_df["Grade"].isin(grades_to_filter)]
att_df = att_df.dropna()

#Now group attendance by school ID
att_df_group_sid = att_df.groupby(["School ID", "School Name", "Network"])[
    ["2018", "2019", "2021", "2022"]
].mean()
att_df_group_sid = att_df_group_sid.reset_index()

#Adding cols for pre-Covid, post-Covid and p.p. diff 
att_df_group_sid["pre_cov_att"] = att_df_group_sid[["2018","2019"]].mean(axis = 1)
att_df_group_sid["post_cov_att"] = att_df_group_sid[["2021","2022"]].mean(axis = 1)
att_df_group_sid["att_diff_pp"] = att_df_group_sid["post_cov_att"] - att_df_group_sid["pre_cov_att"]

att_df_group_sid.to_csv("clean_attendance_ep.csv", index=False)

# Work with school_admin csv to extract relevant cols and merge with attendance data
# Check final location and name of file- will definitely lead to bugs in case of incorrect pathname
school_prf_df = pd.read_csv("/home/eshanprashar/PanicAtTheSchool/raw_data/admin_demog.csv")
school_prf_df = school_prf_df.loc[
    :,
    [
        "School_ID",
        "Community Areas",
        "Finance_ID",
        "Student_Count_Total",
        "Student_Count_Low_Income",
        "Student_Count_Black",
        "Student_Count_Hispanic",
        "Student_Count_White",
        "Transportation_Bus",
    ],
]
#Add new measures to data and drop schools that don't have total student count
school_prf_df["perc_black_stu"] = school_prf_df["Student_Count_Black"]/school_prf_df["Student_Count_Total"]
school_prf_df["perc_hisp_stu"] = school_prf_df["Student_Count_Hispanic"]/school_prf_df["Student_Count_Total"]
school_prf_df["perc_white_stu"] = school_prf_df["Student_Count_White"]/school_prf_df["Student_Count_Total"]
school_prf_df["perc_low_income"] = school_prf_df["Student_Count_Low_Income"]/school_prf_df["Student_Count_Total"]
school_prf_df["bus_count"] = school_prf_df['Transportation_Bus'].apply(lambda x: len(str(x).split(',')) if pd.notna(x) else 0)

#filtering schools that don't have minimum threshold of children
min_stu_count = 50 
school_prf_df = school_prf_df[school_prf_df['Student_Count_Total'] > min_stu_count]

#Reordering and renaming columns
school_prf_df = school_prf_df.loc[
    :,
    [
        "School_ID",
        "Community Areas",
        "Finance_ID",
        "Student_Count_Total",
        "perc_low_income",
        "perc_black_stu",
        "perc_hisp_stu",
        "perc_white_stu",
        "bus_count",
    ],
]
school_prf_df = school_prf_df.rename(
    columns={
        "School_ID": "sch_id",
        "Community Areas": "ca_id",
        "Finance_ID": "fin_id",
        "Student_Count_Total": "tot_student"
    }
)
school_prf_df.to_csv("clean_school_admin_ep.csv", index=False)