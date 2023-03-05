# ADD ALL PROJECT GRAPH DESCRIPTIONS TO THE BELOW DICTIONARY.
# KEY SHOULD BE SHORT/GRAPHSPECIFIC, AND VALUE SHOULD BE YOUR DESCRIPTION


# To open your plots in ipython3:
#       %load_ext autoreload
#       %autoreload 2
#       from CAPP_project.analysis_plots import plots
#       plots._____

descriptions = {
    "intro one": "Sarah",  # plots.intro_attendance()
    "intro two": "Sarah",  # plots.intro_two()
    "attend": "Someone",  # plots.scatter_SSrate_attendance()
    "crime": """News sources have identified crime rates as a key factor in falling attendance at Chicago 
            Public Schools. By categorizing the data into the wards with the highest, lowest, and middle-ground 
            levels of crime, we are able to identify schools that operate in these varying environments. 
            By tracking attendance over the years, we intended to investigate those news claims and 
            identify any relationship that may exist between varying levels of crime and attendance. 
            We found that schools in the lowest tercile for crime reports actually experienced the 
            largest drop in attendance, particularly since 2019, which is the opposite of what we had 
            expected. Further research would benefit from looking more closely at the several wards 
            that changed crime class during this ten year period, and how attendance correlates 
            with that shift, rather than overall crime levels.""",
    "ISS and OSS": "Sarah writes this",  # plots.bar_crime_OSS_ISS()
    "police": "Sarah writes this",  # plots.bar_police_crime()
    "pre_post grid": "Eshan writes this",  # plots.scatter_pre_post_grid()
    "income": "Eshan writes this",  # plots.scatter_income_pre_post()
    "change": "Eshan writes this",  # plots.bar_att_diff_buckets()
    "finance": "Eshan writes this",  # plots.bar_finance_buckets()
    "somebody": "Somebody writes this",
    "conclusion": "Eshan writes this",
}

# Webpage tabs:
# Introduction-
#     intro_attendance()
#     intro_two()
# Misconduct-
#     plot_crime()
#     scatter_SSrate_attendance()
#     bar_crime_OSS_ISS()
#     bar_police_crime()
# Impact of COVID in Schools -
#     scatter_pre_post_grid()
#     scatter_income_pre_post()
#     bar_att_diff_buckets()
#     bar_finance_buckets()
# Conclusion-
#     text that Eshan will investigate


# To do:
#     -We each write our plot descriptions in dictionary above
#     -Conclusion/Further Research Opportunities - Eshan write description for this
#     -Eshan = __init__ and package details... Get the program running front to back how we will turn it in
#     -Write documentation/update ReadMe
#     -Check rubric and make sure we have everything
