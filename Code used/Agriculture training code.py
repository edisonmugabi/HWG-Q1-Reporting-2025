import pandas as pd
import numpy as np

## Agriculture one training Analysis

#reading the agriculture one file from the system
agric1_training=pd.read_csv(r"C:\Users\Edison New\Desktop\HWG Q1 Reporting 2025\Raw data sets from the app\check2 hWG Q1 files\Agriculture one training.csv")

#reading the census data
census_2025= pd.read_excel(r"C:\Users\Edison New\Desktop\HWG Q1 Reporting 2025\Raw data sets from the app\check2 hWG Q1 files\HWG Data request (1).xlsx")

# filtering kitagwenda and rakai districts
agric1_train=agric1_training[agric1_training['district_name'].isin(['Kitagwenda','Rakai'])]
agric1_train['village_name']=agric1_train['village_name'].str.strip().str.lower()

census_2025.columns
census_villages=census_2025['village'].unique()
census_villages=[str(v).strip().lower() for v in census_villages]
training_village=agric1_training['village_name'].unique()
training_village=[str(v).strip().lower() for v in training_village]
Missing_village=[village for village in census_villages if village not in training_village]
if Missing_village:
 print("Missing_village:",Missing_village)
Agric1_training_clean=agric1_train[agric1_train['village_name'].isin(census_villages)]
Agric1_training_clean=Agric1_training_clean.drop_duplicates(subset=["household_id"])

Agric1_training_clean.shape

## Agriculture preparation and preplanting day 1 cleaning

# reading the data for Agriculture 2 day 1 training(preparation and preplanting)
agric2_training1=pd.read_csv(r"C:\Users\Edison New\Desktop\HWG Q1 Reporting 2025\Raw data sets from the app\check2 hWG Q1 files\Agric preparation and preplanting training day1.csv")
agric2_training1['village_name']=agric2_training1['village_name'].str.strip().str.lower()
# filtering the kitagwenda and Rakai districts in the traing report
agric2_training1=agric2_training1[agric2_training1['district_name'].isin(['Kitagwenda','Rakai'])]

# selecting villages in the agric2 day1 preparation and preplanting
agric2_training1_villages=agric2_training1['village_name'].unique()
agric2_training1_villages=[str(v).strip().lower() for v in agric2_training1_villages]

# checking whether they exist in census villages
Missing_village_agric2_day1=[village for village in census_villages if village not in agric2_training1_villages]
if Missing_village_agric2_day1:
   print("Missing_village_agric2_day1",Missing_village_agric2_day1)

# generating the clean file for preparation and preplanting training day#1
agric2_day1_clean=agric2_training1[agric2_training1['village_name'].isin(census_villages)]
agric2_day1_clean=agric2_day1_clean.drop_duplicates(subset=["household_id"])
agric2_day1_clean.shape


## Agriculture training  day#2 preparation and preplanting
 
 # reading the data for preparation and preplanting
agric2_training2=pd.read_csv(r"C:\Users\Edison New\Desktop\HWG Q1 Reporting 2025\Raw data sets from the app\check2 hWG Q1 files\Agric preparation and preplanting training day2.csv")
agric2_training2=agric2_training2[agric2_training2['district_name'].isin(['Kitagwenda','Rakai'])]
agric2_training2['village_name']=agric2_training2['village_name'].str.strip().str.lower()
# filtering the villages for agric2 training day#2
agric2_day2_villages=agric2_training2['village_name'].unique()
agric2_day2_villages=[str(v).strip().lower() for v in agric2_day2_villages]
missing_village=[village for village in census_villages if village not in agric2_day2_villages]
if missing_village:
 print("Missing_village",missing_village)
agric2_training2_clean=agric2_training2[agric2_training2['village_name'].isin(census_villages)]
agric2_training2_clean=agric2_training2_clean.drop_duplicates(subset="household_id")
agric2_training2_clean.shape

## merging data for agriculture training 1 and agriculture two trainings day 1 and day 2
Agriculture_clean_data = pd.concat([Agric1_training_clean, agric2_day1_clean, agric2_training2_clean])                                  
Agriculture_clean_data['type'].unique()

#exporting the clean merged file
output_path = r"C:\Users\Edison New\Desktop\HWG Q1 Reporting 2025\Datasetsets shared\Agriculture_clean_data.csv"
Agriculture_clean_data.to_csv(output_path, index=False)