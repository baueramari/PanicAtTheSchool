from CAPP_project.analysis_plots import plots

# from CAPP_project.analysis_plots import exploratory_plots
import time


def run(name):
    if name == "plot":
        start_time = time.time()
        plots.plot_crime(),
        plots.scatter_SSrate_attendance(),
        plots.scatter_ISS_attendance(),
        plots.bar_crime_OSS_ISS(),
        plots.bar_police_crime(),
        plots.scatter_pre_post_grid(),
        plots.scatter_income_pre_post(),
        plots.bar_att_diff_buckets(),
        plots.bar_finance_buckets(),
        plots.intro_attendance(),
        plots.intro_two(),
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Plotted data successfully in {elapsed_time:.2f} seconds!")
