from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


def e2e_example():
    username = 'standard_user'
    password = 'secret_sauce'

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager(cache_valid_range=1).install()))

    driver.get('https://www.saucedemo.com/')

    # Login
    username_field = driver.find_element(by=By.ID, value='user-name')
    username_field.send_keys(username)
    password_field = driver.find_element(by=By.ID, value='password')
    password_field.send_keys(password)
    login_button = driver.find_element(by=By.ID, value='login-button')
    login_button.click()

    # Add to cart
    menu_button = driver.find_element(by=By.ID, value="add-to-cart-sauce-labs-bike-light")
    menu_button.click()

    # Open the cart
    menu_button = driver.find_element(by=By.ID, value="shopping_cart_container")
    menu_button.click()

    # Assert the item is added to cart
    item_name = driver.find_element(by=By.ID, value="item_0_title_link")
    assert item_name.text == "Sauce Labs Bike Light"

    # Checkout
    menu_button = driver.find_element(by=By.ID, value="checkout")
    menu_button.click()
    menu_button = driver.find_element(by=By.ID, value="first-name")
    menu_button.send_keys(username)
    menu_button = driver.find_element(by=By.ID, value="last-name")
    menu_button.send_keys(username)
    menu_button = driver.find_element(by=By.ID, value="postal-code")
    menu_button.send_keys("78901")
    menu_button = driver.find_element(by=By.ID, value="continue")
    menu_button.click()

    # Assert the order
    item_name_overview = driver.find_element(by=By.ID, value="item_0_title_link")
    assert item_name_overview.text == "Sauce Labs Bike Light"
    total = driver.find_element(by=By.CLASS_NAME, value="summary_total_label")
    assert total.text == "Total: $10.79"
    menu_button = driver.find_element(by=By.ID, value="finish")
    menu_button.click()
    completed_order_text_msg = driver.find_element(by=By.CSS_SELECTOR, value="#checkout_complete_container h2")
    assert completed_order_text_msg.text == "THANK YOU FOR YOUR ORDER"

    # Logout
    menu_button = driver.find_element(by=By.ID, value="react-burger-menu-btn")
    menu_button.click()
    logout_link = driver.find_element(by=By.ID, value="logout_sidebar_link")
    logout_link.click()
    url = driver.current_url
    assert url == "https://www.saucedemo.com/"

    driver.quit()


e2e_example()
