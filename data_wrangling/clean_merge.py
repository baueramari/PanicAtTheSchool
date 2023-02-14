import pandas as pd

#may need to split this into one cleaning file, one merging file?
crime_cols = ['id', 'case_number', 'date', 'iucr',
       'primary_type', 'description', 'arrest',
       'domestic', 'district', 'ward', 'community_area', 'fbi_code',
        'year', 'updated_on']
#crime = pd.read_csv('raw_data/crime.csv', usecols = crime_cols)
crime = crime[crime['year'] > 2011]
crime = crime[crime['year'] != 2023] 

admin_cols = ['School_ID','Short_Name','Long_Name','Primary_Category','Is_High_School','Is_Middle_School',
        'Is_Elementary_School','Is_Pre_School','Summary','Address','City','State','Zip','Phone','Attendance_Boundaries',
        'Grades_Offered_All','Grades_Offered','Student_Count_Total','Student_Count_Low_Income','Student_Count_Special_Ed',
        'Student_Count_English_Learners','Student_Count_Black','Student_Count_Hispanic','Student_Count_White','Student_Count_Asian',
        'Student_Count_Native_American','Student_Count_Other_Ethnicity','Student_Count_Asian_Pacific_Islander',
        'Student_Count_Multi','Student_Count_Hawaiian_Pacific_Islander','Student_Count_Ethnicity_Not_Available',
        'Statistics_Description','Demographic_Description','Title_1_Eligible','Transportation_Bus','Transportation_El',
        'Transportation_Metra','Average_ACT_School','Mean_ACT','College_Enrollment_Rate_School','College_Enrollment_Rate_Mean',
        'Graduation_Rate_School','Graduation_Rate_Mean','Overall_Rating','Rating_Status','Rating_Statement',
        'Classification_Description','School_Year','School_Latitude','School_Longitude','Location','Boundaries - ZIP Codes',
        'Community Areas','Zip Codes','Census Tracts','Wards'] 
admin = pd.read_csv('raw_data/admin_demog.csv', usecols = admin_cols)

admin_to_merge = admin[['School_ID','Wards']] #If planning to look at other variables from file, add them in here

year_range = list(range(2012,2023))
year_range.insert(0,'School ID')

attend = attend[year_range]
attend = attend[attend['School Name'] != 'CITYWIDE']
attend = pd.read_csv('raw_data/attendance.csv')
attend['School ID'] = attend['School ID'].astype(int)

#HANDLE NA'S 
#clean columns, subset to years that we're interested in
#create subset with crime counts and averages by ward

