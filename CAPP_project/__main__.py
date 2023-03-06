"""
Eshan wrote this file
#Objective is to give user the flexibiity to jump to the app or just test functions in specific modules
"""
import sys
import pathlib
from CAPP_project.dash_app import app
from CAPP_project.data_wrangling import __main__ as dw_main
from CAPP_project.analysis_plots import __main__ as ap_main

def package_breakdown():
    """
    Function to run different files (and associated functions) based on input given by user in console
    Input: One of the following commands from variable sys_args
    Returns: Execute command and give confirmation message (TBD)
    """
    sys_args = ["fetch", "clean", "merge", "plot", "explore", "all"]
    print(f"Great! Choose one of the steps:{sys_args}:")
    arg = input().lower()
    if arg == "all":
        dw_main.run(arg)
        ap_main.run(arg)
    elif arg == "clean" or arg == "merge":
        dw_main.run(arg)
    elif arg == "plot":
        ap_main.run(arg) 
    else:
        print(f"Unknown step: {arg}")
        sys.exit(1)

if __name__ == "__main__":
    print("Hi user! Do you want to jump to our dash app or run the app stepwise? [jump/stepwise]")
    arg = input().lower()
    if arg == "stepwise":
        package_breakdown()
    elif arg == "jump":
        app.run_server(port=6093)
        print("Now, do you want to run package stepwise? [y/n]")
        if arg == "n":
            print("Great,looking forward to the feedback!")
        elif arg == "y":
            package_breakdown()
        else:
            print(f"Unknown command: {arg}")
            sys.exit()
    else:
        print(f"Unknown command: {arg}")
        sys.exit()