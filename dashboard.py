import textblob as tb
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import csv
# How many cities are there?
# How many restaurants have Table option
# How many has online delivery
# Scatter chart of Aggregate rating
# Bar chart of Text Rating
# Exit

with open('zomato.csv', 'r', errors='ignore') as file:
    reader = csv.reader(file)
    row= []
    city= []
    resto= []
    online_del= []
    aggregrate_rating= []
    for row in reader:
        #city.append(row.city)
        city.append(row[0])
        resto.append(row[1])
        online_del.append(row[2])
        aggregrate_rating.append(row[3])
print(resto)
# START OF THE QUSTIONS
# How many cities are there?
def unique_c(city):
    myset = set(city)
    distinct_city_list=list(myset)
    print("Number of Distinct cities are :", len(distinct_city_list))

# How many restaurants have Table option
def table_option(resto):
    print("THE NUMBER OF RESTAURANTS WITH TABLE OPTION AVAILABLE ARE :", resto.count('Yes'))

# How many has online delivery

def online_dell(online_dell):
    print("THE NUMBER OF RESTAURANTS WITH ONLINE DELIVERY ARE :", online_del.count('Yes'))
print(online_del)

print("#####")
print(unique_c(city))
print("#####")
print(table_option(resto))
print("#####")
print(online_dell(online_dell))

# Scatter chart of Aggregate rating
y=[]
x = np.random.normal(min(y), max(y), len(y))
        plt.scatter(x, y)
        plt.savefig("scatter_sentiment_analysis.pdf")
        plt.show()