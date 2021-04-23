import pandas as pd
from pandas import DataFrame
import datetime
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

crop_data = pd.read_csv('data/actual_crop_data.csv')

sns.barplot(data=crop_data, x='year', y='acre_planted')
plt.show()
sns.barplot(data=crop_data, x='year', y='acre_harvested')
plt.show()
sns.barplot(data=crop_data, x='year', y='acres_loss')
plt.show()
sns.barplot(data=crop_data, x='year', y='yield_lb_per_acres')

plt.show()