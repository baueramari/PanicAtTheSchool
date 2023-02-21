import pandas as pd

#from data_wrangling import clean_functions

# Check final location and name of file- will definitely lead to bugs in case of incorrect pathname
demo_df = pd.read_csv("cmap_demog_data.csv")
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
        "WHITE",
        "HISP",
        "BLACK",
        "ASIAN",
        "OTHER",
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
#Add new measures to data: dividing by HH/population or calculate differences over time
demo_df["perc_chg_pop"] = (
    (demo_df["2020_POP"] - demo_df["2000_POP"]) / demo_df["2000_POP"]
) * 100
demo_df["perc_white"] = (demo_df["WHITE"] / demo_df["TOT_POP"]) * 100
demo_df["perc_black_hispanic"] = (
    (demo_df["HISP"] + demo_df["BLACK"]) / demo_df["TOT_POP"]
) * 100
demo_df["perc_other_races"] = 100 - (
    demo_df["perc_white"] + demo_df["perc_black_hispanic"]
)
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
        "perc_white",
        "perc_black_hispanic",
        "perc_other_races",
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
demo_df.to_csv("clean_demog.csv", index=False)
# Path will cause bugs if we move things around