"""
Sarah wrote 
Eshan wrote
Amari wrote plot_crime()
This file contains all code to create data visualizations. 
"""
import pandas as pd
import plotly.express as px

# import dash
# from dash import dcc, html
# from dash.dependencies import Input, Output


# Sarah wrote these
# clean introduction data (last minute addition)
def clean_intro():
    attendance_cols = ["Year", "Grade", "Average Attendance"]
    attendance = pd.read_csv(
        "CAPP_project/raw_data/introduction/FIG1.csv", usecols=attendance_cols
    )

    attendance["Grade"] = attendance["Grade"].astype(str)
    attendance["Year"] = attendance["Year"].astype(str)
    attendance["Average Attendance"] = attendance["Average Attendance"].astype(float)

    attendance.to_csv("CAPP_project/data_wrangling/cleaned_data/intro_attendance.csv")


# using on introduction page
def intro_attendance():
    attendance = pd.read_csv(
        "CAPP_project/data_wrangling/cleaned_data/intro_attendance.csv"
    )

    intro_line = px.line(
        attendance,
        x="Year",
        y="Average Attendance",
        color="Grade",
        labels={
            "Average Attendance": "Average Attendance Rate (%)",
        },
        title="School Attendance Over Time by Grade",
        markers=True,
        line_shape="spline",
    )
    intro_line.update_layout(
        title={"y": 0.9, "x": 0.5, "xanchor": "center", "yanchor": "top"}
    )

    return intro_line


# using on introduction page
def intro_two():
    num_schools = {
        "Number of Schools": [649, 152],
        "": ["Total Number of CPS Schools", "Number of CPS High Schools"],
    }

    num_schools_df = pd.DataFrame(num_schools)

    fig = px.bar(
        num_schools_df,
        x="",
        y="Number of Schools",
        title="Only 23% of CPS Schools are High Schools",
    )

    fig.update_layout(title={"y": 0.9, "x": 0.5, "xanchor": "center", "yanchor": "top"})
    return fig


