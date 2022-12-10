import pandas as pd
import googlemaps, urllib.parse
from datetime import datetime

while True:
    userFileName = input("Input .csv file name to read from(do not add extension):")
    userFileName = userFileName + ".csv"
    try:
        dataFrame = pd.read_csv(userFileName)
    except:
        print("Invalid file name")
    else:
        break

userBookName = input("Input name to save book as (do not add extension): ")
userBookName = userBookName + '.xlsx'

gmaps = googlemaps.Client(key="AIzaSyBEU7IurUphn0vFLD5bq6o3LvLcZjqanzc")
addresses = dataFrame.Address
googleURLAddress = []

#for i in range(len(addresses)):
googleURL = "https://www.google.com/maps/search/?api=1&query="
for i in range(len(addresses)):
    googleURLAddress.append(googleURL + urllib.parse.quote(addresses[i]))
dataFrame.Address = googleURLAddress

with pd.ExcelWriter(userBookName) as writer:
    dataFrame.to_excel(writer,'data')
