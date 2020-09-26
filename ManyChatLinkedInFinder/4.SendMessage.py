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
import time
import random
import os
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from ManyChatLinkedInFinder import user_login
from ManyChatLinkedInFinder import send_message

#No 1 : Change
#Change the messages as you wish, one of them will be randomly picked
subjects = [
    "I have one idea for sale.",
    "I need your opinion about one idea.",
    "I need your mentoring in this field. ",
    "I need your partnership in this reason. "
]

#No 2 : Change
#Change the messages as you wish, one of them will be randomly picked
messages = [
    "Hello Sir, \nI am serving International Organization for more than three years.\nOur company work in Unicef Somalia (Nairobi based) as a BI(Business Intelligence) Consultant. If you accept my invitation I will be a very glade.",
    "Hello Sir, \nI am working with UNDP base organization for more than three years.\nOur company work in Unicef Somalia (Nairobi based) as a BI(Business Intelligence) Consultant. If you accept my invitation I will be a very glade.",
    "Hello Sir, \nI am serving International Diplomate  for more than three years.my office is in Gulshan 2 near the Unicef hartal office.\nOur company work in Unicef Somalia (Nairobi based) as a BI(Business Intelligence) Consultant. If you accept my invitation I will be a very glade."
]



#What will be searched

#Time waiting for page
waiting_for_page = 10

# Login
has_navigator, driver = user_login.login_func()

#No 3 : Change
#Replace this with the link of your list
url = "https://www.linkedin.com/sales/lists/people/6709657848672071680?sortCriteria=CREATED_TIME"

driver.get(url)
time.sleep(waiting_for_page)

try:
    pages = int(driver.find_element_by_class_name("search-results__pagination-list").find_elements_by_tag_name("li")[-1].text.split("…")[-1])
except:
    pages = 1

#change the names of the list
list_to_remove = "UNDP Connection"

list_to_add = "Send UNDP People 2nd Massage"

send_message.send_message_4(pages, driver, subjects, messages, list_to_remove, list_to_add)

# TODO: ADD to Another List After Sending Massage - DONE
# Close the current browser
driver.close()



