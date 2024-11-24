import pandas as pd
import numpy as np
import scipy.stats as stats
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv('russian_demography.csv')
print(data.head())
print(data.isnull().sum())
data_clean = data.dropna(subset=['birth_rate', 'region'])
anova_result = stats.f_oneway(*(data_clean[data_clean['region'] == region]['birth_rate'].values
                                for region in data_clean['region'].unique()))
print('ANOVA Test Result:', anova_result)
plt.figure(figsize=(12, 6))
sns.boxplot(data=data_clean, x='region', y='birth_rate')
plt.xticks(rotation=90)
plt.title('Boxplot of Birth Rates by Region')
plt.xlabel('Region')
plt.ylabel('Birth Rate')
plt.show()
if anova_result.pvalue < 0.05:
    print("There is a significant difference in the mean birth rates between regions.")
else:
    print("There is no significant difference in the mean birth rates between regions.")