# using this on the misconduct page
def plot_crime():
    attend_by_crime = pd.read_csv(
        "CAPP_project/data_wrangling/merged_data/attend_by_crime.csv"
    )
    order = ["High", "Medium", "Low"]
    attend_by_crime["crime_class"] = pd.Categorical(
        attend_by_crime["crime_class"], categories=order
    )
    attend_by_crime = attend_by_crime.sort_values(["crime_class", "Year"])
    plot_axes = {
        "xaxis_title": "School Year",
        "yaxis_title": "Attendance (% Students at School)",
        "legend_title": "Crime Tercile",
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


# Sarah wrote these
# using this on the misconduct page
def scatter_SSrate_attendance():
    avg_SS_attend = pd.read_csv(
        "CAPP_project/data_wrangling/merged_data/suspension_attendance.csv"
    )
    SSrate_attend_scatter = px.scatter(
        avg_SS_attend,
        x="% of Misconducts Resulting in a Suspension\n(includes ISS and OSS)",
        y="Attendance",
        labels={
            "Attendance": "Average Attendance Rate",
            "% of Misconducts Resulting in a Suspension\n(includes ISS and OSS)": "% of Misconducts Resulting in a Suspension (includes In School and Out of School Suspension)",
        },
        title="Average Attendance Rate by Percent of Misconducts Resulting in a Suspension",
    )

    SSrate_attend_scatter.update_layout(
        title={"y": 0.9, "x": 0.5, "xanchor": "center", "yanchor": "top"}
    )

    return SSrate_attend_scatter


# not using this
def scatter_OSS_attendance():
    avg_SS_attend = pd.read_csv(
        "CAPP_project/data_wrangling/merged_data/suspension_attendance.csv"
    )
    OSS_attend_scatter = px.scatter(
        avg_SS_attend,
        x="% of Unique Students Receiving OSS",
        y="Attendance",
        labels={
            "Attendance": "Average Attendance Rate",
        },
        title="Average Attendance Rate by Percent of Unique Students Receiving Out of School Suspension",
    )

    return OSS_attend_scatter


# not using this
def scatter_ISS_attendance():
    avg_SS_attend = pd.read_csv(
        "CAPP_project/data_wrangling/merged_data/suspension_attendance.csv"
    )
    ISS_attend_scatter = px.scatter(
        avg_SS_attend,
        x="% of Unique Students Receiving ISS",
        y="Attendance",
        labels={
            "Attendance": "Average Attendance Rate",
        },
        title="Average Attendance Rate by Percent of Unique Students Receiving In School Suspension",
    )

    return ISS_attend_scatter


# using this on misconducts page
def bar_crime_OSS_ISS():
    avg_SS_crime = pd.read_csv(
        "CAPP_project/data_wrangling/merged_data/avg_suspension_crime.csv"
    )

    High_ISS = avg_SS_crime.groupby(["crime_class"])[
        "% of Unique Students Receiving ISS"
    ].mean()["High"]
    Medium_ISS = avg_SS_crime.groupby(["crime_class"])[
        "% of Unique Students Receiving ISS"
    ].mean()["Medium"]
    Low_ISS = avg_SS_crime.groupby(["crime_class"])[
        "% of Unique Students Receiving ISS"
    ].mean()["Medium"]

    High_OSS = avg_SS_crime.groupby(["crime_class"])[
        "% of Unique Students Receiving OSS"
    ].mean()["High"]
    Medium_OSS = avg_SS_crime.groupby(["crime_class"])[
        "% of Unique Students Receiving OSS"
    ].mean()["Medium"]
    Low_OSS = avg_SS_crime.groupby(["crime_class"])[
        "% of Unique Students Receiving OSS"
    ].mean()["Medium"]

    groups = {
        "Crime Class": ["Low", "Low", "Medium", "Medium", "High", "High"],
        "Percent Unique Suspensions": [
            Low_ISS,
            Low_OSS,
            Medium_ISS,
            Medium_OSS,
            High_ISS,
            High_OSS,
        ],
        "Suspension Type": [
            "In School Suspension (ISS)",
            "Out of School Suspension (OSS)",
            "In School Suspension (ISS)",
            "Out of School Suspension (OSS)",
            "In School Suspension (ISS)",
            "Out of School Suspension (OSS)",
        ],
    }

    groups_df = pd.DataFrame(groups)

    fig = px.bar(
        groups_df,
        x="Crime Class",
        y="Percent Unique Suspensions",
        labels={
            "Percent Unique Suspensions": "% Unique Suspensions",
        },
        title="Percent Unique Suspensions by Community Crime Class",
        color="Suspension Type",
        barmode="group",
    )

    fig.update_layout(title={"y": 0.9, "x": 0.5, "xanchor": "center", "yanchor": "top"})

    fig.update_yaxes(range=[0, 20], row=1, col=1)
    return fig


# using this on misconducts page
def bar_police_crime():
    avg_SS_crime = pd.read_csv(
        "CAPP_project/data_wrangling/merged_data/avg_suspension_crime.csv"
    )

    order = ["Low", "Medium", "High"]
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
        title="Percent of Misconducts Resulting in a Police Notification by Crime Class",
    )
    bar_police_crime.update_layout(yaxis_range=[0, 20])

    bar_police_crime.update_layout(
        title={"y": 0.9, "x": 0.5, "xanchor": "center", "yanchor": "top"}
    )

    return bar_police_crime


