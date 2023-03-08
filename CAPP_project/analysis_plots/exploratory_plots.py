"""
Eshan wrote this file, defunct file: not utilised in final output
"""

import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt


school_demo_merge = pd.read_csv("CAPP_project/data_wrangling/merged_data/school_demo_merged.csv")
teach_mob = pd.read_csv("CAPP_project/data_wrangling/merged_data/exp_teach_mob.csv")


#Create a correlation heatmap of attendance and demo_variables

num_schools = 3
school_demo_merge = school_demo_merge[school_demo_merge["count_schools"] >= num_schools]

cols_for_corr = ["pre_cov_att",
"post_cov_att",
"att_diff_pp",
"perc_black_hispanic",
"perc_pop_lforce,
"perc_emp",
"med_inc",
"inc_p_cap",
"med_rent",
"perc_hh_comp",
"perc_hh_internet",
]
corr_matrix = school_demo_merge[school_demo_merge].corr()
sns.set(rc = {'figure.figsize': (12,9)})
sns.heatmap(corr_matrix, cmap="coolwarm", annot=True, annot_kws = {"size": 6})
plt.savefig("correlation_heatmap.png")

#create a scatterplot with trendline

scatter = px.scatter(
    teach_mob,
    x="teachers_per_100_stu",
    y="Student Attendance Rate",
    hover_data=["salary_per_teach", "help_per_100_stu"],
)

avg_x = teach_mob["teachers_per_100_stu"].mean()
avg_y = teach_mob["Student Attendance Rate"].mean()

scatter.add_shape(
    type="line",
    x0=avg_x,
    y0=min(teach_mob["teachers_per_100_stu"]),
    x1=avg_x,
    y1=max(teach_mob["teachers_per_100_stu"]),
    line=dict(color="red", width=1),
)

scatter.add_shape(
    type="line",
    x0=min(teach_mob["Student Attendance Rate"]),
    y0=avg_y,
    x1=max(teach_mob["Student Attendance Rate"]),
    y1=avg_y,
    line=dict(color="red", width=1),
)