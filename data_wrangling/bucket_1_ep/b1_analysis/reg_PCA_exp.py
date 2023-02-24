# In this file, I will rearrange merged file columns, and run:
# 1. Make scatterplots, look at correlation coefficients -- Done
# 2. Run regression on reduced column space -- Done
# 3. Backlog: Try to run PCA to, reduce matrix size and then run regression
# This file should tell me what variables should be plotted while analysing attendance

import pandas as pd
from sklearn.model_selection import train_test_split #has not been used yet
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import statsmodels.api as sm

merged_df = pd.read_csv(
    "/home/eshanprashar/PanicAtTheSchool/data_wrangling/bucket_1_ep/b_1_clean_data/school_demo_hl_merged.csv"
)

# For, analysis: we will first explore correlations
num_schools = 3
merged_df = merged_df[merged_df["count_schools"] >= num_schools]

cols_for_corr = [
    "att_diff_pp",
    "perc_low_income",
    "perc_black_his_stu",
    "bus_count",
    "dolla_per_student",
    "med_age",
    "covid_idx",
    "perc_chg_pop",
    "perc_black_hispanic",
    "perc_pop_lforce",
    "perc_emp",
    "med_inc",
    "inc_p_cap",
    "med_rent",
    "perc_hh_comp",
    "perc_hh_internet",
    "highly_walkable_pop_pct",
    "highly_walkable_emp_pct",
    "low_bw_rate",
    "uninsured_rate",
    "adq_child_care",
    "perc_vacant_units",
    "perc_sing_par_hh",
    "comm_belong_16_18",
    "comm_belong_20_21",
    "perc_hh_stamps",
    "perc_not_getting_stamps",
    "rent_burdened_hh",
    "homicide_rate",
    "drug_induced_dt_rate",
]
#corr_matrix = merged_df[cols_for_corr].corr()
#sns.set(rc = {'figure.figsize': (12,9)})
#sns.heatmap(corr_matrix, cmap="coolwarm", annot=True, annot_kws = {"size": 6})
#plt.savefig("correlation_heatmap.png")
#corr_matrix.to_csv("correlation_table.csv")

# After creating correlation matrix, check if there is a linear relationship using scatterplots
dep_var = "att_diff_pp"
independent_vars = [
    "perc_low_income",
    "perc_black_his_stu",
    "bus_count",
    "dolla_per_student"
    ]
#for variable in independent_vars:
    #plt.clf()
    #sns.scatterplot(x = merged_df[variable], y= merged_df[dep_var])
    #plt.savefig("scatterplot"+"{}".format(variable)+"_heatmap_.jpg")

#Running multi-linear regresssion now
y = merged_df[dep_var]
x = merged_df[independent_vars]
x = sm.add_constant(x)
model = sm.OLS(y,x).fit()
print(model.summary())

new_lst = ["perc_low_income",
    "perc_black_his_stu",
    "bus_count",
    "dolla_per_student",
    "med_age",
    "covid_idx",
    "perc_chg_pop",
    "perc_black_hispanic",
    "perc_pop_lforce",
    "perc_emp",
    "med_inc",
    "inc_p_cap",
    "med_rent",
    "perc_hh_comp",
    "perc_hh_internet",
    "highly_walkable_pop_pct",
    "highly_walkable_emp_pct",
    "low_bw_rate",
    "uninsured_rate",
    "adq_child_care",
    "perc_vacant_units",
    "perc_sing_par_hh",
    "comm_belong_16_18",
    "comm_belong_20_21",
    "perc_hh_stamps",
    "perc_not_getting_stamps",
    "rent_burdened_hh",
    "homicide_rate",
    "drug_induced_dt_rate"]
