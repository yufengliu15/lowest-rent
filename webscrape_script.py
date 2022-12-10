# use google api to implement transit time and to create a url to google map of the surroundings

from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time, os, csv

windowsPATH = ""
macPATH = "/Users/yufeng/chromedriver"
driver = webdriver.Chrome(macPATH)
#fileHandle = open("data.txt", 'w')

url = []
price = []
numberOfBeds = []
numberOfBaths = []
minuteToTrain = []

#userWebsiteToScrape = input("Copy paste the URL you would like to use: ")
userWebsiteToScrape = "https://rentals.ca/ottawa"
driver.get(userWebsiteToScrape)

totalNumOfRentals = driver.find_element(By.CLASS_NAME, "page-title__bottom-line")
totalNumOfRentals = totalNumOfRentals.find_element(By.TAG_NAME, "p")
totalNumOfRentals = int(totalNumOfRentals.text.split(' ', 1)[0])

totalPropertiesTraversed = 0
firstTime = True
while totalPropertiesTraversed < totalNumOfRentals:
    propertiesOnCurrPage = driver.find_elements(By.CLASS_NAME, "listing-card__details")
    for counter in range(len(propertiesOnCurrPage)):
        currProperty = propertiesOnCurrPage[counter]

        # url data
        link = currProperty.find_element(By.TAG_NAME, "a")
        url.append(link.get_attribute("href"))

        # pricing data
        price.append(currProperty.find_element(By.CLASS_NAME, "listing-card__price").text)
        bedsAndBathList = currProperty.find_elements(By.TAG_NAME, "li")
        
        # number of beds data
        bedData = bedsAndBathList[0]
        lowestBedIndex = bedData.text.find("BED")
        numberOfBeds.append(bedData.text[:lowestBedIndex])

        # number of baths data
        bathData = bedsAndBathList[1]
        lowestBedIndex = bathData.text.find("BATH")
        numberOfBaths.append(bathData.text[:lowestBedIndex])
        
        os.system("clear")
        totalPropertiesTraversed += 1
        print (f"{(totalPropertiesTraversed/totalNumOfRentals*100):.2f}%") 
    
    # next page
    nextPageUrl = driver.find_element(By.LINK_TEXT, "Next")
    driver.get(nextPageUrl.get_attribute("href"))
    if firstTime: 
        input("After bot verification, press any key to continue...")
        firstTime = False

dataDictionary = {}

for i in range(totalNumOfRentals):
    propertyDictionary = {}
    propertyDictionary["url"] = url[i]
    propertyDictionary["Pricing"] = price[i]
    propertyDictionary["Beds"] = numberOfBeds[i]
    propertyDictionary["Baths"] = numberOfBaths[i]
    dataDictionary[i] = propertyDictionary

with open("data.csv", 'w', newline='') as csvFile:
    _fieldnames = ['url', 'Beds', 'Baths', 'Pricing']
    writer = csv.DictWriter(csvFile, fieldnames = _fieldnames)
    writer.writeheader()
    for i in range(totalNumOfRentals):
        writer.writerow(dataDictionary[i])

driver.quit()