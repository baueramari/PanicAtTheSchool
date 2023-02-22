# In this file, I will rearrange merged file columns, and run:
# 1.
# 2. Run regression on reduced column space
# 3. Backlog: Try to run PCA to, reduce matrix size and then run regression
# This file should tell me what variables should be plotted while analysing attendance

import pandas as pd
from sklearn.preprocessing import StandardScaler
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

merged_df = pd.read_csv(
    "/home/eshanprashar/PanicAtTheSchool/data_wrangling/bucket_1_ep/b_1_clean_data/school_demo_hl_merged.csv"
)

# For, analysis: we will first explore correlations
print(merged_df.columns)
cols_for_corr = ["perc_low_income", "att_diff_pp"]
corr_matrix = merged_df[cols_for_corr].corr()
sns.heatmap(corr_matrix, cmap="coolwarm", annot=True)
plt.savefig("correlation_heatmap.png")
