import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

crop_data = pd.read_csv('data/actual_crop_data.csv')
crop_data = crop_data[(crop_data['county_name'] == 'ARKANSAS') & (crop_data['year'] > 2000)]

# ax = sns.lineplot(data=crop_data, x='year', y='production_cwt', markers=True)
# ax.set(xticks=crop_data.year)

# plt.show()

# ax = sns.lineplot(data=crop_data, x='year', y='acre_harvested', markers=True)
# ax.set(xticks=crop_data.year)
# plt.show()

# ax = sns.lineplot(data=crop_data, x='year', y='acres_loss', markers=True)
# ax.set(xticks=crop_data.year)
# plt.show()

# ax = sns.barplot(data=crop_data, x='year', y='acres_loss')
# plt.show()

crop_data['yield_lb_per_acres'].hist(bins=10)
plt.show()

# ax = sns.lineplot(data=crop_data, x='year', y='yield_lb_per_acres', markers=True)
# ax.set(xticks=crop_data.year)
# plt.show()

# ax = sns.lineplot(data=crop_data, x='year', y='production_cwt', markers=True)
# ax.set(xticks=crop_data.year)
# plt.show()
