import pandas as pd

avg_attend = pd.read_csv("data_wrangling/cleaned_data/avg_attend.csv")
crime_by_ward = pd.read_csv("data_wrangling/cleaned_data/crime_by_ward.csv")
schoolid_ward_map = pd.read_csv("data_wrangling/cleaned_data/schoolid_ward_map.csv")

low_crime = crime_by_ward["crime_capita"].quantile(0.25)
medium_crime = crime_by_ward["crime_capita"].quantile(0.75)
high_crime = float("inf")
crime_by_ward["crime_class"] = pd.cut(
    crime_by_ward["crime_capita"],
    bins=[0, low_crime, medium_crime, high_crime],
    labels=["Low", "Medium", "High"],
)
id_crime_merge = crime_by_ward.merge(
    schoolid_ward_map, how="left", left_on="ward", right_on="Wards"
)
attend_id_crime = id_crime_merge.merge(
    avg_attend,
    how="left",
    left_on=["School_ID", "year"],
    right_on=["School ID", "Year"],
)
attend_id_crime.dropna(how="all", subset=["Year", "Attendance"], inplace=True)

attend_id_crime = attend_id_crime[
    [
        "School_ID",
        "Wards",
        "crime_capita",
        "crime_class",
        "Year",
        "Attendance",
        "Network",
    ]
]
attend_id_crime["Year"] = attend_id_crime["Year"].astype(int)

attend_by_crime = attend_id_crime.groupby(
    by=["crime_class", "Year"], as_index=False
).mean("Attendance")
attend_by_crime = attend_by_crime[["crime_class", "Year", "Attendance"]]

attend_id_crime.to_csv("data_wrangling/cleaned_data/attend_id_crime.csv")
attend_by_crime.to_csv("data_wrangling/cleaned_data/attend_by_crime.csv")


#Sarah's data merge needed for her visuals

crime_cols = [
    "School_ID",
    "crime_class",  
]
ID_crimeclass = pd.read_csv("data_wrangling/cleaned_data/attend_id_crime.csv", usecols=crime_cols)
suspensions = pd.read_csv("data_wrangling/cleaned_data/suspension_data.csv")

high_schools = suspensions["School ID"].unique().tolist()
ID_crimeclass = ID_crimeclass[ID_crimeclass["School_ID"].isin(high_schools)]

suspension_crime_merge = pd.merge(suspensions, ID_crimeclass,
     left_on = "School ID", right_on = "School_ID"
)
suspension_crime_merge.drop('School_ID', axis=1, inplace=True)
suspension_crime_merge.drop_duplicates(inplace=True)
suspension_crime_merge.dropna(how="all", inplace=True)

avg_suspension_crime = suspension_crime_merge.groupby(by="crime_class", as_index=False).mean(numeric_only=True)
avg_suspension_crime.drop('School ID', axis=1, inplace=True)

avg_suspension_crime.to_csv("data_wrangling/cleaned_data/suspension_crime.csv")
