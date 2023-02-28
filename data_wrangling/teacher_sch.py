import pandas as pd
import recordlinkage
from pyjarowinkler import distance

df_school = pd.read_csv("raw_data/admin_demog.csv")
df_school = df_school[["School_ID", "Long_Name", "Student_Count_Total"]]
df_teacher = pd.read_csv(
    "raw_data/school_info_ep/EducationDataPortal_02.16.2023_Schools.csv"
)
df_teacher = df_teacher[df_teacher["lea_name"].str.contains("Chicago")]
df_teacher = df_teacher[
    [
        "school_name",
        "lea_name",
        "teachers_fte_crdc",
        "counselors_fte",
        "social_workers_fte",
        "psychologists_fte",
        "salaries_teachers",
    ]
]

school_ids = {}

for index, row in df_teacher.iterrows():
    max_score = 0
    match_id = None

    for id, name, student in zip(
        df_school["School_ID"], df_school["Long_Name"], df_school["Student_Count_Total"] #student testing pending
    ):
        score = distance.get_jaro_distance(row["school_name"], name, winkler=True)
        if score > max_score:
            max_score = score
            match_id = id
    school_ids[row["school_name"]] = (
        match_id,
        max_score,
        row["teachers_fte_crdc"],
        (row["teachers_fte_crdc"] / student)*100,
        ((row["counselors_fte"] + row["social_workers_fte"] + row["psychologists_fte"])/student)*100,
        row["salaries_teachers"])
df_school_ids = pd.DataFrame.from_dict(
    school_ids,
    orient="index",
    columns=[
        "School_ID",
        "match_score",
        "teachers",
        "teachers_per_100stu",
        "help_fte_per_100stu",
        "teacher_salary",
    ],
)
threshold_score = 0.89
df_school_ids = df_school_ids[df_school_ids["match_score"] > threshold_score]
df_school_ids = df_school_ids.dropna()
df_school_ids.to_csv("data_wrangling/cleaned_data/clean_teacher.csv", index=True)