from Data_preparation import *
from Final_Project.focus_factors import *


# %%#%%Car type counts:
df.loc[df['VEHICLE TYPE CODE 1'] == 'sport utility / station wagon', 'VEHICLE TYPE CODE 1'] = 'station wagon/sport utility vehicle'
focus_vehicles = df['VEHICLE TYPE CODE 1'].value_counts().head(13).index
counts_vehicle = df['VEHICLE TYPE CODE 1'].value_counts().head(13)

plt.bar(counts_vehicle.index, counts_vehicle)
#plt.yscale('log')

# Label the axes
plt.xlabel('Focus factor')
plt.xticks(rotation = 90)
plt.ylabel('Count')

plt.savefig('/Users/rasmuskongsted/Documents/Danmarks Tekniske Universitet/DTU/10. semester/Dataanalyse/Gitpage/raskong.github.io/Final_Project/figures/cartype_counts.png')
# Show the plot
plt.show()


#%%
df['VEHICLE TYPE CODE 1'].value_counts().head(13)


#%%One-out-of-K coding for vehicle type:
classLabels = df[:, -1]
classNames = np.unique(classLabels)
classDict = dict(zip(classNames, range(len(classNames))))
origin = np.array([classDict[cl] for cl in classLabels])
K = origin.max()+1
origin_encoding = np.zeros((origin.size, K))
origin_encoding[np.arange(origin.size), origin] = 1




