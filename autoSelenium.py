from PyQt5 import QtWidgets,uic
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class plakaSelenium():
    def __init__(self,plaka):
        self.plaka=plaka
        browser=webdriver.Chrome()
        url="https://www.kentekencheck.nl/RDW-Kenteken-Check?&gclid=CjwKCAjwq5-WBhB7EiwAl-HEkj1J1IXGhbAlaeUxXvNvISy6mrsBDQtqDYl3kRFwSqEFQcozwG0z8hoCJ5EQAvD_BwE"
        browser.get(url)

        time.sleep(2)

# ***********************
# platelabel
# search_pushButton

# uic.loadUi('ui/autoscout24.ui')          
        plaka=browser.find_element(By.XPATH, '//*[@id="subForm"]')
#plaka=plate_box.text()
        plaka.send_keys(self.plaka)
        time.sleep(2)

        browser.find_element(By.XPATH, '//*[@id="kenteken-input-form"]/button').click()
        time.sleep(3)

        browser.quit()

