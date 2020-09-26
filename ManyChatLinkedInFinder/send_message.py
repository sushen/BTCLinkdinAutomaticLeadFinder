import time
import random


def send_message_connect_leads(pages, driver, message_to_connect, email):
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

            aux = people[p].find_element_by_class_name("artdeco-dropdown__content-inner").find_elements_by_tag_name(
                "li")

            for m in range(len(aux)):
                # No 3 : Change
                # Change to "Connect"
                if "Connect" in aux[m].text:
                    aux[m].click()
                    time.sleep(1)

                    driver.find_element_by_id("connect-cta-form__invitation").send_keys(
                        random.choice(message_to_connect))
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


def send_message_4(pages, driver, subjects, messages, list_to_remove, list_to_add):
    for i in range(pages):

        people = driver.find_element_by_tag_name("table").find_elements_by_tag_name("tr")
        people = people[1:]
        n_people = len(people)

        p = 0
        aux_count = 0
        while n_people > 0:
            time.sleep(5)
            people = driver.find_element_by_tag_name("table").find_elements_by_tag_name("tr")
            people = people[1:]

            time.sleep(1)

            people[p].find_elements_by_tag_name("button")[-1].click()

            time.sleep(2)

            aux = people[p].find_element_by_class_name("artdeco-dropdown__content-inner").find_elements_by_tag_name(
                "li")

            for m in range(len(aux)):
                # No 4 : Change to "Message"
                if "Message" in aux[m].text:

                    aux[m].click()

                    time.sleep(2)

                    try:

                        try:
                            driver.find_element_by_class_name("compose-form__subject-field").send_keys(
                                random.choice(subjects))
                            time.sleep(1)
                        except:
                            pass

                        driver.find_element_by_class_name("compose-form__message-field").send_keys(
                            random.choice(messages))
                        time.sleep(2)

                        # Click send

                        main_aux = driver.find_element_by_class_name("pr3")
                        main_aux.find_element_by_class_name("ml4").click()

                        time.sleep(1)

                        try:
                            driver.find_element_by_class_name("message-overlay").find_element_by_tag_name(
                                "header").find_elements_by_tag_name("button")[-1].click()
                        except:
                            pass

                        time.sleep(3)
                        break
                    except:
                        driver.find_element_by_class_name("message-overlay").find_element_by_tag_name(
                            "header").find_elements_by_tag_name("button")[-1].click()
                        time.sleep(3)
                        break

            time.sleep(2)

            people[p].find_elements_by_tag_name("button")[-1].click()

            time.sleep(2)

            aux = people[p].find_element_by_class_name("artdeco-dropdown__content-inner").find_elements_by_tag_name(
                "li")

            for m in range(len(aux)):
                # No 3 : Change
                # Change to "Add to another list"
                if "Add to another list" in aux[m].text:
                    aux[m].click()
                    time.sleep(3)

                    cont = driver.find_element_by_class_name("entity-lists-ta__ta-container")

                    btns = cont.find_elements_by_tag_name("button")

                    # Remove from list
                    for b in btns:
                        nm = ""
                        try:
                            nm = b.text.split("\n")[0]
                        except:
                            nm = b.text

                        if list_to_remove == nm:
                            b.click()

                    time.sleep(2)
                    mn = driver.find_element_by_class_name("entity-lists-ta__unselected-menu")
                    aux_btns = mn.find_elements_by_tag_name("button")

                    for xua in aux_btns:
                        nm = ""
                        try:
                            nm = xua.text.split(" (")[0]
                        except:
                            nm = xua.text

                        if list_to_add == nm:
                            xua.click()

                    time.sleep(1)
                    driver.find_element_by_class_name("edit-entity-lists-modal__save-btn").click()
                    break

            time.sleep(1)

            driver.find_element_by_id("content-main").click()

            people = driver.find_element_by_tag_name("table").find_elements_by_tag_name("tr")
            people = people[1:]
            n_people = len(people)
