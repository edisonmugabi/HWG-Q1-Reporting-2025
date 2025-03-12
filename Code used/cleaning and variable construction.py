import pandas as pd
import numpy as np
#reading the agriculture one file from the system
agric1_training=pd.read_csv(r"C:\Users\Edison New\Desktop\HWG Q1 Reporting 2025\Raw data sets from the app\check2 hWG Q1 files\Agriculture one training.csv")

#reading the census data
census_2025= pd.read_excel(r"C:\Users\Edison New\Desktop\HWG Q1 Reporting 2025\Raw data sets from the app\check2 hWG Q1 files\HWG Data request (1).xlsx")

# filtering kitagwenda and rakai districts
agric1_train=agric1_training[agric1_training['district_name'].isin(['Kitagwenda','Rakai'])]

census_2025.columns
census_villages=census_2025['village'].unique()
training_village=agric1_training['village_name'].unique()
Missing_village=[village for village in census_villages if village not in training_village]
print(Missing_village)
