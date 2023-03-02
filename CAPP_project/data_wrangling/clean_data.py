from pathlib import Path
import pandas as pd

cwd = Path.cwd()
parent_dir = cwd.parent

crime_cols = [
    "id",
    "case_number",
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
# crime = pd.read_csv("raw_data/crime.csv", usecols=crime_cols)

# crime = crime[crime["year"] > 2011]
# crime = crime[crime["year"] != 2023]
# crime.dropna(subset="ward", inplace=True)
# crime.drop_duplicates(inplace=True)
# crime["ward"] = crime["ward"].astype(int)
# crime_by_ward = crime.groupby(by=["ward", "year"], as_index=False).size()
# crime_by_ward["crime_capita"] = (
#    crime_by_ward["size"] / 55000
# )  # average population in Chicago wards interpret: crime reports per person in ward.
# crime_by_ward.to_csv("data_wrangling/cleaned_data/crime_by_ward.csv")

# Amari's code for mapping schools
admin_cols = [
    "School_ID",
    "Community Areas",
    "Zip Codes",
    "Census Tracts",
    "Wards",
    "Finance_ID",
    "Student_Count_Total",
    "Student_Count_Low_Income",
    "Student_Count_Black",
    "Student_Count_Hispanic",
    "School_Latitude",
    "School_Longitude",
    "Location",
]
admin_filename = parent_dir / "CAPP_project/raw_data/school_info/admin_demog.csv"
admin = pd.read_csv(
    "CAPP_project/raw_data/school_info/admin_demog.csv", usecols=admin_cols
)
admin_filename,  #
# filtering schools that don't have minimum threshold of children
min_stu_count = 50
admin = admin[admin["Student_Count_Total"] > min_stu_count]

# Adding columns Eshan needs for analysis
admin["perc_black_his_stu"] = (
    admin["Student_Count_Black"] + admin["Student_Count_Hispanic"]
) / admin["Student_Count_Total"]
admin["perc_low_income"] = (
    admin["Student_Count_Low_Income"] / admin["Student_Count_Total"]
)

# Reordering and renaming columns for Eshan's file
school_prf_df = admin.loc[
    :,
    [
        "School_ID",
        "Community Areas",
        "Finance_ID",
        "Student_Count_Total",
        "perc_low_income",
        "perc_black_his_stu",
    ],
]
school_prf_df = school_prf_df.rename(
    columns={
        "School_ID": "sch_id",
        "Community Areas": "ca_id",
        "Finance_ID": "fin_id",
        "Student_Count_Total": "tot_student",
        "School_Latitude": "lat",
        "School_Longitude": "long",
        "Location": "loc",
    }
)
school_prf_df.to_csv(
    parent_dir / "data_wrangling/cleaned_data/clean_school_admin.csv", index=False
)

# Amari's output from admin demog file
schoolid_ward_map = admin[
    ["School_ID", "Wards"]
]  # If planning to look at other variables from file, add them in here
schoolid_ward_map.to_csv(
    parent_dir / "data_wrangling/cleaned_data/schoolid_ward_map.csv"
)

# Load in attendance data; split it into subsets for team
attend_filename = parent_dir / "raw_data/school_info/attendance.csv"
attend = pd.read_csv(attend_filename, usecols=lambda x: x not in ["Group"])
year_range = list(range(2012, 2023))
year_range = list(map(str, year_range))
year_range.remove("2020")  # no attendance data for 2020 - covid.

# For Amari's citywide crime analysis: pending
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
citywide_attend.to_csv(parent_dir / "data_wrangling/cleaned_data/citywide_attend.csv")

attend = attend[attend["School Name"] != "CITYWIDE"]
attend["School ID"] = attend["School ID"].astype(int)
attend.dropna(
    how="all", subset=year_range, inplace=True
)  # drop rows where ALL of the year values are NaN's
attend = attend[
    attend["Grade"].isin(["9", "10", "11", "12"])
]  # only looking at high school attendance

# Eshan's attendance dataset
att_df_group_sid = attend.groupby(["School ID", "School Name", "Network"])[
    ["2018", "2019", "2021", "2022"]
].mean()
att_df_group_sid = att_df_group_sid.reset_index()

# Adding cols for pre-Covid, post-Covid and p.p. diff
att_df_group_sid["pre_cov_att"] = att_df_group_sid[["2018", "2019"]].mean(axis=1)
att_df_group_sid["post_cov_att"] = att_df_group_sid[["2021", "2022"]].mean(axis=1)
att_df_group_sid["att_diff_pp"] = (
    att_df_group_sid["pre_cov_att"] - att_df_group_sid["post_cov_att"]
)

cols_to_select = [
    "School ID",
    "School Name",
    "pre_cov_att",
    "post_cov_att",
    "att_diff_pp",
]
att_df_group_sid.dropna(how="any", inplace=True)
print(att_df_group_sid)
att_df_group_sid[cols_to_select].to_csv(
    parent_dir / "data_wrangling/cleaned_data/clean_attendance.csv", index=False
)

# Amari's analysis: pivot columns - to be edited
attend = pd.melt(
    attend,
    id_vars=["School ID", "Grade", "Network"],
    value_vars=year_range[1:],
    value_name="Attendance",
)  # data is tidy.
attend = attend[attend["Attendance"] != 0.0]
attend = attend[attend["Attendance"] != 100.0]  # untrustworthy reporting
attend.rename(columns={"variable": "Year"}, inplace=True)
attend["Year"] = attend["Year"].astype(int)

avg_attend = attend.groupby(by=["School ID", "Year", "Network"], as_index=False).mean(
    "Attendance"
)
avg_attend.dropna(subset="Attendance", inplace=True)
high_schools = avg_attend["School ID"].unique().tolist()  # Sarah wants this

avg_attend.to_csv(parent_dir / "data_wrangling/cleaned_data/avg_attend.csv")

# Eshan's code: Cleaning finance data
fin_filename = parent_dir / "raw_data/school_info/FY_21_22_budget_data.csv"
sch_finance = pd.read_csv(fin_filename)

# Columns have whitespace: remove and convert to lower
sch_finance.rename(columns=lambda x: x.strip().replace(" ", "_").lower(), inplace=True)

sch_finance = sch_finance.loc[
    :,
    ["finance_id", "fy_2022_proposed_budget"],
]

# Cleaning data: removing whitespaces, string characters and dropping zero rows
sch_finance["fy_2022_proposed_budget"] = sch_finance["fy_2022_proposed_budget"].apply(
    lambda x: float(
        x.replace(",", "").replace("(", "").replace(")", "").strip()
        if x.strip() != "-"
        else 0
    )
)
budget_threshold = 10000
sch_finance = sch_finance.loc[
    (sch_finance["fy_2022_proposed_budget"] > budget_threshold)
]
sch_finance.to_csv(
    parent_dir / "data_wrangling/cleaned_data/clean_school_budget.csv", index=False
)


# Sarah's Data Cleaning: School suspension data
suspension_cols = [
    "School ID",
    "School Name",
    "School Network",
    "School Year",
    "Time Period",
    "% of Misconducts Resulting in a Suspension\n(includes ISS and OSS)",
    "% of Unique Students Receiving ISS",
    "% of Unique Students Receiving OSS",
    "% of Misconducts Resulting in a Police Notification",
]
susp_filename = parent_dir / "raw_data/suspensions/suspension_data.csv"
suspensions = pd.read_csv(susp_filename, usecols=suspension_cols)

# avg_attend = pd.read_csv("data_wrangling/cleaned_data/avg_attend.csv")
# high_schools = avg_attend["School ID"].unique().tolist()
suspensions = suspensions[suspensions["School ID"].isin(high_schools)]
suspensions["School ID"] = suspensions["School ID"].astype(int)

suspensions = suspensions[suspensions["Time Period"] == "EOY"]
suspensions = suspensions[
    suspensions["% of Misconducts Resulting in a Suspension\n(includes ISS and OSS)"]
    != "--"
]
suspensions[
    "% of Misconducts Resulting in a Suspension\n(includes ISS and OSS)"
] = suspensions[
    "% of Misconducts Resulting in a Suspension\n(includes ISS and OSS)"
].astype(
    float
)

suspensions = suspensions[suspensions["% of Unique Students Receiving ISS"] != "--"]
suspensions["% of Unique Students Receiving ISS"] = suspensions[
    "% of Unique Students Receiving ISS"
].astype(float)

suspensions = suspensions[suspensions["% of Unique Students Receiving OSS"] != "--"]
suspensions["% of Unique Students Receiving OSS"] = suspensions[
    "% of Unique Students Receiving OSS"
].astype(float)

suspensions = suspensions[
    suspensions["% of Misconducts Resulting in a Police Notification"] != "--"
]
suspensions["% of Misconducts Resulting in a Police Notification"] = suspensions[
    "% of Misconducts Resulting in a Police Notification"
].astype(float)

suspensions.to_csv(parent_dir / "data_wrangling/cleaned_data/suspension_data.csv")

# Eshan's code: Cleaning health data
# Check final location and name of file- will definitely lead to bugs in case of incorrect pathname
ha_filename = parent_dir / "raw_data/health_data/health_indicators_atlas_v2.csv"
ha_df = pd.read_csv(ha_filename, skiprows=range(4))
ha_df = ha_df.loc[
    :,
    [
        "Name",
        "GEOID",
        "Population",
        "Longitude",
        "Latitude",
        "VRBWP_2013-2017",
        "UNS_2017-2021",
        "VRPNCP_2013-2017",
        "VAC_2017-2021",
        "HTA_2017-2021",
        "HCSCBP_2016-2018",
        "HCSCBP_2020-2021",
        "SNP_2017-2021",
        "SNQ_2017-2021",
        "RBU_2017-2021",
        "VRHOR_2015-2019",
        "VRDIDR_2015-2019",
    ],
]

ha_df = ha_df.rename(
    columns={
        "Name": "comm_area",
        "GEOID": "ca_id",
        "Population": "pop",
        "Longitude": "long",
        "Latitude": "lat",
        "VRBWP_2013-2017": "low_bw_rate",
        "UNS_2017-2021": "uninsured_rate",
        "VRPNCP_2013-2017": "adq_child_care",
        "VAC_2017-2021": "perc_vacant_units",
        "HTA_2017-2021": "perc_sing_par_hh",
        "HCSCBP_2016-2018": "comm_belong_16_18",
        "HCSCBP_2020-2021": "comm_belong_20_21",
        "SNP_2017-2021": "perc_hh_stamps",
        "SNQ_2017-2021": "perc_not_getting_stamps",
        "RBU_2017-2021": "rent_burdened_hh",
        "VRHOR_2015-2019": "homicide_rate",
        "VRDIDR_2015-2019": "drug_induced_dt_rate",
    }
)
# comm_belong_16_18 has 1 missing value; will impute average of remaining
col_impute_val = ha_df["comm_belong_16_18"].mean()
ha_df["comm_belong_16_18"].fillna(col_impute_val, inplace=True)
ha_df.to_csv(
    parent_dir / "data_wrangling/cleaned_data/clean_health_atlas.csv", index=False
)

# Eshan's code: Cleaning demographic data
# Check final location and name of file- will definitely lead to bugs in case of incorrect pathname
demo_filename = parent_dir / "raw_data/demographic_data/cmap_demog_data.csv"
demo_df = pd.read_csv(demo_filename)
demo_df = demo_df.loc[
    :,
    [
        "GEOID",
        "GEOG",
        "CCVI_Score",
        "2000_POP",
        "2020_POP",
        "2020_HH",
        "TOT_POP",
        "MED_AGE",
        "HISP",
        "BLACK",
        "IN_LBFRC",
        "EMP",
        "MEDINC",
        "INCPERCAP",
        "MED_RENT",
        "COMPUTER",
        "INTERNET",
        "highly_walkable_pop_pct",
        "highly_walkable_emp_pct",
    ],
]
# Add new measures to data: dividing by HH/population or calculate differences over time
demo_df["perc_chg_pop"] = (
    (demo_df["2020_POP"] - demo_df["2000_POP"]) / demo_df["2000_POP"]
) * 100
demo_df["perc_black_hispanic"] = (
    (demo_df["HISP"] + demo_df["BLACK"]) / demo_df["TOT_POP"]
) * 100
demo_df["perc_pop_lforce"] = (demo_df["IN_LBFRC"] / demo_df["TOT_POP"]) * 100
demo_df["perc_emp"] = (demo_df["EMP"] / demo_df["IN_LBFRC"]) * 100
demo_df["perc_hh_comp"] = (demo_df["COMPUTER"] / demo_df["2020_HH"]) * 100
demo_df["perc_hh_internet"] = (demo_df["INTERNET"] / demo_df["2020_HH"]) * 100

# Reselecting and reordering columns so that all calculated fields/normalized ones are at the end "CCVI_Score"
demo_df = demo_df.loc[
    :,
    [
        "GEOID",
        "GEOG",
        "MED_AGE",
        "CCVI_Score",
        "perc_chg_pop",
        "perc_black_hispanic",
        "perc_pop_lforce",
        "perc_emp",
        "MEDINC",
        "INCPERCAP",
        "MED_RENT",
        "perc_hh_comp",
        "perc_hh_internet",
        "highly_walkable_pop_pct",
        "highly_walkable_emp_pct",
    ],
]
demo_df = demo_df.rename(
    columns={
        "GEOID": "ca_id",
        "GEOG": "comm_area",
        "MED_AGE": "med_age",
        "CCVI_Score": "covid_idx",
        "MEDINC": "med_inc",
        "INCPERCAP": "inc_p_cap",
        "MED_RENT": "med_rent",
    }
)
demo_df.to_csv(parent_dir / "data_wrangling/cleaned_data/clean_demog.csv", index=False)
