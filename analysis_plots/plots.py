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
        title="School's Average Attendance Rate by Percent of Misconducts Resulting in a Suspension",
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
        title="School's Average Attendance Rate by Percent of Unique Students Receiving Out of School Suspension",
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
        title="School's Average Attendance Rate by Percent of Unique Students Receiving In School Suspension",
    )

    return ISS_attend_scatter



# OH with James -- how can I get these side by side? 
def bar_crime_ISS():

    avg_SS_crime = pd.read_csv("data_wrangling/merged_data/avg_suspension_crime.csv", use_cols)

    order = ["High", "Medium", "Low"]
    avg_SS_crime["crime_class"] = pd.Categorical(
        avg_SS_crime["crime_class"], categories=order
    )
    avg_SS_crime = avg_SS_crime.sort_values("crime_class")

    fig_ISS = px.bar(avg_SS_crime, x="crime_class", y="% of Unique Students Receiving ISS")


    # avg_SS_crime = pd.read_csv("data_wrangling/cleaned_data/suspension_crime.csv")
    # fig = go.Figure(go.Bar(x="crime_class", y="% of Unique Students Receiving OSS"))
    # fig.add_trace(go.Bar(x="crime_class", y="% of Unique Students Receiving ISS"))
    # fig.update_layout(barmode="stack")
    fig_ISS.show()


def bar_crime_OSS():

    avg_SS_crime = pd.read_csv("data_wrangling/merged_data/avg_suspension_crime.csv", use_cols)

    order = ["High", "Medium", "Low"]
    avg_SS_crime["crime_class"] = pd.Categorical(
        avg_SS_crime["crime_class"], categories=order
    )
    avg_SS_crime = avg_SS_crime.sort_values("crime_class")
    
    fig_OSS = px.bar(avg_SS_crime, x="crime_class", y="% of Unique Students Receiving OSS")

    return fig_OSS



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
        title="School's Percent of Misconducts Resulting in a Police Notification by Crime Class",
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


#I'm gonna say this is not super useful 
def scatter_teachers_pre_post():
    school_df = pd.read_csv("data_wrangling/merged_data/all_school_merged.csv")
    ## create a scatterplot with trendline
    scatter = px.scatter(
        school_df,
        x="pre_cov_att",
        y="post_cov_att",
        color = "teachers_per_100stu"
    )

    avg_x = school_df["pre_cov_att"].mean()
    avg_y = school_df["post_cov_att"].mean()

    scatter.add_hline(y= avg_y, line_width = 1, line_color = "red")
    scatter.add_vline(x = avg_x, line_width = 1, line_color = "red")

    ### This part is not needed- will go in dash.py file
    # app = dash.Dash(__name__)
    # app.layout = html.Div([dcc.Graph(id="scatterplot", figure=scatter)])

    return scatter

#this is cool... but will we use it? 
def scatter_race_pre_post():
    school_df = pd.read_csv("data_wrangling/merged_data/all_school_merged.csv")
    ## create a scatterplot with trendline
    scatter = px.scatter(
        school_df,
        x="pre_cov_att",
        y="post_cov_att",
        color = "perc_black_his_stu", 
        color_continuous_scale='Bluered_r',
        
    )
    scatter.update_traces(marker=dict(size=8))

    avg_x = school_df["pre_cov_att"].mean()
    avg_y = school_df["post_cov_att"].mean()

    scatter.add_hline(y= avg_y, line_width = 1, line_color = "red")
    scatter.add_vline(x = avg_x, line_width = 1, line_color = "red")

    ### This part is not needed- will go in dash.py file
    # app = dash.Dash(__name__)
    # app.layout = html.Div([dcc.Graph(id="scatterplot", figure=scatter)])

    return scatter

#again, cool but credible? 
def scatter_income_pre_post():
    school_df = pd.read_csv("data_wrangling/merged_data/all_school_merged.csv")
    ## create a scatterplot with trendline
    scatter = px.scatter(
        school_df,
        x="pre_cov_att",
        y="post_cov_att",
        color = "perc_low_income", 
        color_continuous_scale='Bluered_r',
        
    )
    scatter.update_traces(marker=dict(size=8))

    avg_x = school_df["pre_cov_att"].mean()
    avg_y = school_df["post_cov_att"].mean()

    scatter.add_hline(y= avg_y, line_width = 1, line_color = "red")
    scatter.add_vline(x = avg_x, line_width = 1, line_color = "red")

    ### This part is not needed- will go in dash.py file
    # app = dash.Dash(__name__)
    # app.layout = html.Div([dcc.Graph(id="scatterplot", figure=scatter)])

    return scatter


def sarahs_merge_edit():
    '''
    '''
    school_df = pd.read_csv("data_wrangling/merged_data/all_school_merged.csv")

    school_df["pre_post"] = ""

    # school_df.loc[(school_df["pre_att_bucket"] == "low" and school_df["post_att_bucket"] == "low"), ["pre_post"]] = 'LL'
    
    for _, row in school_df.iterrows():
        if row["pre_att_bucket"] == "low" and row["post_att_bucket"] == "low":
            row["pre_post"] = "LL"
        elif row["pre_att_bucket"] == "low" and row["post_att_bucket"] == "high":
            row["pre_post"] = "LH"
        elif row["pre_att_bucket"] == "high" and row["post_att_bucket"] == "low":
            row["pre_post"] = "HL"
        else:
            row["pre_post"] = "HH"

    return school_df


def bar_att_diff_buckets():
    df = sarahs_merge_edit()

    fig = px.bar(df, x="pre_post", y="att_diff_pp")

    return fig

def bar_finance_buckets():
    df = sarahs_merge_edit()

    fig = px.bar(df, x="pre_post", y="dolla_per_student")
    avg_dollars = df["dolla_per_student"].mean()
    fig.add_hline(y= avg_dollars, line_width = 1, line_color = "red")

    return fig

#update df s.t. new categorical column is made 
#two graphs I can do 


if __name__ == "__main__":
    app.run_server(debug=True)
