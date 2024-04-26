
import pandas as pd
import numpy as np


df = pd.read_csv('/work/Motor_Vehicle_Collisions_-_Crashes_20240409.csv')




#Changing all strings to lower case:
df = df.map(lambda x: x.lower() if isinstance(x, str) else x)

