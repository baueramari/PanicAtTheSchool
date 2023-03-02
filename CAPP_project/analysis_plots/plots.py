# CODE TO GENERATE PLOTS
import pandas as pd
import plotly.express as px

# import dash
# from dash import dcc, html
# from dash.dependencies import Input, Output

#Amari wrote plot_crime()
def plot_crime():
    attend_by_crime = pd.read_csv("data_wrangling/merged_data/attend_by_crime.csv")
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
def scatter_SSrate_attendance():
    avg_SS_attend = pd.read_csv("data_wrangling/merged_data/suspension_attendance.csv")
    SSrate_attend_scatter = px.scatter(
        avg_SS_attend,
        x="% of Misconducts Resulting in a Suspension\n(includes ISS and OSS)",
        y="Attendance",
        labels={
            "Attendance": "Average Attendance Rate",
        },
        title="Average Attendance Rate by Percent of Misconducts Resulting in a Suspension",
    )

    return SSrate_attend_scatter

def scatter_OSS_attendance():
    avg_SS_attend = pd.read_csv("data_wrangling/merged_data/suspension_attendance.csv")
    OSS_attend_scatter = px.scatter(
        avg_SS_attend,
        x="% of Unique Students Receiving OSS",
        y="Attendance",
        labels={
            "Attendance": "Average Attendance Rate",
        },
        title="Average Attendance Rate by Percent of Unique Students Receiving Out of School Suspension",
    )

    # scatter.show()
    return OSS_attend_scatter


def scatter_ISS_attendance():
    avg_SS_attend = pd.read_csv("data_wrangling/merged_data/suspension_attendance.csv")
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



def bar_crime_OSS_ISS():

    avg_SS_crime = pd.read_csv("data_wrangling/merged_data/avg_suspension_crime.csv")

    High_ISS = avg_SS_crime.groupby(["crime_class"])["% of Unique Students Receiving ISS"].mean()["High"]
    Medium_ISS = avg_SS_crime.groupby(["crime_class"])["% of Unique Students Receiving ISS"].mean()["Medium"]
    Low_ISS = avg_SS_crime.groupby(["crime_class"])["% of Unique Students Receiving ISS"].mean()["Medium"]

    High_OSS = avg_SS_crime.groupby(["crime_class"])["% of Unique Students Receiving OSS"].mean()["High"]
    Medium_OSS = avg_SS_crime.groupby(["crime_class"])["% of Unique Students Receiving OSS"].mean()["Medium"]
    Low_OSS = avg_SS_crime.groupby(["crime_class"])["% of Unique Students Receiving OSS"].mean()["Medium"]

    groups = {"Crime Class": ["Low", "Low", "Medium", "Medium", "High", "High"],
                "Percent Unique Suspensions": [Low_ISS, Low_OSS, Medium_ISS, Medium_OSS, High_ISS, High_OSS],
                "Suspension Type":["In School Suspension", "Out of School Suspension", "In School Suspension", "Out of School Suspension", "In School Suspension", "Out of School Suspension"]}

    groups_df = pd.DataFrame(groups)

    fig = px.bar(groups_df, 
                x="Crime Class", 
                y="Percent Unique Suspensions",
                title="Percent Unique Suspensions by Crime Class",
                color = "Suspension Type", 
                barmode = "group")
    return fig



def bar_police_crime():
    avg_SS_crime = pd.read_csv("data_wrangling/merged_data/avg_suspension_crime.csv")

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
        title="Percent of Misconducts Resulting in a Police Notification by Crime Class",
    )
    bar_police_crime.update_layout(yaxis_range=[0, 10])

    return bar_police_crime


##Eshan's code to plot
def scatter_pre_post_grid():
    school_df = pd.read_csv("data_wrangling/merged_data/all_school_merged.csv")
    ## create a scatterplot with trendline
    scatter = px.scatter(
        school_df,
        x="pre_cov_att",
        y="post_cov_att",
        labels={
            "pre_cov_att": "Average Attendance Rate in Pre-COVID",
            "post_cov_att": "Average Attendance Rate in Post-COVID",
        },
        title="Average Attendance Rate in Pre versus Post COVID Time Period",
        hover_data=["pre_att_bucket", "post_att_bucket"]
    )

    avg_x = school_df["pre_cov_att"].mean()
    avg_y = school_df["post_cov_att"].mean()

    scatter.add_hline(y= avg_y, line_width = 1, line_color = "red")
    scatter.add_vline(x = avg_x, line_width = 1, line_color = "red")

    ### This part is not needed- will go in dash.py file
    # app = dash.Dash(__name__)
    # app.layout = html.Div([dcc.Graph(id="scatterplot", figure=scatter)])

    return scatter


#Is there enough data points to make this useful? 
def scatter_teachers_pre_post():
    school_df = pd.read_csv("data_wrangling/merged_data/all_school_merged.csv")
    
    scatter = px.scatter(
        school_df,
        x="pre_cov_att",
        y="post_cov_att",
        color = "teachers_per_100stu"
        #title and label here
    )

    avg_x = school_df["pre_cov_att"].mean()
    avg_y = school_df["post_cov_att"].mean()

    scatter.add_hline(y= avg_y, line_width = 1, line_color = "red")
    scatter.add_vline(x = avg_x, line_width = 1, line_color = "red")

    return scatter

