#  Copyright (c) 2020.
#  Version : 1.0.2
#  Script Author : Sushen Biswas and Pedro Brito
#
#  Sushen Biswas Github Link : https://github.com/sushen
#  Pedro Brito Github Link : https://github.com/XiBiTuH
#
#  !/usr/bin/env python
#  coding: utf-8

import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
driver = webdriver.Chrome("../chromedriver.exe",chrome_options=chrome_options)

username = os.environ.get('my_Linkdin_username')
password = os.environ.get('my_Linkdin_password')

class Login:
    def __init__(self,  sendUsername, sendPassword, clickButton):
        self.sendUsername = driver.find_element_by_id("session_key").send_keys(username)
        self.sendPassword = driver.find_element_by_id("session_password").send_keys(password)
        self.clickButton = driver.find_element_by_class_name("sign-in-form__submit-button").click()

