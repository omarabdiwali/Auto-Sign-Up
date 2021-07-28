from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from dotenv import load_dotenv
import os
import time

load_dotenv()

def signUp(lecCrn, labCrn, typ):
    url = os.environ.get('URL')
    
    opts = Options()
    opts.headless = True

    driver = webdriver.Chrome(executable_path=os.environ.get('PATH'), options=opts)
    driver.get(url)

    driver.find_element_by_id("UserID").send_keys(os.environ.get("USER"))

    password = driver.find_element_by_name("PIN")
    password.send_keys(os.environ.get("PIN"))
    password.submit()

    time.sleep(1)
    student = driver.find_elements_by_class_name("submenulinktext2")[5]
    student.click()

    time.sleep(1)
    registration = driver.find_elements_by_class_name("submenulinktext2")[6]
    registration.click()

    time.sleep(1)
    classes = driver.find_elements_by_class_name("submenulinktext2")[8]
    classes.click()

    term = Select(driver.find_element_by_id("term_id"))
    term.select_by_value("202130")
    item = driver.find_element_by_id("term_id")
    item.submit()

    lecOption = Select(driver.find_element_by_id("action_id4"))
    labOption = Select(driver.find_element_by_id("action_id5"))

    crn = driver.find_element_by_id("crn_id1")
    crn1 = driver.find_element_by_id("crn_id2")
    crn2 = driver.find_element_by_id("crn_id3")
    crn3 = driver.find_element_by_id("crn_id4")

    if typ == "lab+lec":
        lecOption.select_by_value("DW")
        labOption.select_by_value("DW")

        crn.send_keys(lecCrn)
        crn1.send_keys(labCrn)
    
    else:
        labOption.select_by_value("DW")
        crn.send_keys(labCrn)
    
    crn2.send_keys("32066")
    crn3.send_keys("32070")

    enter = driver.find_elements_by_name("REG_BTN")[1]
    enter.click()

    time.sleep(2)

    exitLink = driver.find_elements_by_class_name("submenulinktext2")[3]
    exitLink.click()

    time.sleep(1)