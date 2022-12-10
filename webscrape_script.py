# use google api to implement transit time and to create a url to google map of the surroundings

from selenium import webdriver
from selenium.webdriver.common.by import By # used for By.CLASS_NAME etc. 
import os,csv # os for system('clear'), csv for writing to csv files

windowsPATH = ""
macPATH = "/Users/yufeng/chromedriver"
driver = webdriver.Chrome(macPATH)

url = []
price = []
numberOfBeds = []
numberOfBaths = []
address = []

websiteToScrape = "https://rentals.ca/ottawa"
driver.get(websiteToScrape)

totalNumOfRentals = driver.find_element(By.CLASS_NAME, "page-title__bottom-line")
totalNumOfRentals = totalNumOfRentals.find_element(By.TAG_NAME, "p")
totalNumOfRentals = int(totalNumOfRentals.text.split(' ', 1)[0])

totalPropertiesTraversed = 0
firstTime = True
# data retrival for properties on the same page 
while totalPropertiesTraversed < totalNumOfRentals:
    propertiesOnCurrPage = driver.find_elements(By.CLASS_NAME, "listing-card__details")
    
    # data retrieval for each specific property
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
        
        # address data
        addressData = currProperty.find_element(By.CLASS_NAME, "listing-card__title")
        address.append(addressData.text)
        
        os.system("clear")
        totalPropertiesTraversed += 1
        
        # percentage bar
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
    propertyDictionary["Address"] = address[i]
    dataDictionary[i] = propertyDictionary

csvFileName = input("Input a name for the .csv file (do not add extension): ")
csvFileName = csvFileName + '.csv'

with open(csvFileName, 'w', newline='') as csvFile:
    _fieldnames = ['url', 'Beds', 'Baths', 'Pricing', 'Address']
    writer = csv.DictWriter(csvFile, fieldnames = _fieldnames)
    # writeheader allows for column names using fieldnames
    writer.writeheader()
    for i in range(totalNumOfRentals):
        writer.writerow(dataDictionary[i])

driver.quit()