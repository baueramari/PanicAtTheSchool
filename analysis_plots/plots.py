# CODE TO GENERATE PLOTS
import pandas as pd
import plotly.express as px

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
crime_attend.show()
