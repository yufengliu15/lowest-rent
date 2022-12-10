# Lowest-rent
Using Google Chrome and rentals.ca, the program will find all the houses/apartments in an area and return it in a clear and concise excel spreadsheet. 

Uses Selenium API for web scraping, pandas API for data output to excel, Google Maps API for geocoding, and csv for writing and reading .csv files. 

## Objectives
- Learn how to web scrape using Python
- Learn how to manage and write CSV files
- Learn how to send data into an excel sheet
- Learn how to use Google Maps API for more detailed information on the property

## How to use
First, run webscrape_script.py. Once running, there will typically be a bot verification test after the script loads into the next page. Complete the verification then follow the instructions on the terminal. Wait until the script finishes by checking the percentage on the terminal. 

Second, the program will ask you for a file name for the .csv file, which it will then save as. 

Third run excel_script.py. The program will ask you for a .csv file to convert into a .xlsx file. Then it will ask what you would like to name the Excel book. 

Your data should look something like this:
![Alt text](/images/Screen%20Shot%202022-12-10%20at%204.42.58%20PM.png)