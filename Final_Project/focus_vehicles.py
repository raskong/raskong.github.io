from Data_preparation import *
from Exploratory import *


# %%#%%Car type counts:
df.loc[df['VEHICLE TYPE CODE 1'] == 'sport utility / station wagon', 'VEHICLE TYPE CODE 1'] = 'station wagon/sport utility vehicle'
focus_vehicles = df['VEHICLE TYPE CODE 1'].value_counts().head(15).index
focus_vehicles = focus_vehicles[focus_vehicles != '4 dr sedan']
df = df[df['VEHICLE TYPE CODE 1'].isin(focus_vehicles)]
counts_vehicle = df['VEHICLE TYPE CODE 1'].value_counts().head(15)



#%%Cartype counts
plt.figure(figsize=(10, 6))
plt.bar(counts_vehicle.index, counts_vehicle)
#plt.yscale('log')


# Label the axes
plt.xlabel('Vehicle type')
plt.xticks(rotation = 90)
plt.ylabel('Count')
plt.title('Counts of crashes per vehicle type 1')
plt.savefig('/Users/rasmuskongsted/Documents/Danmarks Tekniske Universitet/DTU/10. semester/Dataanalyse/Gitpage/raskong.github.io/Final_Project/figures/cartype_counts.png', bbox_inches='tight')
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
