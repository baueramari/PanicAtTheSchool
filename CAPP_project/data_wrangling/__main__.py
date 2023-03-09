from CAPP_project.data_wrangling import clean_data, merge_data
import time

def run(name):
    start_time = time.time()
    if name == "clean":
        clean_data.clean_data()
    if name == "merge":
        merge_data.data_merge()
    if name == "exploratory":
        print("Sit back, Jaro-Wink in progress!")
        from CAPP_project.data_wrangling import exp_teacher_jaro, exploratory_merge
        exp_teacher_jaro.go()
        exploratory_merge.merge_teach_mobility()
        exploratory_merge.merge_school_demo()
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"{name} ran data successfully in {elapsed_time:.2f} seconds!")