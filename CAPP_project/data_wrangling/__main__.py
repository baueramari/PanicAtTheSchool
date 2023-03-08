from CAPP_project.data_wrangling import clean_data, merge_data
import time

def run(name):
    if name == "clean":
        start_time = time.time()
        clean_data.clean_data()
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Cleaned data successfully in {elapsed_time:.2f} seconds!")
    if name == "merge":
        start_time = time.time()
        merge_data.data_merge()
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Merged data successfully in {elapsed_time:.2f} seconds!")
    if name == "exploratory":
        print("Sit back, Jaro-Wink in progress!")
        from CAPP_project.data_wrangling import exp_teacher_jaro, exploratory_merge
        start_time = time.time()
        exp_teacher_jaro.go()
        exploratory_merge.merge_teach_mobility()
        exploratory_merge.merge_school_demo()
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Ran Jaro-Winkler for school matching, and merged files in {elapsed_time:.2f} seconds!")