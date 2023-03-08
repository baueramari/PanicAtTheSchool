"""
Eshan wrote this file, plots generated not used in final output
"""

import pandas as pd
import plotly.express as px
import dash
from dash import dcc, html 
from dash.dependencies import Input, Output

#filepath needs to be validated

att_matrix = pd.read_csv(
    "CAPP_project/data_wrangling/merged_data/all_school_merged.csv"
)
# create a scatterplot with trendline
scatter = px.scatter(
    att_matrix,
    x="pre_cov_att",
    y="post_cov_att",
    hover_data=["pre_att_bucket", "post_att_bucket"],
)

avg_x = att_matrix["pre_cov_att"].mean()
avg_y = att_matrix["post_cov_att"].mean()

scatter.add_shape(
    type="line",
    x0=avg_x,
    y0=min(att_matrix["pre_cov_att"]),
    x1=avg_x,
    y1=max(att_matrix["pre_cov_att"]),
    line=dict(color="red", width=1),
)

scatter.add_shape(
    type="line",
    x0=min(att_matrix["post_cov_att"]),
    y0=avg_y,
    x1=max(att_matrix["post_cov_att"]),
    y1=avg_y,
    line=dict(color="red", width=1),
)

# create a list of options for the dropdown
dropdown_options = [
    {"label": "pre_cov_att", "value": "pre_cov_att"},
    {"label": "post_cov_att", "value": "post_cov_att"},
]

# create the layout for the app
app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Dropdown(
        id='x-axis-dropdown',
        options=dropdown_options,
        value='pre_cov_att'  # default value
    ),
    dcc.Graph(id="scatterplot", figure=scatter)
])

# create a callback to update the x-axis of the scatter plot
@app.callback(
    dash.dependencies.Output('scatterplot', 'figure'),
    [dash.dependencies.Input('x-axis-dropdown', 'value')]
)
def update_figure(x_axis):
    fig = px.scatter(
        att_matrix,
        x=x_axis,
        y="post_cov_att",
        hover_data=["pre_att_bucket", "post_att_bucket"],
    )

    fig.add_shape(
        type="line",
        x0=att_matrix[x_axis].mean(),
        y0=min(att_matrix[x_axis]),
        x1=att_matrix[x_axis].mean(),
        y1=max(att_matrix[x_axis]),
        line=dict(color="red", width=1),
    )

    fig.add_shape(
        type="line",
        x0=min(att_matrix["post_cov_att"]),
        y0=att_matrix["post_cov_att"].mean(),
        x1=max(att_matrix["post_cov_att"]),
        y1=att_matrix["post_cov_att"].mean(),
        line=dict(color="red", width=1),
    )

    return fig

if __name__ == "__main__":
    app.run_server(debug=True, port = 8051)



####
#import pandas as pd
#import seaborn as sns
#import matplotlib.pyplot as plt
#import numpy as np
#import statsmodels.api as sm

#merged_df = pd.read_csv(
#    "/home/eshanprashar/PanicAtTheSchool/data_wrangling/merged_data/all_school_merged.csv"
#)

# For, analysis: we will first explore correlations
#num_schools = 3
#merged_df = merged_df[merged_df["count_schools"] >= num_schools]

#cols_for_corr = [
#    "perc_low_income","perc_black_his_stu","pre_cov_att","post_cov_att","teachers_per_100stu","help_fte_per_100stu","dolla_per_student","salary_per_teacher"
#]
#corr_matrix = merged_df[cols_for_corr].corr()
#sns.set(rc = {'figure.figsize': (12,9)})
#sns.heatmap(corr_matrix, cmap="coolwarm", annot=True, annot_kws = {"size": 6})
#plt.savefig("correlation_heatmap.png")
#corr_matrix.to_csv("correlation_table.csv")