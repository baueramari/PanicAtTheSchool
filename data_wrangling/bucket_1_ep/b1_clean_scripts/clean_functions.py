#<Add function to normalize data>
from sklearn.preprocessing import StandardScaler

def normalize_data(DataFrame, DataFrame.columns,output_csv_path):
    cols_to_normalize = DataFrame.columns
    df_to_normalize = DataFrame[cols_to_normalize]
    scaler = StandardScaler()
    df_normalized = pd.DataFrame(scaler.fit_transform(df_to_normalize), columns=cols_to_normalize)
    DataFrame[cols_to_normalize] = demo_df_normalized
    demo_df.to_csv("normalized_demog.csv", index=False)

# Add function to find missing values in column of a dataset 
def missing_val_per_col(DataFrame):
    for column in DataFrame:
    mis_values = DataFrame[column].isna().sum()
    if mis_values > 0:
        print(f'Column "{column}" has {mis_values} missing value(s)')

 # Add function to merge two datasets
 # We may want to structure it such that function can pass two datasets without file paths also
 def merge_datasets(file_path_1, file_path_2, col_left_on, col_right_on):
    df_file_1 = pd.read_csv(file_path_1)
    df_file_2 = pd.read_csv(file_path_2)
    merged_df = df_file_1(df_file_2, left_on = col_left_on, right_on = col_right_on)
    return merged_df

#Now time to normalise all columns needed for analysis and saving in new csv file
#cols_to_normalize = ha_df.columns[5:]
#ha_df_to_normalize = ha_df[cols_to_normalize] 
#scaler = StandardScaler()
#ha_df_normalized = pd.DataFrame(scaler.fit_transform(ha_df_to_normalize), columns = cols_to_normalize)
#ha_df[cols_to_normalize] = ha_df_normalized

    