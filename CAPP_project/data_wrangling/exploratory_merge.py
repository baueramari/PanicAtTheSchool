"""
Author: Eshan
The objective of this file is to merge datasets: a) teacher-mobility and b) attendance-demographic\
information which we eventually put in "exploratory" section
"""

import pandas as pd

def merge_teach_mobility():
    """
    Merge teacher and mobility data for exploration
    """
    teacher_df = pd.read_csv("CAPP_project/data_wrangling/cleaned_data/clean_teacher.csv")
    mobility_df = pd.read_csv("CAPP_project/data_wrangling/cleaned_data/clean_mobility.csv")

    tch_mob_merge = pd.merge(teacher_df, mobility_df, how = "left", on = "match_id")
    print(tch_mob_merge.columns)

    cols_to_drop = [
        "Unnamed: 0_x",
        "lea_name",
        "num_student_x",
        "max_score_x",
        "Unnamed: 0_y",
        "School Name", 
        "District",
        "City",
        "num_student_y",
        "max_score_y",
    ]
    tch_mob_merge = tch_mob_merge.drop(cols_to_drop, axis=1)
    tch_mob_merge.to_csv("CAPP_project/data_wrangling/merged_data/exp_teach_mob.csv")

def merge_school_demo():
    """
    Merge school data with demographic and health data at community level to explore trends at community level
    """

    cols_to_keep = ["ca_id", "pre_cov_att", "post_cov_att", "att_diff_pp"]
    school_merged = pd.read_csv("CAPP_project/data_wrangling/merged_data/all_school_merged.csv")
    att_demo = school_merged.loc[:, cols_to_keep]

    demog_info = pd.read_csv("CAPP_project/data_wrangling/cleaned_data/clean_demog.csv")
    health_info = pd.read_csv("CAPP_project/data_wrangling/cleaned_data/clean_health_atlas.csv")

    cols_grouping = {"ca_id": "count"}
    cols_grouping.update({col: "mean" for col in att_demo.columns if col != "ca_id"})
    att_demo = att_demo.groupby("ca_id").agg(cols_grouping)
    att_demo = att_demo.rename(columns={"ca_id": "count_schools"})
    att_demo = att_demo.reset_index()

    # Threshold for number of schools
    num_schools = 2
    att_demo = att_demo[att_demo["count_schools"] >= num_schools]

    # School data ready, now merge demographic and health data with this
    merged_att_demo = pd.merge(att_demo, demog_info, on="ca_id")
    merged_att_demo = pd.merge(merged_att_demo, health_info, on="ca_id")
    cols_to_drop = ["comm_area_y"]
    merged_att_demo = merged_att_demo.drop(cols_to_drop, axis=1)
    merged_att_demo.to_csv(
        "CAPP_project/data_wrangling/merged_data/exp_school_demo_merged.csv", index=False
    )