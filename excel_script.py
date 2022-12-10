import pandas as pd

# imports our data.csv file
dataFrame = pd.read_csv('data.csv')

with pd.ExcelWriter("dataBook.xlsx") as writer:
    dataFrame.to_excel(writer,'data')