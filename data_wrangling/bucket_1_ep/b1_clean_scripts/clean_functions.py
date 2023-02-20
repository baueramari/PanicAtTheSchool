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

    