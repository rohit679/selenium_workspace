"""
This python file is going to take decision for shopping, according to the
current temperature and add all the products that are available to the
cart.
SCOPE:
1) Launch Chrome Driver
2) Navigate to wathershopper.pythonanywhere site
3) Check the current temperature
4) Based on temperature, click button & navigate to the respective site
5) Choose all the available products to the cart
6) Click the cart button
7) Close the browser
"""

import time
from selenium import webdriver

def go_to_cart():
    """
        adding_to_cart function is gonna take season as the argument and based upon
        that it adds the product.
    """
    go_to_cart_button = driver.find_element_by_xpath("//button[contains(text(),'Cart')]")
    go_to_cart_button.click()

    print("Clicked go to cart button successfully")


def get_moisturizers_buttons():
    """
        get_moisturizers_buttons is a function that collects all the products and send all
        to get clicked.
    """

    button_list = driver.find_elements_by_xpath("//*[contains(text(),'Aloe')\
                                                 or contains(text(),'Almond')\
                                                 or contains(text(),'aloe')\
                                                 or contains(text(),'almond')]\
                                                 /following-sibling::button")
    click_add_product(button_list)


def get_sunscreens_buttons():
    """
        get_sunscreens_buttons is a function that collects all the products and send all
        to get clicked.
    """

    button_list = driver.find_elements_by_xpath("//*[contains(text(),'SPF-50')\
                                                 or contains(text(),'SPF-30')\
                                                 or contains(text(),'SPF-40')\
                                                 or contains(text(),'spf-30')\
                                                 or contains(text(),'spf-40')\
                                                 or contains(text(),'spf-50')]\
                                                 /following-sibling::button")
    click_add_product(button_list)


def click_add_product(button_list):
    """
        click_add_product is a function that takes button list as an input &
        click out all.
    """

    for i in button_list:
        i.click()
        time.sleep(2)
        print("successfully clicked!!!")


def product_shopping(product_name):
    """
        product_shopping is a function that's take product name as an input and clicks
        the respective button and adds all the respective product to the cart by
        calling funtion.
    """

    driver.find_element_by_xpath("//button[text()='Buy {}']".format(product_name)).click()
    print("Clicked Buy {} button successfully".format(product_name))
    if product_name == "sunscreens":
        get_sunscreens_buttons()
    else:
        get_moisturizers_buttons()

    print("Yes!!! you have added all {} products to the cart:)".format(product_name))


def shopping_decision(temperature):
    """
        shopping_decision is a function which will take current temperature
        and will be taking decision what to buy.
    """

    if temperature < 19:
        print("Weather is too cold, going for buying moisturizers")
        product_shopping("moisturizers")
    elif temperature > 34:
        print("Weather is too hot, going for buying sunscreens")
        product_shopping("sunscreens")
    else:
        print("Weather is nice, don't need to buy anything!!!")


def finding_temperature():
    """
        finding_temperature is a function that is gonna find the
        current temerature.
    """

    temperature = driver.find_element_by_id('temperature').text
    temperature = int(temperature[:-2])
    time.sleep(5)
    print("Current temperature is:",temperature)
    return temperature



if __name__ == "__main__":
    # Creating webdriver and navigating to the respective website
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://weathershopper.pythonanywhere.com/')

    if driver.title == "Current Temperature":
        print("Success: Navigation successful")
    else:
        print("Failed: page Title is incorrect")

    # Finding temperature
    current_temperature = finding_temperature()
    # Navigate to the respective website according to the current temperature
    shopping_decision(current_temperature)
    #go to cart after adding all the products to the cart
    go_to_cart()
    #Closing the page
    time.sleep(5)
    driver.close()
