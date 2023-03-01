# CODE TO GENERATE PLOTS
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

#update where the data files are coming from and the names of the files 
def plot_crime():
    attend_by_crime = pd.read_csv("data_wrangling/cleaned_data/attend_by_crime.csv")
    order = ["High", "Medium", "Low"]
    attend_by_crime["crime_class"] = pd.Categorical(
        attend_by_crime["crime_class"], categories=order
    )
    attend_by_crime = attend_by_crime.sort_values(["crime_class", "Year"])
    plot_axes = {
        "xaxis_title": "School Year",
        "yaxis_title": "Attendance (% Students at School)",
        "legend_title": "Legend",
    }
    crime_attend = px.line(
        attend_by_crime,
        x="Year",
        y="Attendance",
        color="crime_class",
        title="School Attendance by Crime Level",
        markers=True,
        line_shape="spline",
    )
    crime_attend.update_layout(
        plot_axes,
    )
    crime_attend.update_xaxes(tick0=2013, dtick=1)
    return crime_attend


# Sarah's plots for suspension data
def scatter_OSS_attendance():
    avg_SS_attend = pd.read_csv("data_wrangling/cleaned_data/suspension_attendance.csv")
    OSS_attend_scatter = px.scatter(
        avg_SS_attend,
        x="% of Unique Students Receiving OSS",
        y="Attendance",
        labels={
            "Attendance": "Average Attendance Rate",
        },
        title="School's Average Attendance Rate by Percent of Unique Students Receiving Out of School Suspension",
    )

    # scatter.show()
    return OSS_attend_scatter


def scatter_ISS_attendance():
    avg_SS_attend = pd.read_csv("data_wrangling/cleaned_data/suspension_attendance.csv")
    ISS_attend_scatter = px.scatter(
        avg_SS_attend,
        x="% of Unique Students Receiving ISS",
        y="Attendance",
        labels={
            "Attendance": "Average Attendance Rate",
        },
        title="School's Average Attendance Rate by Percent of Unique Students Receiving In School Suspension",
    )

    return ISS_attend_scatter


def scatter_SSrate_attendance():
    avg_SS_attend = pd.read_csv("data_wrangling/cleaned_data/suspension_attendance.csv")
    SSrate_attend_scatter = px.scatter(
        avg_SS_attend,
        x="% of Misconducts Resulting in a Suspension\n(includes ISS and OSS)",
        y="Attendance",
        labels={
            "Attendance": "Average Attendance Rate",
        },
        title="School's Average Attendance Rate by Percent of Misconducts Resulting in a Suspension",
    )

    return SSrate_attend_scatter


# Still need to fix this
def bar_crime_OSS_ISS():
    avg_SS_crime = pd.read_csv("data_wrangling/cleaned_data/suspension_crime.csv")
    order = ["High", "Medium", "Low"]
    avg_SS_crime["crime_class"] = pd.Categorical(
        avg_SS_crime["crime_class"], categories=order
    )
    avg_SS_crime = avg_SS_crime.sort_values("crime_class")

    fig_ISS = px.bar(avg_SS_crime, x="crime_class", y="% of Unique Students Receiving ISS")
    fig_OSS = px.bar(avg_SS_crime, x="crime_class", y="% of Unique Students Receiving OSS")


    # avg_SS_crime = pd.read_csv("data_wrangling/cleaned_data/suspension_crime.csv")
    # fig = go.Figure(go.Bar(x="crime_class", y="% of Unique Students Receiving OSS"))
    # fig.add_trace(go.Bar(x="crime_class", y="% of Unique Students Receiving ISS"))
    # fig.update_layout(barmode="stack")

    
    #fig_OSS.show()
    fig_ISS.show()


def bar_police_crime():
    avg_SS_crime = pd.read_csv("data_wrangling/cleaned_data/suspension_crime.csv")

    order = ["High", "Medium", "Low"]
    avg_SS_crime["crime_class"] = pd.Categorical(
        avg_SS_crime["crime_class"], categories=order
    )
    avg_SS_crime = avg_SS_crime.sort_values("crime_class")

    bar_police_crime = px.bar(
        avg_SS_crime,
        x="crime_class",
        y="% of Misconducts Resulting in a Police Notification",
        labels={
            "crime_class": "Crime Class",
        },
        title="School's Percent of Misconducts Resulting in a Police Notification by Crime Class",
    )
    bar_police_crime.update_layout(yaxis_range=[0, 10])

    return bar_police_crime


##Eshan's non-function scatter code -- needs to be restrutured
import pandas as pd
import plotly.express as px
import dash
from dash import dcc, html
from dash.dependencies import Input, Output

# att_matrix = pd.read_csv(
#    "/home/eshanprashar/PanicAtTheSchool/data_wrangling/bucket_1_2/b1_2_analysis/final_clean_data/pre_vs_post_att.csv"
# )
## create a scatterplot with trendline
# scatter = px.scatter(
#    att_matrix,
#    x="pre_cov_att",
#    y="post_cov_att",
#    hover_data=["pre_att_bucket", "post_att_bucket"],
# )
# avg_x = att_matrix["pre_cov_att"].mean()
# avg_y = att_matrix["post_cov_att"].mean()
# scatter.add_shape(
#    type="line",
#    x0=avg_x,
#    y0=min(att_matrix["pre_cov_att"]),
#    x1=avg_x,
#    y1=max(att_matrix["pre_cov_att"]),
#    line=dict(color="red", width=1),
# )
# scatter.add_shape(
#    type="line",
#    x0=min(att_matrix["post_cov_att"]),
#    y0=avg_y,
#    x1=max(att_matrix["post_cov_att"]),
#    y1=avg_y,
#    line=dict(color="red", width=1),
# )
#
### This part is not needed- will go in dash.py file
# app = dash.Dash(__name__)
# app.layout = html.Div([dcc.Graph(id="scatterplot", figure=scatter)])

if __name__ == "__main__":
    app.run_server(debug=True)
###
