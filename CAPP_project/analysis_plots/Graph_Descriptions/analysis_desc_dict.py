# ADD ALL PROJECT GRAPH DESCRIPTIONS TO THE BELOW DICTIONARY.
# KEY SHOULD BE SHORT/GRAPHSPECIFIC, AND VALUE SHOULD BE YOUR DESCRIPTION


# To open your plots in ipython3:
#       %load_ext autoreload
#       %autoreload 2
#       from CAPP_project.analysis_plots import plots
#       plots._____

descriptions = {
    "opener (no graph)": "This project aimed to investigate possible contributing factors for low attendance rates in Chicago Public Schools (CPS).",
    "intro one": """Using CPS attendance data since 2003, we averaged attendance rates for pre-k, elementary (grades K-5), middle (grades 6-8),
                    and high (grades 9-12) schools for each available year and plotted them over time. First, we notice attendance rates for elementary and
                    middle school students were higher for all time periods compared to high school and pre-k students. Secondly, for all four school levels,
                    there was a noticeable and lasting dip in attendance following the COVID pandemic (with attendance dropping around 6-8% from 2019 to 2021).
                    For the two school years since COVID (2021 and 2022), high schools are experiencing the lowest attendance rates.
                    We see, on average, only 76% of high school students are regularly attending school, which leaves almost a quarter of the high school-aged 
                    population missing class for 10+ days in a school year. Although pre-k is also showing low attendance, we decided to focus this
                    project on the high school population specifically because of the greater autonomy that the students themselves have when deciding
                    whether to attend the school day.""",
    "intro two": """We limited our attendance data to high school records only. For reference, high schools make up 23% (or 152 of 649)
                of all Chicago Public Schools.""",
    "attend": """CPS has publicly available data about misconducts and suspensions occurring in schools. Within this data, there is a
            statistic that tracks the percent of misconducts that result in a suspension (both in school and out of school suspension).
            We hypothesized that schools which assign suspensions at higher rates when a student gets in trouble would perhaps also show lower
            recorded attendance rates.  In this figure, we plot each school’s average attendance rate by the percent of misconducts which result
            in a suspension. Surprisingly, no clear relationship could be found, which might suggest that these statistics are either unrelated,
            or related only through indirect factors not considered here.""",
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
    "ISS and OSS": """Continuing with the trend of crime and misconduct, we next investigated the average unique suspension rate within a
            school (i.e., the percent of students who receive suspension as a student) to the crime class of the community which the school is located in.
            Again, crime class was assigned to schools located in communities with low, medium, and high crime rates. We hypothesized that in high crime
            communities, the students might be more likely to receive suspensions, either because of factors in their community disrupting their behavior,
            or because the students in these schools are “criminalized” (or seen as more “in need” of a suspension) than the medium and low crime
            class schools. We plot percent of unique suspensions by a school’s community crime class and differentiate by in school and out of school
            suspension. The first observation we make is that for all schools, in school suspension (ISS) is assigned more than out of school suspension
            (OSS). When considering how this affects daily attendance, ISS seems like a better option for encouraging students to hold a routine of going
            to school, even if they are completing a suspension. The second observation we find is that more students in schools from low crime
            communities were given ISS and OSS than students in schools from medium and high crime communities. Surprisingly, schools located in high
            crime communities have, on average, the lowest number of students receiving suspensions.""",
    "police": """Finally, we investigated the percent of misconducts resulting in a police notification for schools located in high, medium,
            and low crime class communities. Following similar logic as before, we guessed that in high crime communities, students are criminalized
            at higher rates, and there is greater police presence in areas where higher crime rates are reported. For these reasons, we hypothesized
            that there would be a greater proportion of police notifications being made on students in high crime community schools. We plotted the
            percent of police notifications being made in schools based on low, medium, and high crime community areas. Our figure represents that the
            percent of police notifications being made is slightly greater for schools in high crime communities, however, the percentage is approximately
            the same across all schools. Only 6.6% of misconducts result in a police notification in high crime community schools, followed by 5.9% in
            the medium crime class, and 5.5% in the low crime class.""",
    "pre_post grid": """Looking at high school attendane in ~150 Chicago Public schools,we created 4 buckets using pre-covid
            and post-covid attendance. This scatter tells us 2 things: one, that most schools lie either in low (pre-covid) - low (post-covid): 42 schools
            or high-high categories: 84 schools. Second, the variation in low-low is a lot more than what we observe in the high-high bucket implying multiple
            factors could be at play for historically low attendance and further drops witnessed during Covid.""",  # plots.scatter_pre_post_grid()
    "change": """This chart tells us the average difference in pre and post Covid attendance across 4 buckets of schools. We observe that
            that highest drops happen in high (pre-Covid) -low (post-Covid) schools. ~20 schools fall in this category and their avg. p.p. diff. is 16.23
            The second highest drop is in the low-low category: 10.44 p.p; 42 schools. Even in the high-high category, we see a p.p. difference of 6.6 p.p
            This indicates while all schools saw attendance drops post Covid, those with historically low attendance were
            impacted more.""",  # plots.bar_att_diff_buckets()
    "income": """This scatter plot confirms two commonly known beliefs: one, majority of Chicago Public Schools have >60'%' students from low
            income backgrounds, and two, all schools with less than 60'%' low income are in the high (pre-Covid)- high(post-Covid) attendance bucket,
            indicating these communities (schools, neighbourhoods) have had historically low attendance and might be disproportionately
            impacted by Covid""",  # plots.scatter_income_pre_post()
    "finance": """Low attendance and budget allocation have received a lot of media coverage in the runup to Mayoral elections in Chicago.
            This chart indicates that schools with low pre-Covid attendance, on average, were allocatted more money per student ($19.6K) in 2022
            than schools with high pre-Covid attendance ($15.6K). While this approach seems wise for schools that have had historically low attendance,
            school district officials might have to treat the high-low schools, with average p.p. diff of 10.44,
            differently too.""",  # plots.bar_finance_buckets()
    "conclusion": """Our goal during this project was to investigate trends in high-school attendance in Chicago Public Schools. While we were able
            to find some interesting insights on distribution of schools, relationship of attendance with misconduct, budget allocation etc., we also
            identified some areas of improvement that could have improved the quality of analysis. 2 areas are:
            1. School-level data: While we sourced data on teacher numbers and salaries (below), the subset of schools that had attendance
            as well as teacher data was low (~50 schools). Same is true for truancy data. We obtained school IDs for these datasets by using Jaro-Winkler
            on school names, but even that did not result in a good enough dataset.
            2. Indicator/dataset selection: We selected community level data from Chicago Health Atlas and CMap. However, since Chicago has only 150 high
            schools and 77 community areas (~2 schools on avg. per community area), we did not find enough variation, or interesting trends between
            in attendance and demographic variables.""",
}

# Webpage tabs:
# Introduction-
#     intro_attendance()
#     intro_two()
# Misconduct-
#     plot_crime()
# scatter_SSrate_attendance()
#
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
