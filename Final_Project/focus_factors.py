
from bokeh.plotting import *
from bokeh.models import *
from bokeh.io import output_file, show
import seaborn as sns
import matplotlib.pyplot as plt

from Data_preparation import *

#%%Creating focus crashes df:
focus_factors = np.array(df['CONTRIBUTING FACTOR VEHICLE 1'].value_counts().head(21).index)
#focus_factors = np.delete(focus_factors, np.where(focus_factors == 'unspecified')[0])

df = df[df['CONTRIBUTING FACTOR VEHICLE 1'].isin(focus_factors)]


#%%Focus counts:
counts = df['CONTRIBUTING FACTOR VEHICLE 1'].value_counts().head(21)

plt.figure(figsize=(8, 5))
plt.bar(counts.index, counts, color='salmon')
#plt.yscale('log')

# Label the axes
plt.xlabel('Focus factor')
plt.xticks(rotation = 90)
plt.ylabel('Count')
plt.title('Counts per contributing factor for vehicle 1')
plt.savefig('/Users/rasmuskongsted/Documents/Danmarks Tekniske Universitet/DTU/10. semester/Dataanalyse/Gitpage/raskong.github.io/factor_counts.png', bbox_inches='tight')
# Show the plot
plt.show()



#%% Barplot of crash types per year for vehicle 1:
year_factors = df.groupby(['YEAR', 'CONTRIBUTING FACTOR VEHICLE 1']).size().unstack()

plt.figure(figsize=(8, 6))  # Adjust the figure size if needed

num_rows = 5
num_cols = 3
fig, axes = plt.subplots(nrows=num_rows, ncols=num_cols, figsize=(12, 18),sharex=True)

fig.suptitle('Occurrences per year for Focus Factors (2013-2023)', fontsize=16)

for i, crash in enumerate(year_factors.columns):
    row_index = i // num_cols
    col_index = i % num_cols
    
    axes[row_index, col_index].bar(year_factors.index, year_factors[crash], color='pink')
    axes[row_index, 0].set_ylabel('Occurrences')
    axes[row_index, col_index].set_title(f'{crash}', fontsize=12)
    axes[row_index, col_index].tick_params(axis='x', rotation=90)

fig.text(0.5, -0.01, 'Years', size=12, ha='center')
plt.tight_layout(rect=[0, 0, 1, 0.96])

plt.savefig('/Users/rasmuskongsted/Documents/Danmarks Tekniske Universitet/DTU/10. semester/Dataanalyse/Gitpage/raskong.github.io/Final_Project/figures/crashfactors per year.png', bbox_inches='tight')
plt.show()


#%% Barplot of crash types per weekdays for vehicle 1:
df['WEEKDAY'] = df['CRASH DATE'].dt.weekday
weekday_factors = df.groupby(['WEEKDAY', 'CONTRIBUTING FACTOR VEHICLE 1']).size().unstack()

plt.figure(figsize=(8, 6))  # Adjust the figure size if needed

week_order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

num_rows = 5
num_cols = 3
fig, axes = plt.subplots(nrows=num_rows, ncols=num_cols, figsize=(12, 18),sharex=True)

fig.suptitle('Occurrences per weekday for Focus Factors (2013-2023)', fontsize=16)

for i, crash in enumerate(weekday_factors.columns):
    row_index = i // num_cols
    col_index = i % num_cols
    
    axes[row_index, col_index].bar(week_order, weekday_factors[crash], color='skyblue')
    axes[row_index, 0].set_ylabel('Occurrences')
    axes[row_index, col_index].set_title(f'{crash}', fontsize=12)
    axes[row_index, col_index].tick_params(axis='x', rotation=90)

fig.text(0.5, -0.01, 'Weekdays', size=12, ha='center')
plt.tight_layout(rect=[0, 0, 1, 0.96])

plt.savefig('/Users/rasmuskongsted/Documents/Danmarks Tekniske Universitet/DTU/10. semester/Dataanalyse/Gitpage/raskong.github.io/Final_Project/figures/crashfactors per weekday.png', bbox_inches='tight')
plt.show()




#%% Barplot per month per focus factor
df = df[df['CONTRIBUTING FACTOR VEHICLE 1'] != 'unspecified']
df['MONTH'] = df['CRASH DATE'].dt.month
month_factors = df.groupby(['MONTH', 'CONTRIBUTING FACTOR VEHICLE 1']).size().unstack()

import calendar

