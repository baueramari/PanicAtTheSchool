# CODE TO GENERATE PLOTS
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Question: do we want to add hovers?
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

    # fig = px.bar(
    #     avg_SS_crime,
    #     x="crime_class",
    #     y="% of Unique Students Receiving ISS",
    #     #color="% of Unique Students Receiving ISS",
    # )
    # fig.add_bar(avg_SS_crime,
    #     x="crime_class", y = "% of Unique Students Receiving OSS")

    # fig.add_trace(y = "% of Unique Students Receiving OSS")
    # fig.layout(yaxis = list(title = "percent"), barmode = "group")
    # fig = go.Figure(go.Bar(x="crime_class", y="% of Unique Students Receiving OSS"))
    # fig.add_trace(go.Bar(x="crime_class", y="% of Unique Students Receiving ISS"))
    # fig.update_layout(barmode='stack')

    # 
    #fig_OSS.show()
    fig_ISS.show()


#     import plotly.graph_objects as go

# x=['b', 'a', 'c', 'd']
# fig = go.Figure(go.Bar(x=x, y=[2,5,1,9], name='Montreal'))
# fig.add_trace(go.Bar(x=x, y=[1, 4, 9, 16], name='Ottawa'))
# fig.add_trace(go.Bar(x=x, y=[6, 8, 4.5, 8], name='Toronto'))

# fig.update_layout(barmode='stack')
# fig.update_xaxes(categoryorder='category ascending')
# fig.show()


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
