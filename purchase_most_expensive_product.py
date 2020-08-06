"""
This python file is going to take decision for shopping, according to the
current temperature and add all the products that are available to the
cart.
SCOPE:
1) Launch Chrome Driver
2) Navigate to wathershopper.pythonanywhere site
3) Check the current temperature
4) Based on temperature, click button & navigate to the respective site
5) Choose most expensive available products to the cart
6) Click the cart button
7) Close the browser
"""

import time
from selenium import webdriver

def go_to_cart():
    """
        go_to_cart function is gonna take season as the argument and based upon
        that it adds the product.
    """

    go_to_cart_button = driver.find_element_by_xpath("//button[contains(text(),'Cart')]")
    go_to_cart_button.click()
    print("Clicked go to cart button successfully")


def find_maximum_price(price_list):
    """
        find_maximum_price is function that takes the price list,
        finds the maximum one and return it.
    """

    maximum_price = 0
    for price in price_list:
        if price > maximum_price:
            maximum_price = price

    return maximum_price


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


def adding_maximum_priced_product(price):
    """
        adding_maximum_priced_product is a function that takes maximum price
        of product & clicks out that product.
    """

    driver.find_element_by_xpath("//div[contains(@class,'col-4') and contains(.,'{}')]\
                                 /descendant::button[text()='Add']"\
                                 .format(str(price))).click()
    time.sleep(3)
    print("Clicked the Add button of products having price {}".format(price))


def adding_to_cart(product_type):
    """
        adding_to_cart function is gonna take product type as the argument and based upon
        that it adds the maximum priced product.
    """

    if product_type == "sunscreens":
        price_list = all_summer_product_price()
    else:
        price_list = all_winter_product_price()

    maximum_price = find_maximum_price(price_list)
    print("Maximum price is:", maximum_price)
    # Clicking the Add button for the minimum priced product
    adding_maximum_priced_product(maximum_price)



def product_shopping(product_type):
    """
        product_shopping is a function that's take product type(sunscreens/moisturizers)
        as an input and clicks the respective button and adds all the respective product
        to the cart by calling funtion.
    """

    driver.find_element_by_xpath("//button[text()='Buy {}']".format(product_type)).click()
    print("Clicked Buy {} button successfully".format(product_type))
    adding_to_cart(product_type)
    print("Yes!!! you have added most expensive {} products to the cart:)".format(product_type))


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
    # After adding most expensive product to the cart, go to cart
    go_to_cart()
    #Closing the page
    time.sleep(5)
    driver.close()
