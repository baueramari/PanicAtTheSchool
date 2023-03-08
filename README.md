# PanicAtTheSchool
CAPP 30122 Group Project: 
Sarah, Eshan, and Amari


Our aim of this project is to assess factors which may be contributing to low attendance rates in Chicago public high schools. Based on attendance data from Chicago Public Schools (CPS), grades 9-12 show the lowest attendance rates of all grade levels in the last decade, at an average of about 86.51% before 2019. Moreover, there was a noticeable drop in attendance post-COVID, with high school atteandance rates falling to an average of about 78.79% in school years 2021 and 2022 following the pandemic. 

In our investigation we used CPS data (cps.edu), an API from City of Chicago crime data, and other publically available data sources to investigate factors in attendance. We have broken down our study into two main focus areas: the relationship between school misconducts and community crime rates as an influence on the criminalization of students (which we hypothesized may be associated with changes in attendance), and the impact of COVID in schools. 

During this process, we used pandas to clean our data, plotly to create data visualizations, and dash to launch our web page/application. While further analysis (which goes beyond the scope of this project) would be necessary to truly determine what plays a role in attendance, we were able to find pretty interesting results that could lead to future research opportunities. 

To see our findings, run the following commands within the PanicAtTheSchool repository from your VSCode terminal:

1. ~/PanicAtTheSchool$ poetry install
2. ~/PanicAtTheSchool$ poetry shell
3. (in the shell) ~/PanicAtTheSchool$ python3 -m CAPP_project

Once a user follows these steps, they will get the following message on console:

"Hi user! Please enter 1 if you want to just run the dash app or 2 if you want to check things stepwise: [1/2]"

1. Entering "1" will launch the dash app, which can be opened in browser
2. Entering "2" allows a user to run individual steps/subpackages such as fetching latest API data, cleaning, merging, plotting and finally running the dash app.  

When you have fully explored the webpage and are back in your terminal, run ctrl+d in the terminal to close the application. 