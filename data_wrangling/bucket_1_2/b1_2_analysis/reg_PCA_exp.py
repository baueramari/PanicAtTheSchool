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
    "/home/eshanprashar/PanicAtTheSchool/data_wrangling/bucket_1_ep/b_1_clean_data/school_demo_merge.csv"
)

# For, analysis: we will first explore correlations
num_schools = 3
merged_df = merged_df[merged_df["count_schools"] >= num_schools]

cols_for_corr = [
    "pre_cov_att",
    "post_cov_att",
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
corr_matrix = merged_df[cols_for_corr].corr()
sns.set(rc = {'figure.figsize': (12,9)})
sns.heatmap(corr_matrix, cmap="coolwarm", annot=True, annot_kws = {"size": 6})
plt.savefig("correlation_heatmap.png")
corr_matrix.to_csv("correlation_table.csv")
corr_threshold = 0.5

highly_correlated = np.where(np.abs(corr_matrix) > corr_threshold)
unique_pairs = set([(corr_matrix.columns[x], corr_matrix.columns[y]) for x, y in zip(*highly_correlated) if x != y])

variables_to_include = list(cols_for_corr)
for pair in unique_pairs:
    var1 = pair[0]
    var2 = pair[1]
    if var1 in variables_to_include and var2 in variables_to_include:
        if abs(corr_matrix.loc[var1, :].sum()) > abs(corr_matrix.loc[var2, :].sum()):
            variables_to_include.remove(var2)
        else:
            variables_to_include.remove(var1)



#print(variables_to_include)
#X = merged_df[variables_to_include]
#y = merged_df["pre_cov_att"]
#model = sm.OLS(y, sm.add_constant(X)).fit()
#print(model.summary())



# After creating correlation matrix, check if there is a linear relationship using scatterplots
#dep_var = "post_cov_att"
#independent_vars = [
#    "pre_cov_att",
#    "dolla_per_student",
#    ]
#for variable in independent_vars:
#    plt.clf()
#    sns.scatterplot(x = merged_df[variable], y= merged_df[dep_var])
#    plt.savefig("scatterplot"+"{}".format(variable)+"_heatmap_.jpg")

#Running multi-linear regresssion now
#y = merged_df[dep_var]
#x = merged_df[independent_vars]
#x = sm.add_constant(x)
#model = sm.OLS(y,x).fit()
#print(model.summary())

#new_lst = ["perc_low_income",
#    "perc_black_his_stu",
#    "bus_count",
#    "dolla_per_student",
#    "med_age",
#    "covid_idx",
#    "perc_chg_pop",
#    "perc_black_hispanic",
#    "perc_pop_lforce",
#    "perc_emp",
#    "med_inc",
#    "inc_p_cap",
#    "med_rent",
#    "perc_hh_comp",
#    "perc_hh_internet",
#    "highly_walkable_pop_pct",
#    "highly_walkable_emp_pct",
#    "low_bw_rate",
#    "uninsured_rate",
#    "adq_child_care",
#    "perc_vacant_units",
#    "perc_sing_par_hh",
#    "comm_belong_16_18",
#    "comm_belong_20_21",
#    "perc_hh_stamps",
#    "perc_not_getting_stamps",
#    "rent_burdened_hh",
#    "homicide_rate",
#    "drug_induced_dt_rate"]
