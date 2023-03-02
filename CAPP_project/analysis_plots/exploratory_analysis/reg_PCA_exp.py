# In this file, I will rearrange merged file columns, and run:
# 1. Make scatterplots, look at correlation coefficients -- Done
# 2. Run regression on reduced column space -- Done
# This file should tell me what variables should be plotted while analysing attendance

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import statsmodels.api as sm

merged_df = pd.read_csv(
    "/home/eshanprashar/PanicAtTheSchool/data_wrangling/merged_data/all_school_merged.csv"
)

# For, analysis: we will first explore correlations
#num_schools = 3
#merged_df = merged_df[merged_df["count_schools"] >= num_schools]

cols_for_corr = [
    "perc_low_income","perc_black_his_stu","pre_cov_att","post_cov_att","teachers_per_100stu","help_fte_per_100stu","dolla_per_student","salary_per_teacher"
]
corr_matrix = merged_df[cols_for_corr].corr()
sns.set(rc = {'figure.figsize': (12,9)})
sns.heatmap(corr_matrix, cmap="coolwarm", annot=True, annot_kws = {"size": 6})
plt.savefig("correlation_heatmap.png")
corr_matrix.to_csv("correlation_table.csv")