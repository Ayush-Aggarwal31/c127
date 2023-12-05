
from selenium import webdriver
import pandas as pd
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import time
START_URL = "https://exoplanets.nasa.gov/discovery/exoplanet-catalog/"

browser = webdriver.Edge()
browser.get(START_URL)

time.sleep(10)

planets_data = []

def scrape():
    for i in range(0,20):
        print("Scraping the page Number ",i+1)    
        soup = BeautifulSoup(browser.page_source,"html.parser")

        for ul_tag in soup.find_all("ul", attrs={"class", "exoplanet"}):
            li_tags = ul_tag.find_all("li")
            temp_list = []

            for index , li_tag in enumerate(li_tags):
                if index == 0 :
                    temp_list.append(li_tag.find_all("a")[0].contents[0])
                else:
                    try:
                        temp_list.append(li_tag.contents[0])
                    except:
                        temp_list.append("")

            planets_data.append(temp_list)
        browser.find_element(by=By.XPATH,value='//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()


scrape()
print(planets_data[1])

# Define Header
headers = ["name", "light_years_from_earth", "planet_mass", "stellar_magnitude", "discovery_date"]

# Define pandas DataFrame   
planets_df=pd.DataFrame(planets_data,columns=headers)

# Convert to CSV
planets_df.to_csv("data.csv",index=True,index_label="id")