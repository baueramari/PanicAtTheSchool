import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

# from data_wrangling import clean_functions

# Check final location and name of file- could lead to bug
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
# Checking number of observations for every column
# for column in demo_df:
#    mis_values = demo_df[column].isna().sum()
#    if mis_values > 0:
#        print(f'Column "{column}" has {mis_values} missing value(s)')

# Add new measures to data: dividing by HH/population or calculate differences over time
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
# print(demo_df.columns[2:])
# Data has all columns we need, now we normalize columns -- Use a function to achieve this
cols_to_normalize = demo_df.columns[2:]
demo_df_to_normalize = demo_df[cols_to_normalize]
scaler = StandardScaler()
demo_df_normalized = pd.DataFrame(
    scaler.fit_transform(demo_df_to_normalize), columns=cols_to_normalize
)
demo_df[cols_to_normalize] = demo_df_normalized
demo_df.to_csv("normalized_demog.csv", index=False)

# Path will cause bugs if we move things around