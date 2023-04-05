import json
import random
import pyarrow as pa
import pyarrow.parquet as pq

import pandas as pd

commerce_data_csv_path = "annual-enterprise-survey-2021-financial-year-provisional-csv.csv"
commerce_data_csv_data = pd.read_csv(filepath_or_buffer=commerce_data_csv_path,encoding="unicode_escape",nrows=1000)

#printing columns
print(commerce_data_csv_data.columns)

#printing data
print(commerce_data_csv_data)

#printing data types of csv
print(commerce_data_csv_data.dtypes)

#change the data type from automatic to proper
commerce_data_csv_data = commerce_data_csv_data.convert_dtypes()
#printing data types again
print(commerce_data_csv_data.dtypes)

#load json
commerce_data_path_json = "datajson.txt"
commerce_data_json_df = pd.read_json(commerce_data_path_json,encoding="unicode_escape")
print(len(commerce_data_csv_data)+len(commerce_data_json_df))

#appned and check length
commerce_csv_and_json_appended_df = pd.concat([commerce_data_csv_data,commerce_data_json_df])
print(len(commerce_csv_and_json_appended_df))
print(commerce_csv_and_json_appended_df)

#printing different ways
print(commerce_csv_and_json_appended_df.head(10))

#Merging two dataframes
yearwise_inflation_data = '{"Year": [2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021], "Inflation_Rate": [7.73, 5.72, 5.31, 6.98, 7.56, 5.51, 6.33, 6.42, 4.82, 8.0]}'
inflation_data_json_df = pd.read_json(yearwise_inflation_data)
commerce_csv_and_json_appended_df = commerce_csv_and_json_appended_df.merge(inflation_data_json_df,on="Year")
print(commerce_csv_and_json_appended_df.columns)

#dropping columns from the dataframe
commerce_csv_and_json_appended_df=commerce_csv_and_json_appended_df.drop(["Industry_code_NZSIOC","Variable_code"],axis="columns")
print(commerce_csv_and_json_appended_df.columns)



#Normalization in pandas
data = {'A': [10, 20, 30, 40], 'B': [100, 200, 300, 400], 'C': [1000, 2000, 3000, 4000]}
df = pd.DataFrame(data)

# display the original DataFrame
print('Original DataFrame:')
print(df)

# perform min-max normalization on column A
df['A_normalized'] = (df['A'] - df['A'].min()) / (df['A'].max() - df['A'].min())

# perform z-score normalization on column B
df['B_normalized'] = (df['B'] - df['B'].mean()) / df['B'].std()

# perform decimal scaling normalization on column C
df['C_normalized'] = df['C'] / 1000

# display the normalized DataFrame
print('Normalized DataFrame:')
print(df)

#using lambda function in dataframes to apply to columns
commerce_csv_and_json_appended_df["Inflation_Rate"] = commerce_csv_and_json_appended_df["Inflation_Rate"].apply(lambda s:s*1.15)
print(commerce_csv_and_json_appended_df.tail(10))

#Pivoting the dataframe# create a sample DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie', 'Dave', 'Emily', 'Frank'],
        'Gender': ['Female', 'Male', 'Male', 'Male', 'Female', 'Male'],
        'Age': [25, 30, 35, 40, 45, 50],
        'Salary': [50000, 60000, 70000, 80000, 90000, 100000]}
df = pd.DataFrame(data)

# create a pivot table that groups data by 'Gender' and 'Age' columns
# and computes the mean of the 'Salary' column
pivot_table = df.pivot_table(index='Gender', columns='Age', values='Salary', aggfunc='mean',fill_value=0)

# filter the pivot table to include only 'Female' and 'Male' rows
filtered_pivot_table = pivot_table.loc[['Female', 'Male']]
print(filtered_pivot_table)

#Storing data frame in parquet files and reading from it

commerce_csv_and_json_appended_df.to_parquet("example.parquet", compression='snappy', row_group_size=10000)

read_dataframe = pd.read_parquet("example.parquet")
print(read_dataframe.tail(10))

#melting of the dataframe
commerce_csv_and_json_appended_df = pd.concat([commerce_data_csv_data,commerce_data_json_df])
print(commerce_csv_and_json_appended_df)
melted_commerce_csv_and_json_appended_df = commerce_csv_and_json_appended_df.melt(id_vars=["Variable_code"])
print(melted_commerce_csv_and_json_appended_df)

#normalizing dataframes from nested JSONs

json_obj = {
"Year":"2012",
"Industry_aggregation_NZSIOC":"Level 2",
"Industry_code_NZSIOC":"BA11",
"Industry_name_NZSIOC":"Cotton and Silk farming",
"Units":"Dollars (millions)",
"Variable":{
"code":"H12",
"name":"Equipments and others",
"category":"Financial performance",
},
"Value":"2,970",
"Industry_code_ANZSIC06":"ANZSIC06 groups B011, B012, and B013"
}
json_df_raw = pd.DataFrame.from_dict(json_obj)
print("Printing raw json")
print(json_df_raw)
print(json_df_raw.dtypes)
json_df_normalized = pd.json_normalize(json_obj)
print("Printing normalized json")
print(json_df_normalized)
print(json_df_normalized.dtypes)
