

from Data_preparation import *

#Focus crashes:
pd.set_option('display.max_rows', None)
focus_factors = np.array(df['CONTRIBUTING FACTOR VEHICLE 1'].value_counts().head(25).index)
focus_factors.remove('unspecified')

df = df[df['CONTRIBUTING FACTOR VEHICLE 1'].isin(focus_factors)]

#Setting the order of the weekdays and sorting data
df['WEEKDAY'] = df['CRASH DATE'].dt.weekday
#week_order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
#df['WEEKDAY'] = pd.Categorical(df.WEEKDAY,categories=week_order)
#df = df.sort_values('WEEKDAY')
per_week = df['WEEKDAY'].value_counts()
weekday_factors = df.groupby(['WEEKDAY', 'CONTRIBUTING FACTOR VEHICLE 1']).size().unstack()


#%% Barplot of crash types per weekdays for vehicle 1:
plt.figure(figsize=(10, 6))  # Adjust the figure size if needed

week_order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

num_rows = 8
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

plt.savefig('crashfactors per weekday.png')
plt.show()


#%% Barplot per weekday
plt.figure(figsize=(10, 6))  # Adjust the figure size if needed

# Create bar chart
plt.bar(per_week.index, per_week.values, color='skyblue')

plt.xlabel('Year')
plt.ylabel('Count')
plt.title('Crashes per year')
plt.xticks(week_order)

plt.savefig('\Databehandling\Crashes_per_year.png', bbox_inches='tight')

plt.show()


#%% Create bar chart
plt.bar(per_week.index, per_week.values, color='skyblue')

plt.xlabel('Week')
plt.ylabel('Count')
plt.title('Crashes per weekdays')
plt.xticks(per_week.index)

plt.savefig('\Databehandling\Crashes_per_year.png', bbox_inches='tight')

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

plt.savefig('\Databehandling\Crashes_per_year.png', bbox_inches='tight')

plt.show()









# %%
