import dash
import dash_html_components as html
import dash_core_components as dcc
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from analysis_plots.plots import plot_crime, scatter_OSS_attendance

app = dash.Dash()
# VERY INITIAL STAGE USER INTERFACE


app.layout = html.Div(
    id="parent",
    children=[
        # INCLUDE DROP DOWN OPTIONS HERE
        html.H1(
            id="H1",
            children="School Attendance in Crime-Varying Areas",
            style={"textAlign": "center", "marginTop": 40, "marginBottom": 40},
        ),
        dcc.Graph(id="line_plot", figure=plot_crime()),
        html.H2(
            id="H2",
            children="Out of School Suspension and Attendance",
            style={"textAlign": "center", "marginTop": 40, "marginBottom": 40},
        ),
        dcc.Graph(id="line_plot", figure=scatter_OSS_attendance()),
    ],
)

if __name__ == "__main__":
    app.run_server(port=6001)
