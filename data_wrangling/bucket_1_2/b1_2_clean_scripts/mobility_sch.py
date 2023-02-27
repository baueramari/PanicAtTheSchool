##In-progress file; do not edit
##Objective is to figure out a better algorithm for name-matching using python's recordlinkage library

import pandas as pd
from pyjarowinkler import distance

df_school = pd.read_csv("/home/eshanprashar/PanicAtTheSchool/raw_data/admin_demog.csv") #Student_Count_Total
df_mobility = pd.read_csv("/home/eshanprashar/PanicAtTheSchool/raw_data/mobility/mobility_data.csv")
df_mobility = df_mobility[df_mobility["City"].str.contains("Chicago")]

df_school = df_school[["Long_Name","Student_Count_Total"]]

df_teacher = pd.read_csv("/home/eshanprashar/PanicAtTheSchool/raw_data/school_info_ep/EducationDataPortal_02.16.2023_Schools.csv")
df_teacher = df_teacher[df_teacher["lea_name"].str.contains("Chicago")]

indexer = recordlinkage.BlockIndex(on = "school_name")

compare = recordlinkage.Compare()
compare.exact("school_name", "Long_Name", label = 'name_match')
compare.string("school_name", "Long_Name", method = 'jarowinkler', threshold = 0.9, label = "jw_match")
features = compare.compute(indexer, df_teacher, df_school)

matches = features[features["jw_match"] == 1].reset_index()
matches = matches[["level_1", "school_name"]]
matches = matches.rename(columns = {"level_1":"school_id"})