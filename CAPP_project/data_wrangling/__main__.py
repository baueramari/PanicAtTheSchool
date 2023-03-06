from CAPP_project.data_wrangling import clean_data, merge_data
import time

def run(name):
    if name == "clean":
        start_time = time.time()
        clean_data.clean()
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Cleaned data successfully in {elapsed_time:.2f} seconds!")
    if name == "merge":
        start_time = time.time()
        merge_data.merge()
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Merged data successfully in {elapsed_time:.2f} seconds!")