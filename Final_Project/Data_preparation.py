
import pandas as pd
import numpy as np


df = pd.read_csv('/Users/rasmuskongsted/Documents/Danmarks Tekniske Universitet/DTU/10. semester/Dataanalyse/Gitpage/raskong.github.io/Final_Project/Motor_Vehicle_Collisions_-_Crashes_20240409.csv')




#Changing all strings to lower case:
df = df.map(lambda x: x.lower() if isinstance(x, str) else x)

#Removing 2012 and 2024
df['CRASH DATE'] = pd.to_datetime(df['CRASH DATE'])
df = df.sort_values(by='CRASH DATE')
df['YEAR'] = df['CRASH DATE'].dt.year
df = df[(df['YEAR'] != 2012) & (df['YEAR'] != 2024)]