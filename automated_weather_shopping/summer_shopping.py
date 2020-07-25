"""
This python module is for finding out two least expensive product 
in which one of them contain SPF30 & other would contain SPF50. 

SCOPE:
1) Launch Chrome Driver
2) Navigate to site 'weathershopper.pythonanywhere.com/sunscreen'
3) Finding out the product, which satisfies our base codition 
4) Click to the 'Add' button of the desired product
5) Click to the 'Go to cart' button
6) Close the browser
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


def find_minimum_price(price_list):
    """ 
        find_minimum_price is function that takes the price list,
        finds the least one and return it.
    """

    minimum_price = 10000
    for price in price_list:
        if price < minimum_price:
            minimum_price = price
    
    return minimum_price


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


def spf50_price(driver):
    """ 
        spf50_price is a function that takes driver as the arguement,
        collects all the SPF50 product price and return it.
    """

    product_list = driver.find_elements_by_xpath("//*[contains(text(),'SPF-50')]/following-sibling::p")
    generated_price = price_list_generator(product_list)
    return generated_price


def spf30_price(driver):
    """ 
        spf30_price is a function that takes driver as the arguement,
        collects all the SPF30 product price and return it.
    """

    product_list = driver.find_elements_by_xpath("//*[contains(text(),'SPF-30')]/following-sibling::p")
    generated_price = price_list_generator(product_list)
    return generated_price


def adding_spf50(driver):
    """ 
        getting_spf50 is a function that takes driver as the arguement, 
        finds the minimum spf50 product available and clicks to the
        respective 'add' button.
    """

    spf50_price_list = spf50_price(driver)
    minimum_price = find_minimum_price(spf50_price_list)

    # Clicking the Add button of the least expensive product having spf50
    driver.find_element_by_xpath("//div[contains(@class,'col-4') and contains(.,'{}')]\
    /descendant::button[text()='Add']".format(str(minimum_price))).click()
    print("Clicked the Add button of the least expensive product having spf50")


def adding_spf30(driver):
    """ 
        adding_spf30 is a function that takes driver as the arguement, 
        finds the minimum spf30 product available and clicks to the
        respective 'add' button.
    """

    spf30_price_list = spf30_price(driver)
    minimum_price = find_minimum_price(spf30_price_list)
    
    # Clicking the Add button of the least expensive product having spf30
    driver.find_element_by_xpath("//div[contains(@class,'col-4') and contains(.,'{}')]\
    /descendant::button[text()='Add']".format(str(minimum_price))).click()
    print("Clicked the Add button of the least expensive product having spf30")


" Driver code starts here "

if __name__ == "__main__":
    # Creating driver
    driver = webdriver.Chrome()
    driver.get('https://weathershopper.pythonanywhere.com/sunscreen')

    if(driver.title == "The Best Sunscreens in the World!"):
        print("Success: Navigation successful")
    else:
        print("Failed: page Title is incorrect")

    time.sleep(5)
    # Calling function to add the respective product into the cart
    adding_spf50(driver)
    adding_spf30(driver)
    
    go_to_cart_button = driver.find_element_by_xpath("//button[contains(text(),'Cart')]")
    go_to_cart_button.click()
    print("Clicked go to cart button successfully")
    
    time.sleep(3)
    # Closing the browser
    driver.close()

    
