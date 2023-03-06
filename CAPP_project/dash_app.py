"""
Amari wrote this file.
"""
import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from CAPP_project.analysis_plots.plots import(
    plot_crime,
    scatter_SSrate_attendance,
    scatter_ISS_attendance,
    bar_crime_OSS_ISS,
    bar_police_crime,
    scatter_pre_post_grid,
    scatter_income_pre_post,
    bar_att_diff_buckets,
    bar_finance_buckets,
    intro_attendance,
    intro_two,
)
from CAPP_project.analysis_plots.Graph_Descriptions.analysis_desc_dict import (
     descriptions,
 )
 
def blank_figure():  # necessary to avoid displaying default blank graph when no dropdown option is selected
    blank = go.Figure(
        go.Scatter(x=[], y=[])
    )  # https://stackoverflow.com/questions/66637861/how-to-not-show-default-dcc-graph-template-in-dash
    blank.update_layout(template=None)
    blank.update_xaxes(showgrid=False, showticklabels=False, zeroline=False)
    blank.update_yaxes(showgrid=False, showticklabels=False, zeroline=False)
    return blank


style_dict = {
    "border-style": "none",
    "width": "85%",
    "height": 185,
    "margin-left": 75,
    "margin-right": 75,
    "textAlign": "center",
    "font-size": "16px",
}
graph_margins = {
    "margin-left": 75,
    "margin-right": 75,
}


app = dash.Dash()
app.config.suppress_callback_exceptions = True


app.layout = html.Div(
    id="parent",
    children=[
        html.H1(
            id="H1",
            children="Panic at the Schools",
            style={"textAlign": "center", "marginTop": 40, "marginBottom": 40},
        ),
        html.H2(
            id="H2",
            children="Data Collection and Analysis Completed by Eshan, Sarah, and Amari",
            style={"textAlign": "center"},
        ),
        html.H3(
            id="H3",
            children="With support from Professor Turk, our wonderful TA's, and classmates",
            style={"textAlign": "center"},
        ),
        dcc.Dropdown(
            id="dropdown",
            options=[
                {"label": "Introduction", "value": "Introduction"},
                {"label": "Misconduct", "value": "Misconduct"},
                {
                    "label": "Impact of COVID-19 in Schools",
                    "value": "Impact of COVID-19 in Schools",
                },
                {"label": "Conclusion", "value": "Conclusion"},
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
                    "textAlign": "center",
                    "width": "85%",
                    "marginTop": 50,
                    "height": 300,
                    "border-style": "none",
                    "margin-left": 105,
                    "margin-right": 75,
                    "font-size": "16px",
                },
            )
        ),
        html.Div(
            dcc.Graph(id="fig", figure=blank_figure()),
            style=graph_margins,
        ),
        html.Div(
            dcc.Textarea(
                id="desc1",
                readOnly=True,
                style=style_dict,
            ),
            style={"textAlign": "center"},
        ),
        html.Div(
            dcc.Graph(
                id="fig2",
                figure=blank_figure(),
            ),
            style=graph_margins,
        ),
        html.Div(
            dcc.Textarea(id="desc2", readOnly=True, style=style_dict),
            style={"textAlign": "center"},
        ),
        html.Div(
            dcc.Graph(id="fig3", figure=blank_figure()),
            style=graph_margins,
        ),
        html.Div(
            dcc.Textarea(
                id="desc3",
                readOnly=True,
                style=style_dict,
            ),
            style={"textAlign": "center"},
        ),
        html.Div(
            dcc.Graph(id="fig4", figure=blank_figure()),
            style=graph_margins,
        ),
        html.Div(
            dcc.Textarea(
                id="desc4",
                readOnly=True,
                style=style_dict,
            ),
            style={"textAlign": "center"},
        ),
    ],
)


@app.callback(
    [
        Output(component_id="fig", component_property="figure"),
        Output(component_id="desc1", component_property="value"),
        Output(component_id="fig2", component_property="figure"),
        Output(component_id="desc2", component_property="value"),
        Output(component_id="fig3", component_property="figure"),
        Output(component_id="desc3", component_property="value"),
        Output(component_id="fig4", component_property="figure"),
        Output(component_id="desc4", component_property="value"),
    ],
    [Input(component_id="dropdown", component_property="value")],
)
def display_plots(value):
    if value == "Conclusion":
        fig = blank_figure()
        fig_desc = descriptions["conclusion"]
        fig2 = blank_figure()
        fig2_desc = ""
        fig3 = blank_figure()
        fig3_desc = ""
        fig4 = blank_figure()
        fig4_desc = ""
        return [fig, fig_desc, fig2, fig2_desc, fig3, fig3_desc, fig4, fig4_desc]

    if value == "Misconduct":
        fig = plot_crime()
        fig_desc = descriptions["crime"]
        fig2 = scatter_SSrate_attendance()
        fig2_desc = descriptions["attend"]
        fig3 = bar_crime_OSS_ISS()
        fig3_desc = descriptions["ISS and OSS"]
        fig4 = bar_police_crime()
        fig4_desc = descriptions["police"]
        return [fig, fig_desc, fig2, fig2_desc, fig3, fig3_desc, fig4, fig4_desc]

    if value == "Impact of COVID-19 in Schools":
        fig = scatter_pre_post_grid()
        fig_desc = descriptions["pre_post grid"]
        fig2 = scatter_income_pre_post()
        fig2_desc = descriptions["income"]
        fig3 = bar_att_diff_buckets()
        fig3_desc = descriptions["change"]
        fig4 = bar_finance_buckets()
        fig4_desc = descriptions["finance"]
        return [fig, fig_desc, fig2, fig2_desc, fig3, fig3_desc, fig4, fig4_desc]

    else:  # display intro
        fig = intro_attendance()
        fig_desc = descriptions["somebody"]
        fig2 = intro_two()
        fig2_desc = descriptions["somebody"]
        fig3 = blank_figure()
        fig3_desc = ""
        fig4 = blank_figure()
        fig4_desc = ""
        return [fig, fig_desc, fig2, fig2_desc, fig3, fig3_desc, fig4, fig4_desc]


if __name__ == "__main__":
    app.run_server(port=6093)