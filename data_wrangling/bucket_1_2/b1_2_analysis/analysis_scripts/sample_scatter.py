import pandas as pd
import plotly.express as px
import dash
from dash import dcc, html 
from dash.dependencies import Input, Output

att_matrix = pd.read_csv(
    "/home/eshanprashar/PanicAtTheSchool/data_wrangling/bucket_1_2/b1_2_analysis/final_clean_data/pre_vs_post_att.csv"
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

app = dash.Dash(__name__)
app.layout = html.Div([dcc.Graph(id="scatterplot", figure=scatter)])

if __name__ == "__main__":
    app.run_server(debug=True)