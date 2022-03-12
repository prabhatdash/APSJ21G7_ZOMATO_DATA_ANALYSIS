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
def cities():
    groups=df.groupby(by='City')
    print(len(groups.groups.keys()))


def has_table():
    val=df[df['Has Table booking']=='Yes']
    print(val['City'].count())


def delivery():
    val_online=df[df['Has Online delivery']=='Yes']
    print(val_online['City'].count())


def ratings():
    ratings=list(df['Aggregate rating'])
    x = np.random.normal(min(ratings), max(ratings), len(ratings))
    plt.scatter(x, ratings)
    plt.savefig("scatter_zomato.pdf")
    plt.show()


def rating():
    count_ratings=list(df['Rating text'])
    Excellent=(count_ratings.count('Excellent'))
    Very_good=(count_ratings.count('Very Good'))
    Average=(count_ratings.count('Average'))
    Good=(count_ratings.count('Good'))
    Poor=(count_ratings.count('Poor'))
    x=['Poor','Average', 'Good', 'Very Good',  'Excellent']
    y=[Poor,  Average, Good, Very_good, Excellent]
    plt.bar(x,y)
    plt.savefig("bar_zomato_review.pdf")
    plt.show()

def exit():
    exit()

def options():
    print("ENTER 1 TO SHOW NUMBER OF CITIES IN THIS DATA:\r\nENTER 2 TO SHOW IF THE RESTAURANTS HAVE TABLE OPTIONS:\r\nENTER 3 TO HOW IF THE RESTAURANTS HAVE THEIR OWN ONLINE DELIVERY OPTIONS:\r\nENTER 4 TO SHOW SCATTER CHART OF RATINGS:\r\nENTER 5 TO SHOW BAR CHART OF RATING TEXTS:\r\nENTER 6 TO EXIT:")
    inp=int(input())
    if inp==1:
        cities()
        options()
    if inp==2:
        has_table()
        options()
    if inp==3:
        delivery()
        options()
    if inp==4:
        ratings()
        options()
    if inp==5:
        rating()
        options()
    if inp==6:
        pass