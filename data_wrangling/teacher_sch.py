from pathlib import Path
import pandas as pd
from pyjarowinkler import distance

cwd = Path.cwd()
parent_dir = cwd.parent

df_school = pd.read_csv(parent_dir/"raw_data/school_info/admin_demog.csv")
df_school = df_school[["School_ID", "Short_Name", "Long_Name", "Student_Count_Total"]]
df_teacher = pd.read_csv(parent_dir/"raw_data/school_info/EducationDataPortal_02.16.2023_Schools.csv")
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

    for id, s_name, l_name, student in zip(
        df_school["School_ID"], df_school["Short_Name"], df_school["Long_Name"], df_school["Student_Count_Total"]
    ):
        score_1 = distance.get_jaro_distance(row["school_name"], s_name, winkler=True)
        score_2 = distance.get_jaro_distance(row["school_name"], l_name, winkler=True)
        if score_1 > max_score and score_2 > max_score:
            max_score = (score_1 + score_2)/2 
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
threshold_score = 0.85
df_school_ids = df_school_ids[df_school_ids["match_score"] > threshold_score]
df_school_ids = df_school_ids.dropna()
#To tackle duplicates, group by school ID and use max(match_probability)
idx = df_school_ids.groupby("School_ID")["match_score"].idxmax()
df_school_ids = df_school_ids.loc[idx]
df_school_ids.to_csv(parent_dir/"data_wrangling/cleaned_data/clean_teacher.csv", index=True)
#Come back to this - some cleaning can be done here