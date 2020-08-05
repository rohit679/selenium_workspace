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


def price_filteration(raw_price):
    """
        price_filteration is a function that takes all the price in the text format,
        it will filter the actual price out by removing all irrelevant stuff & return it.
    """

    price = raw_price.split("Price:")[-1]
    price = price.split("Rs.")[-1]
    price = int(price)
    return price


def price_list_generator(product_list):
    """
        price_list_generator is a function that takes raw product price list,
        manipulate all of them and return it.
    """

    price_list = []
    for cost in product_list:
        price = cost.text
        filtered_price = price_filteration(price)
        price_list.append(filtered_price)

    return price_list


def all_summer_product_price():
    """
        all_summer_product_price function will gonna collect all sunscreens product
        price and return it.
    """

    product_list = driver.find_elements_by_xpath("//*[contains(text(),'SPF-50')\
                                                 or contains(text(),'SPF-30')\
                                                 or contains(text(),'SPF-40')\
                                                 or contains(text(),'spf-30')\
                                                 or contains(text(),'spf-40')\
                                                 or contains(text(),'spf-50')]\
                                                 /following-sibling::p")
    return price_list_generator(product_list)


def all_winter_product_price():
    """
        all_winter_product_price function will gonna collect all moisturizer product
        price and return it.
    """

    product_list = driver.find_elements_by_xpath("//*[contains(text(),'Aloe')\
                                                 or contains(text(),'Almond')\
                                                 or contains(text(),'aloe')\
                                                 or contains(text(),'almond')]\
                                                 /following-sibling::p")
    return price_list_generator(product_list)


def adding_to_cart(season):
    """
        adding_to_cart function is gonna take season as the argument and based upon
        that it adds the product.
    """

    if season == "sunscreens":
        price_list = all_summer_product_price()
    elif season == "moisturizers":
        price_list = all_winter_product_price()

    # Clicking the Add button for all product one by one
    for price in price_list:
        print("price to press:", price)
        driver.find_element_by_xpath("//div[contains(@class,'col-4') and contains(.,'{}')]\
                                     /descendant::button[text()='Add']".format(str(price))).click()
        time.sleep(3)

    print("Clicked the Add button of all products")

    go_to_cart_button = driver.find_element_by_xpath("//button[contains(text(),'Cart')]")
    go_to_cart_button.click()

    print("Clicked go to cart button successfully")


def product_shopping(product_name):
    """
        summer_product_shopping is a function that clicks out the buy sunscreens button &
        adds all the respective product to the cart by calling funtion.
    """

    driver.find_element_by_xpath("//button[text()='Buy {}']".format(product_name)).click()
    print("Clicked Buy {} button successfully".format(product_name))
    adding_to_cart(product_name)
    print("Yes!!! you have added all {} products to the cart:)".format(product_name))


def shopping_decision(temperature):
    """
        shopping_product is a function which will take current temperature
        and based upon that, clicks the buy button.
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

    #Closing the page
    time.sleep(5)
    driver.close()