num_rows = 5
num_cols = 4
fig, axes = plt.subplots(nrows=num_rows, ncols=num_cols, figsize=(12, 18),sharex=True)

fig.suptitle('Occurrences per month for Focus Factors (2013-2023)', fontsize=16)

for i, crime in enumerate(month_factors.columns):
    row_index = i // num_cols
    col_index = i % num_cols
    
    axes[row_index, col_index].bar(month_factors.index, month_factors[crime], color='skyblue')
    axes[row_index, 0].set_ylabel('Occurrences')
    axes[row_index, col_index].set_title(f'{crime}', fontsize=12)
    axes[row_index, col_index].tick_params(axis='x', rotation=90)
    axes[row_index, col_index].set_xticks(range(1, 13))
    axes[row_index, col_index].set_xticklabels([calendar.month_abbr[i] for i in range(1, 13)])
  
fig.text(0.5, -0.01, 'Months', size=12, ha='center')
plt.tight_layout(rect=[0, 0, 1, 0.96])

plt.savefig('/Users/rasmuskongsted/Documents/Danmarks Tekniske Universitet/DTU/10. semester/Dataanalyse/Gitpage/raskong.github.io/Final_Project/figures/crashfactors per month.png', bbox_inches='tight')
plt.show()

#%%Barplot per hour of day per focus factor
df = df[df['CONTRIBUTING FACTOR VEHICLE 1'] != 'unspecified']
df['CRASH TIME'] = pd.to_datetime(df['CRASH TIME'], format='%H:%M')
df['CRASH HOUR'] = df['CRASH TIME'].dt.hour
hour_factors = df.groupby(['CRASH HOUR', 'CONTRIBUTING FACTOR VEHICLE 1']).size().unstack()

num_rows = 5
num_cols = 4
fig, axes = plt.subplots(nrows=num_rows, ncols=num_cols, figsize=(12, 18),sharex=True)

fig.suptitle('Occurrences per hour of the day for Focus Factors (2013-2023)', fontsize=16)

for i, crime in enumerate(hour_factors.columns):
    row_index = i // num_cols
    col_index = i % num_cols
    
    axes[row_index, col_index].bar(hour_factors.index, hour_factors[crime], color='skyblue')
    axes[row_index, 0].set_ylabel('Occurrences')
    axes[row_index, col_index].set_title(f'{crime}', fontsize=12)  

fig.text(0.5, -0.01, 'Hours of the day', size=12, ha='center')
plt.tight_layout(rect=[0, 0, 1, 0.96])

plt.savefig('/Users/rasmuskongsted/Documents/Danmarks Tekniske Universitet/DTU/10. semester/Dataanalyse/Gitpage/raskong.github.io/Final_Project/Figures/crashfactors per hour.png', bbox_inches='tight')
plt.show()

#%% Barplot per weekday
per_week = df['WEEKDAY'].value_counts()
plt.figure(figsize=(10, 6))  # Adjust the figure size if needed

# Create bar chart
plt.bar(per_week.index, per_week.values, color='skyblue')

plt.xlabel('Weekday')
plt.ylabel('Count')
plt.title('Crashes per year')
#plt.xticks(week_order)

plt.savefig('/Users/rasmuskongsted/Documents/Danmarks Tekniske Universitet/DTU/10. semester/Dataanalyse/Gitpage/raskong.github.io/Final_Project/figures/crashfactors per weekday.png', bbox_inches='tight')

plt.show()


#%% Create bar chart
plt.bar(per_week.index, per_week.values, color='skyblue')

plt.xlabel('Week')
plt.ylabel('Count')
plt.title('Crashes per weekdays')
plt.xticks(per_week.index)

plt.savefig('/Users/rasmuskongsted/Documents/Danmarks Tekniske Universitet/DTU/10. semester/Dataanalyse/Gitpage/raskong.github.io/Final_Project/figures\Crashes_per_week.png', bbox_inches='tight')

plt.show()




#%% Bar plot per year
per_year = df['YEAR'].value_counts().sort_index()

plt.figure(figsize=(10, 6))  # Adjust the figure size if needed

# Create bar chart
plt.bar(per_year.index, per_year.values, color='skyblue')

plt.xlabel('Year')
plt.ylabel('Count')
plt.title('Crashes per year')
plt.xticks(per_year.index)