#Is this useful?
def scatter_race_pre_post():
    school_df = pd.read_csv("data_wrangling/merged_data/all_school_merged.csv")
    
    scatter = px.scatter(
        school_df,
        x="pre_cov_att",
        y="post_cov_att",
        color = "perc_black_his_stu", 
        color_continuous_scale='Bluered_r',
        #label and title
        
    )
    scatter.update_traces(marker=dict(size=8))

    avg_x = school_df["pre_cov_att"].mean()
    avg_y = school_df["post_cov_att"].mean()

    scatter.add_hline(y= avg_y, line_width = 1, line_color = "red")
    scatter.add_vline(x = avg_x, line_width = 1, line_color = "red")

    return scatter

#will we use this? 
def scatter_income_pre_post():
    school_df = pd.read_csv("data_wrangling/merged_data/all_school_merged.csv")

    scatter = px.scatter(
        school_df,
        x="pre_cov_att",
        y="post_cov_att",
        color = "perc_low_income", 
        color_continuous_scale='Bluered_r',
        #title and labels
        
    )
    scatter.update_traces(marker=dict(size=8))

    avg_x = school_df["pre_cov_att"].mean()
    avg_y = school_df["post_cov_att"].mean()

    scatter.add_hline(y= avg_y, line_width = 1, line_color = "red")
    scatter.add_vline(x = avg_x, line_width = 1, line_color = "red")

    return scatter


def bar_att_diff_buckets():
    '''
    '''
    school_df = pd.read_csv("data_wrangling/merged_data/all_school_merged.csv")

    pre_att_LL = school_df.groupby(["pre_att_bucket", "post_att_bucket"])["pre_cov_att"].mean()[3]
    post_att_LL = school_df.groupby(["pre_att_bucket", "post_att_bucket"])["post_cov_att"].mean()[3]

    pre_att_LH = school_df.groupby(["pre_att_bucket", "post_att_bucket"])["pre_cov_att"].mean()[2]
    post_att_LH = school_df.groupby(["pre_att_bucket", "post_att_bucket"])["post_cov_att"].mean()[2]
    
    pre_att_HL = school_df.groupby(["pre_att_bucket", "post_att_bucket"])["pre_cov_att"].mean()[1]
    post_att_HL = school_df.groupby(["pre_att_bucket", "post_att_bucket"])["post_cov_att"].mean()[1]

    pre_att_HH = school_df.groupby(["pre_att_bucket", "post_att_bucket"])["pre_cov_att"].mean()[0]
    post_att_HH = school_df.groupby(["pre_att_bucket", "post_att_bucket"])["post_cov_att"].mean()[0]

    

    groups = {"Average Attendance Rates" : [pre_att_LL, post_att_LL, pre_att_LH, post_att_LH, pre_att_HL, post_att_HL, pre_att_HH, post_att_HH],
                "Buckets" : ["Low_Low", "Low_Low", "Low_High", "Low_High", "High_Low", "High_Low", "High_High", "High_High"],
                "Time Period" : ["Pre-COVID", "Post-COVID", "Pre-COVID", "Post-COVID", "Pre-COVID", "Post-COVID", "Pre-COVID", "Post-COVID"]
            }
    groups_df = pd.DataFrame(groups)

    fig = px.bar(groups_df, 
                x="Buckets", 
                y="Average Attendance Rates", 
                labels={
                    "Buckets": "Pre vs Post COVID Average Attendance Rates",
                },
                title="Change in Average Attendance in Schools by their Pre vs. Post COVID Attendance Rates",
                color = "Time Period", 
                barmode = "group",
                )
    return fig


def bar_finance_buckets():
    school_df = pd.read_csv("data_wrangling/merged_data/all_school_merged.csv")


    dollars_LL = school_df.groupby(["pre_att_bucket", "post_att_bucket"])["dolla_per_student"].mean()[3]
    dollars_LH = school_df.groupby(["pre_att_bucket", "post_att_bucket"])["dolla_per_student"].mean()[2]
    dollars_HL = school_df.groupby(["pre_att_bucket", "post_att_bucket"])["dolla_per_student"].mean()[1]
    dollars_HH = school_df.groupby(["pre_att_bucket", "post_att_bucket"])["dolla_per_student"].mean()[0]

    groups = {"Average Dollars Spent per Student" : [dollars_LL, dollars_LH, dollars_HL, dollars_HH],
                "Pre vs. Post COVID Attendance Rates" : ["Low_Low", "Low_High", "High_Low", "High_High"]}
    groups_df = pd.DataFrame(groups)

    fig = px.bar(groups_df, 
                x="Pre vs. Post COVID Attendance Rates", 
                y="Average Dollars Spent per Student",
                title="Average Dollars Spent on Students in Schools with Pre vs. Post COVID Attendance Rates",
                )

    avg_dollars = groups_df["Average Dollars Spent per Student"].mean()
    fig.add_hline(y= avg_dollars, line_width = 1, line_color = "red")

    return fig



if __name__ == "__main__":
    app.run_server(debug=True)
