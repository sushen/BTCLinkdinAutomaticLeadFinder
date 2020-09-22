#  Copyright (c) 2020.
#  Version : 1.0.2
#  Script Author : Sushen Biswas and Pedro Brito
#
#  Sushen Biswas Github Link : https://github.com/sushen
#  Pedro Brito Github Link : https://github.com/XiBiTuH
#
#  !/usr/bin/env python
#  coding: utf-8

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--user-data-dir=chrome-data")
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome("../chromedriver.exe",chrome_options=chrome_options)
chrome_options.add_argument("user-data-dir=chrome-data")
driver.implicitly_wait(25)  # seconds


driver.get("https://www.linkedin.com/")

