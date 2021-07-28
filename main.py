from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv
import os
import time
import enter
import tweet

load_dotenv()

def checking(url, num):
    opts = Options()
    opts.headless = True

    driver = webdriver.Chrome(executable_path=os.environ.get('PATH'), options=opts)
    driver.get(url)
    time.sleep(2)

    seats = driver.find_elements_by_class_name('seatText')

    if len(seats) == 2:
        crns = driver.find_elements_by_class_name('crn_value')
        lecCrn = crns[0].text
        labCrn = crns[1].text
        
        if num == 2:
            enter.signUp(lecCrn, labCrn, "lab+lec")
        else:
            enter.signUp(lecCrn, labCrn, "lab")
        
        tweet.tweet("Signed up for the CS class!")
        return True
    
    else:
        print("Full")
        return False

while True:
    check = checking(os.environ.get("CLASS1"), 2)
    if check:
        break

    check = checking(os.environ.get("CLASS2"), 1)
    if check:
        break
    
    check = checking(os.environ.get("CLASS3"), 1)
    if check:
        break
    
    print("---------------")
    time.sleep(1200)