##Eshan wrote this
# using this on impact of COVID page
def scatter_pre_post_grid():
    school_df = pd.read_csv(
        "CAPP_project/data_wrangling/merged_data/all_school_merged.csv"
    )
    ## create a scatterplot with trendline
    scatter = px.scatter(
        school_df,
        x="pre_cov_att",
        y="post_cov_att",
        labels={
            "pre_cov_att": "Average Attendance Rate Pre-COVID",
            "post_cov_att": "Average Attendance Rate Post-COVID",
        },
        title="Average Attendance Rate in Pre versus Post COVID Time Periods <br> (Each Point Represents One School)",
        hover_data=["pre_att_bucket", "post_att_bucket"],
    )
    scatter.update_traces(marker=dict(size=7))
    scatter.update_layout(
        title={"y": 0.9, "x": 0.5, "xanchor": "center", "yanchor": "top"}
    )

    avg_x = school_df["pre_cov_att"].mean()
    avg_y = school_df["post_cov_att"].mean()

    scatter.add_hline(
        y=avg_y,
        line_width=1,
        line_color="red",
        annotation_text="Mean of Attendance Post COVID",
        annotation_position="top left",
    )
    scatter.add_vline(
        x=avg_x,
        line_width=1,
        line_color="red",
        annotation_text="Mean of Attendance Pre COVID",
        annotation_position="top left",
    )

    return scatter


# Sarah wrote these
# not using this
def scatter_teachers_pre_post():
    school_df = pd.read_csv(
        "CAPP_project/data_wrangling/merged_data/all_school_merged.csv"
    )

    scatter = px.scatter(
        school_df, x="pre_cov_att", y="post_cov_att", color="teachers_per_100stu"
    )

    avg_x = school_df["pre_cov_att"].mean()
    avg_y = school_df["post_cov_att"].mean()

    scatter.add_hline(y=avg_y, line_width=1, line_color="red")
    scatter.add_vline(x=avg_x, line_width=1, line_color="red")

    return scatter


# not using this
def scatter_race_pre_post():
    school_df = pd.read_csv(
        "CAPP_project/data_wrangling/merged_data/all_school_merged.csv"
    )

    scatter = px.scatter(
        school_df,
        x="pre_cov_att",
        y="post_cov_att",
        color="perc_black_his_stu",
        color_continuous_scale="Bluered_r",
    )
    scatter.update_traces(marker=dict(size=8))

    avg_x = school_df["pre_cov_att"].mean()
    avg_y = school_df["post_cov_att"].mean()

    scatter.add_hline(y=avg_y, line_width=1, line_color="red")
    scatter.add_vline(x=avg_x, line_width=1, line_color="red")

    return scatter


# using this on impact of COVID page
def scatter_income_pre_post():
    school_df = pd.read_csv(
        "CAPP_project/data_wrangling/merged_data/all_school_merged.csv"
    )

    scatter = px.scatter(
        school_df,
        x="pre_cov_att",
        y="post_cov_att",
        labels={
            "pre_cov_att": "Average Attendance Rate Pre-COVID",
            "post_cov_att": "Average Attendance Rate Post-COVID",
            "perc_low_income": "Percent Low- <br> Income Students",
        },
        title="Pre vs. Post COVID Attendance Rates by Percent Low-Income Students <br> (Each Point Represents One School)",
        hover_data=["pre_att_bucket", "post_att_bucket"],
        color="perc_low_income",
        color_continuous_scale="Bluered_r",
    )
    scatter.update_traces(marker=dict(size=7))
    # scatter.update_layout(legend_title="Percent Low Income Students")

    scatter.update_layout(
        title={"y": 0.9, "x": 0.5, "xanchor": "center", "yanchor": "top"}
    )

    avg_x = school_df["pre_cov_att"].mean()
    avg_y = school_df["post_cov_att"].mean()

    scatter.add_hline(
        y=avg_y,
        line_width=1,
        line_color="red",
        annotation_text="Mean of Attendance Post COVID",
        annotation_position="top left",
    )
    scatter.add_vline(
        x=avg_x,
        line_width=1,
        line_color="red",
        annotation_text="Mean of Attendance Pre COVID",
        annotation_position="top left",
    )

    return scatter


