"""
This python file is going to take decision for shopping, according to the
current temperature.
SCOPE:
1) Launch Chrome Driver
2) Navigate to wathershopper.pythonanywhere site
3) Check the current temperature
4) According to the temperature, click to the respective button for shopping
5) Close the browser
"""

import time
from selenium import webdriver

# Creating webdriver and navigating to the respective website
driver = webdriver.Chrome()
driver.get('https://weathershopper.pythonanywhere.com/')

if(driver.title == "Current Temperature"):
    print ("Success: Navigation successful")
else:
    print ("Failed: page Title is incorrect")

# Finding temperature
temp = driver.find_element_by_id('temperature').text
temp = int(temp[:-2])
time.sleep(5)

# Navigate to the respective website according to the current temperature
if temp < 19:
    driver.find_element_by_xpath("//button[text()='Buy moisturizers']").click()
    print("Weather is too cold, going for buying moisturizers")

elif temp > 34:
    driver.find_element_by_xpath("//button[text()='Buy sunscreens']").click()
    print("Weather is too hot, going for buying sunscream")

else:
    print("Weather is nice, don't need to buy anything!!!")

#Closing the page
time.sleep(5)
driver.close()

