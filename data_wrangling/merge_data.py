import pandas as pd

avg_attend = pd.read_csv("data_wrangling/cleaned_data/avg_attend.csv")
crime_by_ward = pd.read_csv("data_wrangling/cleaned_data/crime_by_ward.csv")
schoolid_ward_map = pd.read_csv("data_wrangling/cleaned_data/schoolid_ward_map.csv")

id_crime_merge = crime_by_ward.merge(
    schoolid_ward_map, how="left", left_on="ward", right_on="Wards"
)
id_crime_merge = id_crime_merge[["School_ID", "Wards", "year", "crime_capita"]]

attend_id_crime = id_crime_merge.merge(
    avg_attend,
    how="left",
    left_on=["School_ID", "year"],
    right_on=["School ID", "Year"],
)
attend_id_crime.dropna(how="all", subset=["Year", "Attendance"], inplace=True)

attend_id_crime = attend_id_crime[
    ["School_ID", "Wards", "crime_capita", "Year", "Attendance"]
]
attend_id_crime["Year"] = attend_id_crime["Year"].astype(int)

attend_id_crime.to_csv("data_wrangling/cleaned_data/attend_id_crime.csv")
