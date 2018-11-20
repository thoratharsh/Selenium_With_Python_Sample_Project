from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def open_browser(url):
    driver=webdriver.Chrome()
    driver.get(url)
    return driver

def input_text(driver,locator,text):
    driver.find_element_by_xpath(locator).sendKeys(text)