# using this on impact of COVID page
def bar_att_diff_buckets():
    """ """
    school_df = pd.read_csv(
        "CAPP_project/data_wrangling/merged_data/all_school_merged.csv"
    )

    pre_att_LL = school_df.groupby(["pre_att_bucket", "post_att_bucket"])[
        "pre_cov_att"
    ].mean()[3]
    post_att_LL = school_df.groupby(["pre_att_bucket", "post_att_bucket"])[
        "post_cov_att"
    ].mean()[3]

    pre_att_LH = school_df.groupby(["pre_att_bucket", "post_att_bucket"])[
        "pre_cov_att"
    ].mean()[2]
    post_att_LH = school_df.groupby(["pre_att_bucket", "post_att_bucket"])[
        "post_cov_att"
    ].mean()[2]

    pre_att_HL = school_df.groupby(["pre_att_bucket", "post_att_bucket"])[
        "pre_cov_att"
    ].mean()[1]
    post_att_HL = school_df.groupby(["pre_att_bucket", "post_att_bucket"])[
        "post_cov_att"
    ].mean()[1]

    pre_att_HH = school_df.groupby(["pre_att_bucket", "post_att_bucket"])[
        "pre_cov_att"
    ].mean()[0]
    post_att_HH = school_df.groupby(["pre_att_bucket", "post_att_bucket"])[
        "post_cov_att"
    ].mean()[0]

    groups = {
        "Average Attendance Rates": [
            pre_att_LL,
            post_att_LL,
            pre_att_LH,
            post_att_LH,
            pre_att_HL,
            post_att_HL,
            pre_att_HH,
            post_att_HH,
        ],
        "Buckets": [
            "Low_Low",
            "Low_Low",
            "Low_High",
            "Low_High",
            "High_Low",
            "High_Low",
            "High_High",
            "High_High",
        ],
        "Time Period": [
            "Pre-COVID",
            "Post-COVID",
            "Pre-COVID",
            "Post-COVID",
            "Pre-COVID",
            "Post-COVID",
            "Pre-COVID",
            "Post-COVID",
        ],
    }
    groups_df = pd.DataFrame(groups)

    fig = px.bar(
        groups_df,
        x="Buckets",
        y="Average Attendance Rates",
        labels={
            "Buckets": "Pre_Post COVID Attendance Category",
        },
        title="Change in Average Attendance by Schools in Pre vs. Post COVID Attendance Rate Categories",
        color="Time Period",
        barmode="group",
    )
    fig.update_layout(title={"y": 0.9, "x": 0.5, "xanchor": "center", "yanchor": "top"})

    return fig


# using this on impact of COVID page
def bar_finance_buckets():
    school_df = pd.read_csv(
        "CAPP_project/data_wrangling/merged_data/all_school_merged.csv"
    )

    dollars_LL = school_df.groupby(["pre_att_bucket", "post_att_bucket"])[
        "dolla_per_student"
    ].mean()[3]
    dollars_LH = school_df.groupby(["pre_att_bucket", "post_att_bucket"])[
        "dolla_per_student"
    ].mean()[2]
    dollars_HL = school_df.groupby(["pre_att_bucket", "post_att_bucket"])[
        "dolla_per_student"
    ].mean()[1]
    dollars_HH = school_df.groupby(["pre_att_bucket", "post_att_bucket"])[
        "dolla_per_student"
    ].mean()[0]

    groups = {
        "Average Dollars Spent per Student": [
            dollars_LL,
            dollars_LH,
            dollars_HL,
            dollars_HH,
        ],
        "Buckets": ["Low_Low", "Low_High", "High_Low", "High_High"],
    }
    groups_df = pd.DataFrame(groups)

    fig = px.bar(
        groups_df,
        x="Buckets",
        y="Average Dollars Spent per Student",
        labels={
            "Buckets": "Pre_Post COVID Attendance Category",
        },
        title="Average Dollars Spent on Students by Pre vs. Post COVID Attendance Categories",
    )
    fig.update_layout(title={"y": 0.9, "x": 0.5, "xanchor": "center", "yanchor": "top"})

    avg_dollars = groups_df["Average Dollars Spent per Student"].mean()
    fig.add_hline(
        y=avg_dollars,
        line_width=1,
        line_color="red",
        annotation_text="Mean Dollars Spent Across All Schools",
        annotation_position="top right",
    )

    return fig
