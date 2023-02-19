# CODE TO GENERATE PLOTS
import seaborn as sns
import pandas as pd
import plotly.express as px

attend_by_crime = pd.read_csv("data_wrangling/cleaned_data/attend_by_crime.csv")
citywide = pd.read_csv("data_wrangling/cleaned_data/citywide_attend.csv")

high_crime_wards = attend_by_crime[attend_by_crime["crime_class"] == "High"]
medium_crime_wards = attend_by_crime[attend_by_crime["crime_class"] == "Medium"]
low_crime_wards = attend_by_crime[attend_by_crime["crime_class"] == "Low"]

high = px.line(x=high_crime_wards["Year"], y=high_crime_wards["Attendance"])
high.add_scatter(x=citywide["Year"], y=citywide["Attendance"])

medium = px.line(x=medium_crime_wards["Year"], y=medium_crime_wards["Attendance"])
medium.add_scatter(x=citywide["Year"], y=citywide["Attendance"])

low = px.line(x=low_crime_wards["Year"], y=low_crime_wards["Attendance"])
low.add_scatter(x=citywide["Year"], y=citywide["Attendance"])
