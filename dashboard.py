import textblob as tb
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import csv
# How many cities are there?
# How many restaurants have Table option
# How many has the option of online delivery via their own app
# Scatter chart of Aggregate rating
# Bar chart of Text Rating
# Exit
df= pd.read_csv('zomato.csv',  encoding='iso-8859-1', nrows=1000, on_bad_lines = 'warn')
groups=df.groupby(by='City')
print(len(groups.groups.keys()))


val=df[df['Has Table booking']=='Yes']
print(val['City'].count())


val_online=df[df['Has Online delivery']=='Yes']
print(val_online['City'].count())


ratings=list(df['Aggregate rating'])
x = np.random.normal(min(ratings), max(ratings), len(ratings))
plt.scatter(x, ratings)
plt.savefig("scatter_sentiment_analysis.pdf")
plt.show()


count_ratings=list(df['Rating text'])
Excellent=(count_ratings.count('Excellent'))
Very_good=(count_ratings.count('Very Good'))
Average=(count_ratings.count('Average'))
Good=(count_ratings.count('Good'))
Poor=(count_ratings.count('Poor'))
x=['Poor','Average', 'Good', 'Very Good',  'Excellent']
y=[Poor,  Average,Good, Very_good, Excellent]
plt.bar(x,y)
plt.savefig("bar_sentiment_analysis.pdf")
plt.show()
