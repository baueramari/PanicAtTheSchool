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
