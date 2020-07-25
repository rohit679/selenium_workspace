"""
This python module is for filling the payment details for purchasing 
respective required products.

SCOPE:
1) Launch Chrome Driver
2) Navigate to site 'weathershopper.pythonanywhere.com/cart'
3) Click to the 'pay with card' button
4) Fill out all the details for payment
5) Click to the submit button
6) Close the browser
"""

import time
from selenium import webdriver

def fill_payment_details(driver):
    " This function is for filling the payment details via iframe popup "
    
    # switching driver to the iframe
    driver.switch_to.frame("stripe_checkout_app")
    print("successfully, switched to the iframe")
    
    # validating payment form 
    email_id = driver.find_element_by_xpath("//input[@type='email']")
    email_id.send_keys("rohit111@gmail.com")
    print("sent email-id successfully")

    account_number = driver.find_element_by_xpath("//input[@type='tel' and @placeholder='Card number']")
    account_number.send_keys("6011100990139424")
    print("sent account number successfully")

    exp_date = driver.find_element_by_xpath("//input[@type='tel' and @placeholder='MM / YY']")
    exp_date.send_keys("07/23")
    print("sent expiry date successfully")
    
    cvv = driver.find_element_by_xpath("//input[@type='tel' and @placeholder='CVC']")
    cvv.send_keys("133")
    print("sent cvv number successfully")
    
    zip_code = driver.find_element_by_xpath("//input[contains(@placeholder,'ZIP Code')]")
    zip_code.send_keys("711201")
    print("sent zip code successfully")
    
    remember_me = driver.find_element_by_xpath("//div[@class='Checkbox-tick']")
    remember_me.click()
    print("clicked remember me button successfully")

    mobile = driver.find_element_by_xpath("//input[@type='tel' and @autocomplete='mobile tel']")
    mobile.send_keys("9223146910")
    print("sent mobile number successfully")

    submit = driver.find_element_by_xpath("//button[@type='submit' and @class='Button-animationWrapper-child--primary Button']")
    submit.click()
    print("clicked submit button successfully")
    
    time.sleep(5)


" Driver code starts here "

if __name__ == "__main__":
    # Creating driver 
    driver = webdriver.Chrome()
    driver.get('https://weathershopper.pythonanywhere.com/cart')
    
    if(driver.title == "Cart Items"):
        print("Success: Navigation successful")
    else:
        print("Failed: page Title is incorrect") 
    
    # Clicking payment button 
    payment_button = driver.find_element_by_xpath("//button[@type='submit']")
    payment_button.click()
    print("clicked pay with card button successfully")
    time.sleep(5)
    
    # Calling function for filling the form 
    fill_payment_details(driver)

    # Switch back to the main window 
    # driver.switch_to_default_content()
    # time.sleep(5)
    
    # Closing the driver
    driver.close()

    
















