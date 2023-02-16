import pandas as pd

crime_cols = [
    "id",
    "case_number",
    "date",
    "iucr",
    "primary_type",
    "description",
    "arrest",
    "domestic",
    "district",
    "ward",
    "community_area",
    "fbi_code",
    "year",
    "updated_on",
]
crime = pd.read_csv("raw_data/crime.csv", usecols=crime_cols)

crime = crime[crime["year"] > 2011]
crime = crime[crime["year"] != 2023]
crime.dropna(subset="ward", inplace=True)
crime.drop_duplicates(inplace=True)
crime["ward"] = crime["ward"].astype(int)
crime_by_ward = crime.groupby(by=["ward", "year"], as_index=False).size()
crime_by_ward["crime_capita"] = (
    crime_by_ward["size"] / 55000
)  # average population in Chicago wards
crime_by_ward.to_csv("data_wrangling/cleaned_data/crime_by_ward.csv")


admin_cols = [
    "School_ID",
    "Short_Name",
    "Long_Name",
    "Primary_Category",
    "Is_High_School",
    "Is_Middle_School",
    "Is_Elementary_School",
    "Is_Pre_School",
    "Summary",
    "Address",
    "City",
    "State",
    "Zip",
    "Phone",
    "Attendance_Boundaries",
    "Grades_Offered_All",
    "Grades_Offered",
    "Student_Count_Total",
    "Student_Count_Low_Income",
    "Student_Count_Special_Ed",
    "Student_Count_English_Learners",
    "Student_Count_Black",
    "Student_Count_Hispanic",
    "Student_Count_White",
    "Student_Count_Asian",
    "Student_Count_Native_American",
    "Student_Count_Other_Ethnicity",
    "Student_Count_Asian_Pacific_Islander",
    "Student_Count_Multi",
    "Student_Count_Hawaiian_Pacific_Islander",
    "Student_Count_Ethnicity_Not_Available",
    "Statistics_Description",
    "Demographic_Description",
    "Title_1_Eligible",
    "Transportation_Bus",
    "Transportation_El",
    "Transportation_Metra",
    "Average_ACT_School",
    "Mean_ACT",
    "College_Enrollment_Rate_School",
    "College_Enrollment_Rate_Mean",
    "Graduation_Rate_School",
    "Graduation_Rate_Mean",
    "Overall_Rating",
    "Rating_Status",
    "Rating_Statement",
    "Classification_Description",
    "School_Year",
    "School_Latitude",
    "School_Longitude",
    "Location",
    "Boundaries - ZIP Codes",
    "Community Areas",
    "Zip Codes",
    "Census Tracts",
    "Wards",
]  # many potentially useful variables
admin = pd.read_csv("raw_data/admin_demog.csv", usecols=admin_cols)

schoolid_ward_map = admin[
    ["School_ID", "Wards"]
]  # If planning to look at other variables from file, add them in here
schoolid_ward_map.to_csv("data_wrangling/cleaned_data/schoolid_ward_map.csv")


attend = pd.read_csv(
    "raw_data/attendance.csv", usecols=lambda x: x not in ["Group", "Network"]
)
year_range = list(range(2012, 2023))
year_range = list(map(str, year_range))
year_range.remove("2020")  # no attendance data for 2020 - covid.

citywide = attend[attend["School Name"] == "CITYWIDE"]
citywide = citywide[citywide["Grade"].isin(["9", "10", "11", "12"])]
citywide = pd.melt(
    citywide,
    id_vars=["Grade"],
    var_name="Year",
    value_vars=year_range[1:],
    value_name="Attendance",
)
citywide_attend = citywide.groupby(by="Year").mean("Attendance")
citywide_attend.to_csv("data_wrangling/cleaned_data/citywide_attend.csv")

attend = attend[attend["School Name"] != "CITYWIDE"]
attend["School ID"] = attend["School ID"].astype(int)
attend.dropna(
    how="all", subset=year_range, inplace=True
)  # drop rows where ALL of the year values are NaN's
attend = attend[
    attend["Grade"].isin(["9", "10", "11", "12"])
]  # only looking at high school attendance
attend = pd.melt(
    attend,
    id_vars=["School ID", "Grade"],
    value_vars=year_range[1:],
    value_name="Attendance",
)  # data is tidy.
attend = attend[attend["Attendance"] != 0.0]
attend = attend[attend["Attendance"] != 100.0]  # untrustworthy reporting
attend.rename(columns={"variable": "Year"}, inplace=True)
attend["Year"] = attend["Year"].astype(int)

avg_attend = attend.groupby(by=["School ID", "Year"], as_index=False).mean("Attendance")
avg_attend.dropna(subset="Attendance", inplace=True)
avg_attend.to_csv("data_wrangling/cleaned_data/avg_attend.csv")
