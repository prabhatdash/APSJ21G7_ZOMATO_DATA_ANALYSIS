import textblob as tb
import matplotlib.pyplot as plt
import numpy as np
import csv
# How many cities are there?
# How many restaurants have Table option
# How many has online delivery
# Scatter chart of Aggregate rating
# Bar chart of Text Rating
# Exit

def main_sa():
    print("ENTER 1 TO SHOW POSITIVE:\r\nENTER 2 TO SHOW NEGATIVE:\r\nENTER 3 TO SHOW NEUTRAL:\r\nENTER 4 TO SHOW SCATTER CHART:\r\nENTER 5 TO SHOW BAR CHART:\r\nENTER 6 TO EXIT:")
    delimiters = ["[", "'", "]", "(", ")"]
    y = []
    a = int(input())


    with open('zomato.csv', 'r',errors='ignore') as file:
        reader = csv.reader(file)
        print(reader)
        for row in reader:
            print(reader)
            data = row
            string_data = str(data)

            for i in delimiters:
                string_data = string_data.replace(i, '')
            input_to_textblob = tb.TextBlob(string_data)

    if a == 1:
        print("++++++++++++++++++++++++++\n   Total Positive: ",pos,"\n++++++++++++++++++++++++++")
        main_sa()
    elif a == 2:
        print("++++++++++++++++++++++++++\n   Total Negative: ", neg,"\n++++++++++++++++++++++++++")
        main_sa()
    elif a == 3:
        print("++++++++++++++++++++++++++\n   Total Neutral: ", neu, "\n++++++++++++++++++++++++++")
        main_sa()
    elif a == 4:
        x = np.random.normal(min(y), max(y), len(y))
        plt.scatter(x, y)
        plt.savefig("scatter_sentiment_analysis.pdf")
        plt.show()
        main_sa()
    elif a == 5:
       x=[5,10,15]
       y=[pos,neg,neu]
       plt.bar(x,y,color=['g','r','k'])
       plt.xticks(x,['+VE','-VE','NEUTRAL'])
       plt.savefig("bar_sentiment_analysis.pdf")
       plt.show()
       main_sa()
    elif a==6:
        exit()
