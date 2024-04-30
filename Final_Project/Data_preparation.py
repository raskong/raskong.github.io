
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv('/Users/rasmuskongsted/Documents/Danmarks Tekniske Universitet/DTU/10. semester/Dataanalyse/Gitpage/raskong.github.io/Final_Project/Motor_Vehicle_Collisions_-_Crashes_20240409.csv')

#Dropping NaN for location:
#df = df.dropna(subset=['LOCATION'])
#df = df.reset_index(drop=True)

#Drpping latitude and longitude as they are the same as location:
#df = df.drop(['LATITUDE', 'LONGITUDE'], axis=1)

# %% Changing dtype of columns:
# Date
df['CRASH DATE'] = pd.to_datetime(df['CRASH DATE'])
df = df.sort_values(by='CRASH DATE')
#df.dtypes

# changing all cells with strings to lowercase:
df = df.map(lambda x: x.lower() if isinstance(x, str) else x)

#Removing years 2012 and 2024
df['YEAR'] = df['CRASH DATE'].dt.year
df = df[(df['YEAR'] != 2012) & (df['YEAR'] != 2024)]



#%% Sort ou











# %%
