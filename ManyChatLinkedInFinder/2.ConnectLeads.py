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



driver.get(url)
time.sleep(waiting_for_page)

try:
    pages = int(driver.find_element_by_class_name("search-results__pagination-list").find_elements_by_tag_name("li")[
                    -1].text.split("…")[-1])
except:
    pages = 1

#TODO: Make a Massage Sending Function
for i in range(pages):

    people = driver.find_element_by_tag_name("table").find_elements_by_tag_name("tr")
    people = people[1:]

    aux_count = 0

    for p in range(len(people)):

        people = driver.find_element_by_tag_name("table").find_elements_by_tag_name("tr")
        people = people[1:]

        driver.execute_script("window.scrollTo(0, {})".format(aux_count))

        time.sleep(1)

        people[p].find_elements_by_tag_name("button")[-1].click()

        time.sleep(2)

        aux = people[p].find_element_by_class_name("artdeco-dropdown__content-inner").find_elements_by_tag_name("li")

        for m in range(len(aux)):
            # No 3 : Change
            # Change to "Connect"
            if "Connect" in aux[m].text:
                aux[m].click()
                time.sleep(1)

                driver.find_element_by_id("connect-cta-form__invitation").send_keys(random.choice(message_to_connect))
                time.sleep(2)

                try:
                    driver.find_element_by_id("connect-cta-form__email").send_keys(email)
                    time.sleep(1)
                except:
                    pass

                driver.find_element_by_class_name("connect-cta-form__send").click()

                break

            time.sleep(2)

        driver.find_element_by_id("content-main").click()

        aux_count += 80

        # TODO: Fixed the pasination

        try:
            driver.find_element_by_class_name("artdeco-pagination__button").click()
        except:
            break

        time.sleep(10)


# TODO: Test that in 3.2.ShuffleScriptSlowLinkdinUNDPUserList.py
# Close the current browser
driver.close()




