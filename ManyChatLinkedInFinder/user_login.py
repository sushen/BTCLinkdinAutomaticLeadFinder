from selenium import webdriver
import time
import os
from selenium.webdriver.chrome.options import Options


def login_func():
    chrome_options = Options()
    chrome_options.add_argument("--user-data-dir=chrome-data")
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome("../chromedriver.exe", chrome_options=chrome_options)
    chrome_options.add_argument("user-data-dir=chrome-data")
    driver.implicitly_wait(25)  # seconds

    driver.get("https://www.linkedin.com/")
    time.sleep(2)

    # Function to check
    can_login = True

    try:
        us = driver.find_element_by_id("session_key")
    except:
        can_login = False

    if can_login:
        # I use environment variable base on this tutorials https://www.youtube.com/watch?v=IolxqkL7cD8
        username = os.environ.get('my_Linkdin_username')
        password = os.environ.get('my_Linkdin_password')

        driver.find_element_by_id("session_key").send_keys(username)
        driver.find_element_by_id("session_password").send_keys(password)
        time.sleep(1)

        driver.find_element_by_class_name("sign-in-form__submit-button").click()
        time.sleep(5)

    # Check if he has sales navigator
    bar = driver.find_element_by_class_name("global-nav__primary-items").find_elements_by_tag_name("li")

    has_navigator = False

    for b in bar:
        if "Sales" in b.text:
            has_navigator = True

    return has_navigator, driver