plt.savefig('/Users/rasmuskongsted/Documents/Danmarks Tekniske Universitet/DTU/10. semester/Dataanalyse/Gitpage/raskong.github.io/Final_Project/Figures/crashes_per_year.png', bbox_inches='tight')

plt.show()



#%% Bokeh for weekdays
#Normalizing data for easy comparison
normalized_crimes = weekday_factors.div(weekday_factors.sum(axis=0), axis=1)
normalized_crimes.index = normalized_crimes.index.astype(str)

output_notebook()
#df_bokeh = ColumnDataSource(normalized_crimes)
df_bokeh = ColumnDataSource(weekday_factors)

weekdays = [str(i) for i in range(7)]
colors = sns.color_palette("husl", len(focus_factors))
colors = ['#%02x%02x%02x' % (int(r * 255), int(g * 255), int(b * 255)) for r, g, b in colors]

p = figure(x_range = FactorRange(factors=weekdays), title="Crimes per weekday (Normalized values)", x_axis_label='Weekday', y_axis_label='Crashes', height=400, width=700) 
#p.xaxis.ticker = range(len(week_order))
#p.xaxis.major_label_overrides = {i: name for i, name in enumerate(week_order)}

k = 0

bar ={}
items = []
for indx,i in enumerate(focus_factors):
    bar[i] = p.vbar(x='WEEKDAY',  top=i, source = df_bokeh, width=0.6,
                      muted_alpha=0.05, muted = True, fill_color = colors[indx])

     ### for the custom legend // you need to figure out where to add it
    items.append((i, [bar[i]])) ### figure where to add it
    legend = Legend(items=items, location=(0, 0)) ## figure where to add it


p.add_layout(legend, 'left')
p.legend.click_policy="mute" ### assigns the click policy (you can try to use ''hide'


output_file('/Users/rasmuskongsted/Documents/Danmarks Tekniske Universitet/DTU/10. semester/Dataanalyse/Gitpage/raskong.github.io/bokeh_weekday.html')
show(p) #displays your plot


year_factors.drop(columns=['unspecified'], inplace=True)
focus_factors = focus_factors[focus_factors != 'unspecified']
#%% Bokeh year not normalized

output_notebook()
normalized_crashes = year_factors.div(year_factors.sum(axis=0), axis=1)
normalized_crashes.index = normalized_crashes.index.astype(str)

year_factors.index = year_factors.index.astype(str)

#df_bokeh = ColumnDataSource(normalized_crashes)
df_bokeh = ColumnDataSource(year_factors)

years = [str(2013 + i) for i in range(11)]
colors = sns.color_palette("husl", len(focus_factors))
colors = ['#%02x%02x%02x' % (int(r * 255), int(g * 255), int(b * 255)) for r, g, b in colors]

p = figure(x_range = FactorRange(factors=years), title="Crashes per year according to contributing factor for vehicle 1", x_axis_label='Year', y_axis_label='Crashes', height=400, width=700) 
k = 0

bar ={}
items = []
for indx,i in enumerate(focus_factors):
    bar[i] = p.vbar(x='YEAR',  top=i, source = df_bokeh, width=0.7,
                      muted_alpha=0.05, muted = True, fill_color = colors[indx])

     ### for the custom legend // you need to figure out where to add it
    items.append((i, [bar[i]])) ### figure where to add it
    legend = Legend(items=items, location=(0, 0)) ## figure where to add it


p.add_layout(legend, 'left')
p.legend.click_policy="mute" ### assigns the click policy (you can try to use ''hide'


output_file('/Users/rasmuskongsted/Documents/Danmarks Tekniske Universitet/DTU/10. semester/Dataanalyse/Gitpage/raskong.github.io/Final_Project/Figures/bokeh_year_factors.html')
show(p) #displays your plot

#%% Bokeh year normalized
output_notebook()
normalized_crashes = year_factors.div(year_factors.sum(axis=0), axis=1)
normalized_crashes.index = normalized_crashes.index.astype(str)

year_factors.index = year_factors.index.astype(str)

df_bokeh = ColumnDataSource(normalized_crashes)
#df_bokeh = ColumnDataSource(year_factors)

years = [str(2013 + i) for i in range(11)]
colors = sns.color_palette("husl", len(focus_factors))
colors = ['#%02x%02x%02x' % (int(r * 255), int(g * 255), int(b * 255)) for r, g, b in colors]

p = figure(x_range = FactorRange(factors=years), title="Crashes per year", x_axis_label='Year', y_axis_label='Crashes', height=400, width=700) 
k = 0

