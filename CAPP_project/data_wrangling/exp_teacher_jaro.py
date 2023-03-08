"""
Author: Eshan 
Objective of this file is to get school-relevant indicators (teacher data and student mobility data) that could impact attendance
"""

import pandas as pd
from pyjarowinkler import distance
import time

def load_school_data():
    """
    Load school, teacher and mobility data csvs which will go as inputs to Jaro-Winkler
    Return clean datasets for school, teacher and mobility daata
    """
    school_cols = ["School_ID", "Short_Name", "Long_Name", "Student_Count_Total"]
    teacher_cols = [
        "school_name",
        "lea_name",
        "teachers_fte_crdc",
        "counselors_fte",
        "social_workers_fte",
        "psychologists_fte",
        "salaries_teachers",
    ]
    mobility_cols = [
        "School Name",
        "District",
        "City",
        "Student Attendance Rate",
        "Student Mobility Rate",
        "Student Chronic Truancy Rate",
        "High School Dropout Rate - Total",
        "Teacher Retention Rate",
    ]

    df_school = pd.read_csv(
        "CAPP_project/raw_data/school_info/admin_demog.csv", usecols=school_cols
    )

    df_teacher = pd.read_csv(
        "CAPP_project/raw_data/school_info/EducationDataPortal_02.16.2023_Schools.csv",
        usecols=teacher_cols,
    )
    df_teacher = df_teacher[df_teacher["lea_name"].str.contains("Chicago")]

    df_mobility = pd.read_csv(
        "CAPP_project/raw_data/mobility/mobility_data.csv", usecols=mobility_cols
    )
    df_mobility = df_mobility.dropna(
        subset=["City", "School Name", "High School Dropout Rate - Total"]
    )
    df_mobility = df_mobility[df_mobility["District"].str.contains("Chicago")]
    return df_school, df_teacher, df_mobility

def get_school_jaro_distance(School, DataFrame, name):
    """
    Match school names using jaro-winkler probability to obtain school ID. Also take care of possible duplicates
    Return the dataframe for which matching has been done
    """
    threshold_score = 0.80
    ids = []
    tot_students = []
    scores = []
    for index, row in DataFrame.iterrows():
        max_score = 0
        match_id = None
        num_student = 0
        for id, s_name, l_name, students in zip(
            School["School_ID"],
            School["Short_Name"],
            School["Long_Name"],
            School["Student_Count_Total"],
        ):
            score_1 = distance.get_jaro_distance(row[name], s_name, winkler=True)
            score_2 = distance.get_jaro_distance(row[name], l_name, winkler=True)

            if (
                score_1 > threshold_score
                and score_1 > max_score
                and score_2 > threshold_score
                and score_2 > max_score
            ):
                max_score = (score_1 + score_2) / 2
                match_id = id
                num_student = students
        ids.append(match_id)
        tot_students.append(num_student)
        scores.append(max_score)
    DataFrame = DataFrame.assign(
        match_id=ids, num_student=tot_students, max_score=scores
    )

    # Now clean the dataset
    min_stu_count = 50
    DataFrame = DataFrame[DataFrame["num_student"] > min_stu_count]
    DataFrame = DataFrame.dropna()

    # To tackle duplicates, group by school ID and use max(match_probability)
    idx = DataFrame.groupby("match_id")["max_score"].idxmax()
    DataFrame = DataFrame.loc[idx]
    return DataFrame


# Teacher data analysis
def prepare_teacher(Teacher):
    """
    Modify and add additional cols to teacher data
    """
    Teacher["teachers_per_100_stu"] = (
        Teacher["teachers_fte_crdc"] / Teacher["num_student"]
    ) * 100
    Teacher["help_per_100_stu"] = (
        (
            Teacher["counselors_fte"]
            + Teacher["social_workers_fte"]
            + Teacher["psychologists_fte"]
        )
        / Teacher["num_student"]
    ) * 100
    Teacher["salary_per_teach"] = (Teacher["salaries_teachers"].astype(float)).divide(
        Teacher["teachers_fte_crdc"]
    )
    return Teacher
    
def go():
    df_school, df_teacher, df_mobility = load_school_data()
    teacher_ids = get_school_jaro_distance(df_school, df_teacher, "school_name")
    teacher_ids = prepare_teacher(teacher_ids)
    teacher_ids.to_csv("CAPP_project/data_wrangling/cleaned_data/clean_teacher.csv", index=True)

    mobility_ids = get_school_jaro_distance(df_school, df_mobility, "School Name")
    mobility_ids.to_csv("CAPP_project/data_wrangling/cleaned_data/clean_mobility.csv", index=True)