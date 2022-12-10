# url cannot work with my current way of thinking, because rentals.ca has terrible html code
# and I cannot access the url of a property since when clicking on it, brings up a subpage
# and no information can be scraped from there. Need to learn HTML or something to fix this

from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas

windowsPATH = ""
macPATH = "/Users/yufeng/chromedriver"
driver = webdriver.Chrome(macPATH)
fileHandle = open("data.txt", 'w')

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

for counter in range(2):
    search = driver.find_elements(By.CLASS_NAME, "listing-card__details")
    currProperty = search[counter]
    
    # url data
    link = currProperty.find_element(By.TAG_NAME, "a")
    url.append(link.get_attribute("href"))
    
    # pricing data
    price.append(currProperty.find_element(By.CLASS_NAME, "listing-card__price").text)
    
    # number of beds data
    bedsList = currProperty.find_elements(By.TAG_NAME, "li")
    lowestBedIndex = bedsList[0].text.find("BED")
    numberOfBeds.append(bedsList[0].text[:lowestBedIndex])
    
    # number of baths data
    


fileHandle.write(",".join(url))
fileHandle.write("\n")
fileHandle.write(",".join(price))   
fileHandle.write("\n")
fileHandle.write(",".join(numberOfBeds)) 
fileHandle.write("\n")
driver.quit()
fileHandle.close()