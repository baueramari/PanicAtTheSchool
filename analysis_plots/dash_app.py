import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from analysis_plots.plots import plot_crime, scatter_OSS_attendance

app = dash.Dash()
# VERY INITIAL STAGE

app.layout = html.Div(
    id="parent",
    children=[
        html.H1(
            id="H1",
            children="Panic at the Schools",
            style={"textAlign": "center", "marginTop": 40, "marginBottom": 40},
        ),
        dcc.Dropdown(
            id="dropdown",
            options=[
                {"label": "Project Introduction", "value": "Project Introduction"},
                {"label": "Misconduct", "value": "Misconduct"},
                {"label": "Demographic", "value": "Demographic"},  # at home factors
                {"label": "Health", "value": "Health"},  # at school factors
            ],
            value="project_intro",
        ),
        html.Div(dcc.Textarea(id="Text Area", value={})),
    ],
)


@app.callback(
    Output(component_id="Text Area", component_property="value"),
    [Input(component_id="dropdown", component_property="value")],
)
def project_intro(dropdown):
    if dropdown == "Project Introduction":
        text = dcc.Textarea(
            id="Text Area",
            value="""CAPP 30122 Group Project: Sarah, Eshan, and Amari

    TLDR: We have moved away from looking into enrollment and learning gains, and now are focusing only at attendance drops. Our goal is to investigate reasons for drops (read below) and visualize our findings on a web app.

    Our aim is to assess the drop in attendance observed by Chicago Public Schools in the last decade, but more specifically, in the time returning from COVID. Based on attendance data from CPS, pre-K and grades 9-12 have shown the most noticeable drop in attendance. For these grades, in 2018 and 2019, for example, the average attendance was 86.15% and 86.51% respectively. Post Covid, these numbers dropped to 79.72% and 78.79% respectively in 2021 and 2022. News agencies covering this issue have attributed these trends to the emergence and solidification of the Chicago Teachers Union. While we’re not looking into those claims through this project, we want to investigate other variables that might have impacted attendance. Specifically, we want to look at 3 buckets: a) Neighborhood indicators: These will cover: Demographic build up of school neighborhood Socioeconomic indicators - employment, income etc. Health indicators Accessibility indicators such as walkability score, access to public transport etc.
    b) Investment in school indicators: These will cover: Per pupil budget for schools Teacher distribution by race/qualification Attendance distribution by school type c) Crime and punishment indicators: Crime in the school neighborhood Suspensions/expulsions handed out by school authorities Through our analysis, we want to see which of these factors impacts attendance the most. Finally, we will visualize our results on a web-app and write down some potential next steps based on research of news articles/interviews with CPS employees.')""",
            style={
                "width": "100%",
                "height": 200,
            },
        )
        return text


"""
@app.callback(
    Output(component_id="plot", component_property="figure"),
    [Input(component_id="dropdown", component_property="value")],
)
def display_plots(dropdown):
    plot_dict = {
        "Misconduct": [
            plot_crime,  # eventually turn this into a dictionary of dictionaries, with the text analysis written in as the values
            scatter_OSS_attendance,
        ],  # list of our plotting functions for each dropdown
        "Demographic": [],
        "Health": [],
    }
    figures = []
    for graphing_f in plot_dict[dropdown]:
        figures.append(html.Div(dcc.Graph(id="plot", figure=graphing_f())))
    # text = dcc.Textarea(id="Text Area", value="INSERT CRIME PLOT ANALYSIS")
    # dcc.Graph(id="line_plot", figure=scatter_OSS_attendance())
    # dcc.Textarea(id="Text Area", value="INSERT SUSPENSION PLOT ANALYSIS")
    return figures
"""

if __name__ == "__main__":
    app.run_server(port=6036)
