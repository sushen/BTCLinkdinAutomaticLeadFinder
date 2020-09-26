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

# No 1 : Change
# Message to send when connecting
message_to_connect = [
    "আপনাকে আইটি রিলেটেড প্রাডাক্ট নিয়ে কাজ করছেন দেখে আপনাকে ম্যাসেজ দিচ্ছি, আমার একটা প্রডাক্ট এবং সার্ভিস আছে যেটা নিয়ে কথা ব্যাবসায়িক কথা বলতে চাই । আপনি কি সময় দেবেন ?",
    "আমার একটা প্রডাক্ট এবং সার্ভিস আছে যেটা নিয়ে কথা ব্যাবসায়িক কথা বলতে চাই । আপনাকে আইটি রিলেটেড প্রাডাক্ট নিয়ে কাজ করছেন দেখে আপনাকে ম্যাসেজ দিচ্ছি,  আপনি কি সময় দেবেন ?",
    "আপনাকে আইটি রিলেটেড প্রাডাক্ট নিয়ে কাজ করছেন দেখে আপনাকে ম্যাসেজ দিচ্ছি,আপনি কি সময় দেবেন ? আমার একটা প্রডাক্ট এবং সার্ভিস আছে যেটা নিয়ে কথা ব্যাবসায়িক কথা বলতে চাই । ",
]

email = "sushenbiswasaga@gmail.com"

# Time waiting for page
waiting_for_page = 10

# Login
has_navigator, driver = user_login.login_func()

# No 2 : Change
# #Replace this with the link of your list
url = "https://www.linkedin.com/sales/lists/people/6710357981692780544"

driver.get(url)
time.sleep(waiting_for_page)

try:
    pages = int(driver.find_element_by_class_name("search-results__pagination-list").find_elements_by_tag_name("li")[
                    -1].text.split("…")[-1])
except:
    pages = 1

#TODO: Make a Massage Sending Function

send_message.send_message_connect_leads(pages, driver, message_to_connect, email)


# TODO: Test that in 3.2.ShuffleScriptSlowLinkdinUNDPUserList.py
# Close the current browser
driver.close()




