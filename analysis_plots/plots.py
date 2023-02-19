# CODE TO GENERATE PLOTS
import pandas as pd
import plotly.express as px

attend_by_crime = pd.read_csv("data_wrangling/cleaned_data/attend_by_crime.csv")
citywide = pd.read_csv("data_wrangling/cleaned_data/citywide_attend.csv")
citywide["crime_class"] = "Chicago Average"
attend_by_crime = pd.concat([attend_by_crime, citywide])

medium_crime_wards = attend_by_crime[attend_by_crime["crime_class"] == "Medium"]
low_crime_wards = attend_by_crime[attend_by_crime["crime_class"] == "Low"]
plot_axes = {
    "xaxis_title": "School Year",
    "yaxis_title": "Attendance (% Students at School)",
}

high = px.line(
    attend_by_crime[attend_by_crime["crime_class"].isin(["High", "Chicago Average"])],
    x="Year",
    y="Attendance",
    color="crime_class",
    title="School Attendance in High Crime Wards",
    markers=True,
)
high.update_layout(plot_axes)
high.update_xaxes(tick0=2013, dtick=1)
high.show()

medium = px.line(
    attend_by_crime[attend_by_crime["crime_class"].isin(["Medium", "Chicago Average"])],
    x="Year",
    y="Attendance",
    color="crime_class",
    title="School Attendance in Medium Crime Wards",
    markers=True,
)
medium.update_layout(plot_axes)
medium.update_xaxes(tick0=2013, dtick=1)
medium.show()

low = px.line(
    attend_by_crime[attend_by_crime["crime_class"].isin(["Low", "Chicago Average"])],
    x="Year",
    y="Attendance",
    color="crime_class",
    title="School Attendance in Low Crime Wards",
    markers=True,
)
low.update_layout(plot_axes)
low.update_xaxes(tick0=2013, dtick=1)
low.show()
