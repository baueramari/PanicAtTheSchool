#In this file, I will rearrange merged file columns, and run:
#1. PCA to remove unnecessary columns 
#2. Run regression on reduced column space
#This file should tell me what variables should be plotted while analysing attendance

import pandas as pd
from sklearn.preprocessing import StandardScaler

merged_df = pd.read_csv("/home/eshanprashar/PanicAtTheSchool/data_wrangling/bucket_1_ep/b_1_clean_data/school_demo_hl_merged.csv")

#For, analysis: drop unnecessary columns, rorder and normalize
merged_df = merged_df.drop(["tot_student","perc_white_stu","School ID","2018","2019","2021","2022","comm_area_y",\
"med_age","perc_white","perc_other_races"], axis = 1)

print(merged_df)