"""
Author: Eshan 
#Objective is to give user the flexibiity to jump to the app directly or just run sub-packages
"""
import sys
import pathlib
from CAPP_project.dash_app import app
from CAPP_project.analysis_plots import __main__ as ap_main
from CAPP_project.raw_data.crime_api import crime_extract


def package_breakdown():
    """
    Function to run different files (and associated functions) based on input given by user in console
    Input: None
    Returns: None. Executes selected file/function and reports time to run
    """
    sys_args = ["fetch", "clean", "merge", "plot", "exploratory", "all"]
    print(f"Great! Choose one of the steps:{sys_args} or exit")
    arg = input().lower()

    if arg == "fetch":
        print(
            "Hope you got the correct API key...\
        Fetching crime data from Chicago data portal...\
        this will take ~10 minutes! If you want to exit, press Ctrl+C"
        )
        crime_extract()

    elif arg == "plot":
        ap_main.run(arg)

    elif arg == "clean" or arg == "merge" or arg == "exploratory" or arg == "all":
        from CAPP_project.data_wrangling import (
            __main__ as dw_main,
        )

        if arg == "clean" or "all":
            print(
                "Please check ReadMe for steps to access the crime.csv. Program will stop if not already added!"
            )
            dw_main.run(arg)
        if arg == "all":
            print(
                "This includes fetching latest data which takes ~10 mins;\
                 type y if you want to continue or type n if you want to skip fetching:[y/n]"
            )
            if input().lower() == "y":
                crime_extract()
            print("Now importing other files, sit back...")
            dw_main.run("clean")
            dw_main.run("merge")
            ap_main.run("plot")
            print("And we're ready...")
            app.run_server(port=6094)
    else:
        print(f"Unknown step: {arg}")
        sys.exit(1)


if __name__ == "__main__":
    print(
        "Hi user! Please enter 1 if you want to just run the dash app or 2 if you want to check things stepwise: [1/2]"
    )
    arg = input()
    if arg == "2":
        package_breakdown()
    elif arg == "1":
        app.run_server(port=6094)
        print("Now do you want to check step-wise operations? [y/n]")
        new_arg = input().lower()
        if new_arg == "y":
            package_breakdown()
        elif new_arg == "n":
            sys.exit(1)
        else:
            print(sys.argv)
            print(f"Unknown command:{new_arg}. Please try again!")
    else:
        print(f"Unknown command: {arg}")
        sys.exit(1)
