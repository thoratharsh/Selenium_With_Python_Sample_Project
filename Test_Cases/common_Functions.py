from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

def open_browser(url):
    driver=webdriver.Chrome()
    driver.implicitly_wait(30)
    driver.maximize_window()
    driver.get(url)
    return driver

def close_browser(driver):
    driver.close()

def input_text(driver,locator,text):
    driver.find_element_by_xpath(locator).send_keys(text)

def click(driver,locator):
    driver.find_element_by_xpath(locator).click()

def select_picklist_by_visible_text(driver,locator,text):
    select = Select(driver.find_element_by_xpath(locator))
    select.select_by_visible_text(text)

def deselect_picklist_by_visible_text(driver,locator,text):
    select = Select(driver.find_element_by_xpath(locator))
    select.deselect_by_visible_text(text)

def select_picklist_by_index(driver,locator,index):
    select = Select(driver.find_element_by_xpath(locator))
    select.select_by_index(index)

def deselect_picklist_by_index(driver,locator,index):
    select = Select(driver.find_element_by_xpath(locator))
    select.deselect_by_index(index)

def select_picklist_by_value(driver,locator,value):
    select = Select(driver.find_element_by_xpath(locator))
    select.select_by_value(value)

def deselect_picklist_by_value(driver,locator,value):
    select = Select(driver.find_element_by_xpath(locator))
    select.deselect_by_index(value)

def get_selected_picklist(driver,locator):
    select = Select(driver.find_element_by_xpath(locator))
    select.first_selected_option()

def get_all_selected_options(driver,locator):
    select = Select(driver.find_element_by_xpath(locator))
    options =select.all_selected_options()
    return options

def delect_all_options(driver,locator):
    select = Select(driver.find_element_by_xpath(locator))
    select.deselect_all()

def is_checkbox_selected(driver,locator):
    result=driver.find_element_by_xpath(locator).is_selected()
    return result

def select_checkbox(driver,locator):
    isSelected=driver.find_element_by_xpath(locator).is_selected()
    if ~isSelected:
        driver.find_element_by_xpath(locator).click()

def deselect_checkbox(driver,locator):
    isSelected=driver.find_element_by_xpath(locator).is_selected()
    if isSelected:
        driver.find_element_by_xpath(locator).click()

