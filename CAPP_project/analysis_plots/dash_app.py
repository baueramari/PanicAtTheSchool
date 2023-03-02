import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from analysis_plots.plots import (
    plot_crime,
    scatter_OSS_attendance,
    scatter_SSrate_attendance,
    scatter_ISS_attendance,
    bar_crime_OSS_ISS,
    bar_police_crime,
    scatter_pre_post_grid,
)


def blank_figure():  # necessary to avoid displaying default blank graph when no dropdown option is selected
    blank = go.Figure(
        go.Scatter(x=[], y=[])
    )  # https://stackoverflow.com/questions/66637861/how-to-not-show-default-dcc-graph-template-in-dash
    blank.update_layout(template=None)
    blank.update_xaxes(showgrid=False, showticklabels=False, zeroline=False)
    blank.update_yaxes(showgrid=False, showticklabels=False, zeroline=False)
    return blank


app = dash.Dash()
app.config.suppress_callback_exceptions = True


# VERY INITIAL STAGE


app.layout = html.Div(
    id="parent",
    children=[
        html.H1(
            id="H1",
            children="Panic at the Schools",
            style={"textAlign": "center", "marginTop": 40, "marginBottom": 40},
        ),
        html.H2(id="H2", children="Eshan, Sarah, and Amari!"),
        dcc.Dropdown(
            id="dropdown",
            options=[
                {"label": "Misconduct", "value": "Misconduct"},
                {"label": "Demographic", "value": "Demographic"},  # at home factors?
                {"label": "Health", "value": "Health"},  # at school factors?
            ],
            value="project_intro",
        ),
        html.Div(
            dcc.Textarea(
                id="intro",
                value="""CAPP 30122 Group Project: Sarah, Eshan, and Amari

    TLDR: We have moved away from looking into enrollment and learning gains, and now are focusing only at attendance drops. Our goal is to investigate reasons for drops (read below) and visualize our findings on a web app.

    Our aim is to assess the drop in attendance observed by Chicago Public Schools in the last decade, but more specifically, in the time returning from COVID. Based on attendance data from CPS, pre-K and grades 9-12 have shown the most noticeable drop in attendance. For these grades, in 2018 and 2019, for example, the average attendance was 86.15% and 86.51% respectively. Post Covid, these numbers dropped to 79.72% and 78.79% respectively in 2021 and 2022. News agencies covering this issue have attributed these trends to the emergence and solidification of the Chicago Teachers Union. While we’re not looking into those claims through this project, we want to investigate other variables that might have impacted attendance. Specifically, we want to look at 3 buckets: a) Neighborhood indicators: These will cover: Demographic build up of school neighborhood Socioeconomic indicators - employment, income etc. Health indicators Accessibility indicators such as walkability score, access to public transport etc.
    b) Investment in school indicators: These will cover: Per pupil budget for schools Teacher distribution by race/qualification Attendance distribution by school type c) Crime and punishment indicators: Crime in the school neighborhood Suspensions/expulsions handed out by school authorities Through our analysis, we want to see which of these factors impacts attendance the most. Finally, we will visualize our results on a web-app and write down some potential next steps based on research of news articles/interviews with CPS employees.')""",
                style={
                    "width": "100%",
                    "height": 200,
                },
            )
        ),
        html.Div(dcc.Graph(id="fig", figure=blank_figure())),
        html.Div(dcc.Graph(id="fig2", figure=blank_figure())),
        html.Div(dcc.Graph(id="fig3", figure=blank_figure())),
        html.Div(dcc.Graph(id="fig4", figure=blank_figure())),
        html.Div(dcc.Graph(id="fig5", figure=blank_figure())),
        html.Div(dcc.Graph(id="fig6", figure=blank_figure())),
        # html.Div(dcc.Graph(id="prepost", figure=blank_figure())),
    ],
)


# @app.callback(
#    Output(component_id="intro", component_property="children"),
#    [Input(component_id="dropdown", component_property="value")],
# )
# def project_intro(value):
#    if value == "Project Introduction":
#        text = dcc.Textarea(
#            id="intro",
#            value="""CAPP 30122 Group Project: Sarah, Eshan, and Amari
#
#    TLDR: We have moved away from looking into enrollment and learning gains, and now are focusing only at attendance drops. Our goal is to investigate reasons for drops (read below) and visualize our findings on a web app.
#
#    Our aim is to assess the drop in attendance observed by Chicago Public Schools in the last decade, but more specifically, in the time returning from COVID. Based on attendance data from CPS, pre-K and grades 9-12 have shown the most noticeable drop in attendance. For these grades, in 2018 and 2019, for example, the average attendance was 86.15% and 86.51% respectively. Post Covid, these numbers dropped to 79.72% and 78.79% respectively in 2021 and 2022. News agencies covering this issue have attributed these trends to the emergence and solidification of the Chicago Teachers Union. While we’re not looking into those claims through this project, we want to investigate other variables that might have impacted attendance. Specifically, we want to look at 3 buckets: a) Neighborhood indicators: These will cover: Demographic build up of school neighborhood Socioeconomic indicators - employment, income etc. Health indicators Accessibility indicators such as walkability score, access to public transport etc.
#    b) Investment in school indicators: These will cover: Per pupil budget for schools Teacher distribution by race/qualification Attendance distribution by school type c) Crime and punishment indicators: Crime in the school neighborhood Suspensions/expulsions handed out by school authorities Through our analysis, we want to see which of these factors impacts attendance the most. Finally, we will visualize our results on a web-app and write down some potential next steps based on research of news articles/interviews with CPS employees.')""",
#            style={
#                "width": "100%",
#                "height": 200,
#            },
#        )
#        return [text]


@app.callback(
    [
        Output(component_id="fig", component_property="figure"),
        # Output(component_id="bacon", component_property="figure"),
        Output(component_id="fig2", component_property="figure"),
        Output(component_id="fig3", component_property="figure"),
        Output(component_id="fig4", component_property="figure"),
        Output(component_id="fig5", component_property="figure"),
        Output(component_id="fig6", component_property="figure"),
    ],
    [Input(component_id="dropdown", component_property="value")],
)
def display_plots(value):
    if value == "Misconduct":
        fig = plot_crime()
        # fig12 = "bacon"
        fig2 = scatter_SSrate_attendance()
        fig3 = scatter_OSS_attendance()
        fig4 = scatter_ISS_attendance()
        fig5 = bar_crime_OSS_ISS()
        fig6 = bar_police_crime()
        return [fig, fig2, fig3, fig4, fig5, fig6]
    if value == "Health":
        fig = scatter_pre_post_grid()
        fig2 = blank_figure()  # insert  other health related ones here
        fig3 = blank_figure()
        fig4 = blank_figure()
        fig5 = blank_figure()
        fig6 = blank_figure()

        return [fig, fig2, fig3, fig4, fig5, fig6]
    # add last option in here


# NEED TO FIGURE OUT HOW TO ADD TEXT DESCRIPTION IN HERE, WRITE THEM IN ANOTHER FILE AND LOAD THEM IN?
if __name__ == "__main__":
    app.run_server(port=6096)
