from Data_preparation import *
from Exploratory import *


# %%#%%Car type counts:
df.loc[df['VEHICLE TYPE CODE 1'] == 'sport utility / station wagon', 'VEHICLE TYPE CODE 1'] = 'station wagon/sport utility vehicle'
focus_vehicles = df['VEHICLE TYPE CODE 1'].value_counts().head(18).index
focus_vehicles = focus_vehicles[focus_vehicles != '4 dr sedan']
focus_vehicles = focus_vehicles[focus_vehicles != 'other']
focus_vehicles = focus_vehicles[focus_vehicles != 'unknown']
df = df[df['VEHICLE TYPE CODE 1'].isin(focus_vehicles)]
counts_vehicle = df['VEHICLE TYPE CODE 1'].value_counts()

#%%Cartype counts
plt.figure(figsize=(10, 6))
plt.bar(counts_vehicle.index, counts_vehicle, color = 'salmon')
#plt.yscale('log')


# Label the axes
plt.xlabel('Vehicle type')
plt.xticks(rotation = 90)
plt.ylabel('Count')
plt.title('Counts of crashes per vehicle type 1')
plt.savefig('/Users/rasmuskongsted/Documents/Danmarks Tekniske Universitet/DTU/10. semester/Dataanalyse/Gitpage/raskong.github.io/cartype_counts.png', bbox_inches='tight')
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


df = df[df['VEHICLE TYPE CODE 1'].isin(focus_vehicles)]
weekday_vehicles = df.groupby(['WEEKDAY', 'VEHICLE TYPE CODE 1']).size().unstack()

#%%Bokeh per week norm
normalized_crashes = weekday_vehicles.div(weekday_vehicles.sum(axis=0), axis=1)
normalized_crashes.index = normalized_crashes.index.astype(str)

output_notebook()
df_bokeh = ColumnDataSource(normalized_crashes)
#df_bokeh = ColumnDataSource(weekday_vehicles)

weekdays = [str(i) for i in range(7)]
colors = sns.color_palette("husl", len(focus_vehicles))
colors = ['#%02x%02x%02x' % (int(r * 255), int(g * 255), int(b * 255)) for r, g, b in colors]

p = figure(x_range = FactorRange(factors=weekdays), title="Crashes per weekday - 2013 to 2023 (Normalized values)", x_axis_label='Weekday', y_axis_label='Crashes (Normalized)', height=400, width=700) 
k = 0

bar ={}
items = []
for indx,i in enumerate(focus_vehicles):
    bar[i] = p.vbar(x='WEEKDAY',  top=i, source = df_bokeh, width=0.7,
                      muted_alpha=0.05, muted = True, fill_color = colors[indx])

     ### for the custom legend // you need to figure out where to add it
    items.append((i, [bar[i]])) ### figure where to add it
    legend = Legend(items=items, location=(0, 0)) ## figure where to add it


p.add_layout(legend, 'left')
p.legend.click_policy="mute" ### assigns the click policy (you can try to use ''hide'


output_file('/Users/rasmuskongsted/Documents/Danmarks Tekniske Universitet/DTU/10. semester/Dataanalyse/Gitpage/raskong.github.io/Final_Project/Figures/bokeh_weekday_vehicles_norm.html')
show(p) #displays your plot





#%%Bokeh per year
year_vehicles = df.groupby(['YEAR', 'VEHICLE TYPE CODE 1']).size().unstack()


output_notebook()
#normalized_vehicles = year_vehicles.div(year_vehicles.sum(axis=0), axis=1)
#normalized_vehicles.index = normalized_vehicles.index.astype(str)

year_vehicles.index = year_vehicles.index.astype(str)

#df_bokeh = ColumnDataSource(normalized_vehicles)
df_bokeh = ColumnDataSource(year_vehicles)

years = [str(2013 + i) for i in range(11)]
colors = sns.color_palette("husl", len(focus_vehicles))
colors = ['#%02x%02x%02x' % (int(r * 255), int(g * 255), int(b * 255)) for r, g, b in colors]

p = figure(x_range = FactorRange(factors=years), title="Crashes per year for different vehicle types - 2013 to 2023", x_axis_label='Year', y_axis_label='Crashes', height=400, width=700) 
k = 0

bar ={}
items = []
for indx,i in enumerate(focus_vehicles):
    bar[i] = p.vbar(x='YEAR',  top=i, source = df_bokeh, width=0.7,
                      muted_alpha=0.05, muted = True, fill_color = colors[indx])

     ### for the custom legend // you need to figure out where to add it
    items.append((i, [bar[i]])) ### figure where to add it
    legend = Legend(items=items, location=(0, 0)) ## figure where to add it


p.add_layout(legend, 'left')
p.legend.click_policy="mute" ### assigns the click policy (you can try to use ''hide'


output_file('/Users/rasmuskongsted/Documents/Danmarks Tekniske Universitet/DTU/10. semester/Dataanalyse/Gitpage/raskong.github.io/Final_Project/Figures/bokeh_year_vehicles.html')
show(p) #displays your plot



# %%
hour_factors = df.groupby(['CRASH HOUR', 'VEHICLE TYPE CODE 1']).size().unstack()

num_rows = 5
num_cols = 3
fig, axes = plt.subplots(nrows=num_rows, ncols=num_cols, figsize=(12, 18),sharex=True)

fig.suptitle('Occurrences per hour of the day for Focus Vehicles (2013-2023)', fontsize=16)

for i, crime in enumerate(focus_vehicles):
    row_index = i // num_cols
    col_index = i % num_cols
    
    axes[row_index, col_index].bar(hour_factors.index, hour_factors[crime], color='salmon')
    axes[row_index, 0].set_ylabel('Occurrences')
    axes[row_index, col_index].set_title(f'{crime}', fontsize=12)  

fig.text(0.5, -0.01, 'Hours of the day', size=12, ha='center')
plt.tight_layout(rect=[0, 0, 1, 0.96])

plt.savefig('/Users/rasmuskongsted/Documents/Danmarks Tekniske Universitet/DTU/10. semester/Dataanalyse/Gitpage/raskong.github.io/Final_Project/Figures/vehicles per hour.png', bbox_inches='tight')
plt.show()


#%% Barplot of crash types per weekdays for vehicle 1:
df['WEEKDAY'] = df['CRASH DATE'].dt.weekday
weekday_factors = df.groupby(['WEEKDAY', 'VEHICLE TYPE CODE 1']).size().unstack()

plt.figure(figsize=(8, 6))  # Adjust the figure size if needed

week_order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

num_rows = 5
num_cols = 3
fig, axes = plt.subplots(nrows=num_rows, ncols=num_cols, figsize=(12, 18),sharex=True)

fig.suptitle('Occurrences per Weekday for Focus Vehicles (2013-2023)', fontsize=16)

for i, crash in enumerate(weekday_factors.columns):
    row_index = i // num_cols
    col_index = i % num_cols
    
    axes[row_index, col_index].bar(week_order, weekday_factors[crash], color='salmon')
    axes[row_index, 0].set_ylabel('Occurrences')
    axes[row_index, col_index].set_title(f'{crash}', fontsize=12)
    axes[row_index, col_index].tick_params(axis='x', rotation=90)

fig.text(0.5, -0.01, 'Weekdays', size=12, ha='center')
plt.tight_layout(rect=[0, 0, 1, 0.96])

plt.savefig('/Users/rasmuskongsted/Documents/Danmarks Tekniske Universitet/DTU/10. semester/Dataanalyse/Gitpage/raskong.github.io/Final_Project/figures/vehicles per weekday.png', bbox_inches='tight')
plt.show()

# %%
