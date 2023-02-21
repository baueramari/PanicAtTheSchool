import pandas as pd

sch_finance = pd.read_csv(
    "/home/eshanprashar/PanicAtTheSchool/raw_data/school_info_ep/FY_21_22_budget_data.csv"
)

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
sch_finance.to_csv("clean_school_budget.csv", index=False)
