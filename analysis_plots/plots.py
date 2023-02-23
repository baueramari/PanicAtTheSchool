# CODE TO GENERATE PLOTS
import pandas as pd
import plotly.express as px


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


#Sarah's plots for suspension data
def scatter_OSS_attendance():
    avg_SS_attend = pd.read_csv("data_wrangling/cleaned_data/suspension_attendance.csv")
    OSS_attend_scatter = px.scatter(avg_SS_attend, x = '% of Unique Students Receiving OSS', y= "Attendance")
    
    #scatter.show()
    return OSS_attend_scatter

def scatter_ISS_attendance():
    avg_SS_attend = pd.read_csv("data_wrangling/cleaned_data/suspension_attendance.csv")
    ISS_attend_scatter = px.scatter(avg_SS_attend, x = '% of Unique Students Receiving ISS', y= "Attendance")
    
    return ISS_attend_scatter

def scatter_SSrate_attendance():
    avg_SS_attend = pd.read_csv("data_wrangling/cleaned_data/suspension_attendance.csv")
    SSrate_attend_scatter = px.scatter(avg_SS_attend, x = '% of Misconducts Resulting in a Suspension\n(includes ISS and OSS)', y= "Attendance")
    
    return SSrate_attend_scatter


#will want to imagine this in a deifferent way, but it's a start
def bar_SSrate_OSS_ISS():
    avg_SS_crime = pd.read_csv("data_wrangling/cleaned_data/suspension_crime.csv")
    fig = px.bar(avg_SS_crime, x="crime_class", y='% of Misconducts Resulting in a Suspension\n(includes ISS and OSS)', color = '% of Unique Students Receiving ISS')
    fig.show()


#will want to modify the y-axis range so it doesn't look as dramatic
def line_police_crime():
    avg_SS_crime = pd.read_csv("data_wrangling/cleaned_data/suspension_crime.csv")

    order = ["Low", "Medium", "High"]
    avg_SS_crime = avg_SS_crime.sort_values("crime_class")
    avg_SS_crime["crime_class"] = pd.Categorical(
        avg_SS_crime["crime_class"], categories=order
    )

    line_police_crime = px.line(
        avg_SS_crime,
        x="crime_class",
        y="% of Misconducts Resulting in a Police Notification",
    )

    line_police_crime.show()