bar ={}
items = []
for indx,i in enumerate(focus_factors):
    bar[i] = p.vbar(x='YEAR',  top=i, source = df_bokeh, width=0.7,
                      muted_alpha=0.05, muted = True, fill_color = colors[indx])

     ### for the custom legend // you need to figure out where to add it
    items.append((i, [bar[i]])) ### figure where to add it
    legend = Legend(items=items, location=(0, 0)) ## figure where to add it


p.add_layout(legend, 'left')
p.legend.click_policy="mute" ### assigns the click policy (you can try to use ''hide'


output_file('/Users/rasmuskongsted/Documents/Danmarks Tekniske Universitet/DTU/10. semester/Dataanalyse/Gitpage/raskong.github.io/Final_Project/Figures/bokeh_year_norm.html')
show(p) #displays your plot


# %%#%%Car type counts:
df.loc[df['VEHICLE TYPE CODE 1'] == 'sport utility / station wagon', 'VEHICLE TYPE CODE 1'] = 'station wagon/sport utility vehicle'
focus_vehicles = df['VEHICLE TYPE CODE 1'].value_counts().head(10).index
counts_vehicle = df['VEHICLE TYPE CODE 1'].value_counts().head(10)

plt.bar(counts_vehicle.index, counts_vehicle)
#plt.yscale('log')

# Label the axes
plt.xlabel('Focus factor')
plt.xticks(rotation = 90)
plt.ylabel('Count')

plt.savefig('/Users/rasmuskongsted/Documents/Danmarks Tekniske Universitet/DTU/10. semester/Dataanalyse/Gitpage/raskong.github.io/Final_Project/figures/cartype_counts.png')
# Show the plot
plt.show()



# %%#%%Car type counts:
df.loc[df['VEHICLE TYPE CODE 1'] == 'sport utility / station wagon', 'VEHICLE TYPE CODE 1'] = 'station wagon/sport utility vehicle'
focus_vehicles = df['VEHICLE TYPE CODE 1'].value_counts().head(10).index
counts_vehicle = df['VEHICLE TYPE CODE 1'].value_counts().head(10)

plt.bar(counts_vehicle.index, counts_vehicle)
#plt.yscale('log')

# Label the axes
plt.xlabel('Focus factor')
plt.xticks(rotation = 90)
plt.ylabel('Count')

plt.savefig('/Users/rasmuskongsted/Documents/Danmarks Tekniske Universitet/DTU/10. semester/Dataanalyse/Gitpage/raskong.github.io/Final_Project/figures/cartype_counts.png')
# Show the plot
plt.show()


#%%killed per car
#sedan
sedan = df[df['VEHICLE TYPE CODE 1']=='sedan']
sedan['NUMBER OF PERSONS KILLED'].mean()

#station wagon
station_wagon = df[df['VEHICLE TYPE CODE 1']=='station wagon/sport utility vehicle']
station_wagon['NUMBER OF PERSONS KILLED'].mean()

#passenger vehicle
passenger_vehicle = df[df['VEHICLE TYPE CODE 1']=='passenger vehicle']
passenger_vehicle['NUMBER OF PERSONS KILLED'].mean()

#bus
bus = df[df['VEHICLE TYPE CODE 1']=='bus']
bus['NUMBER OF PERSONS KILLED'].mean()

#pick-up truck
pick_up = df[df['VEHICLE TYPE CODE 1']=='pick-up truck']
pick_up['NUMBER OF PERSONS KILLED'].mean()



#%% Injured per car
sedan = df[df['VEHICLE TYPE CODE 1']=='sedan']
sedan['NUMBER OF PEDESTRIANS INJURED'].mean()

#station wagon
station_wagon = df[df['VEHICLE TYPE CODE 1']=='station wagon/sport utility vehicle']
station_wagon['NUMBER OF PEDESTRIANS INJURED'].mean()

#passenger vehicle
passenger_vehicle = df[df['VEHICLE TYPE CODE 1']=='passenger vehicle']
passenger_vehicle['NUMBER OF PEDESTRIANS INJURED'].mean()

#bus
bus = df[df['VEHICLE TYPE CODE 1']=='bus']
bus['NUMBER OF PEDESTRIANS INJURED'].mean()

#pick-up truck
pick_up = df[df['VEHICLE TYPE CODE 1']=='pick-up truck']
pick_up['NUMBER OF PEDESTRIANS INJURED'].mean()



