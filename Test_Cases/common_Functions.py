from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import allure

def open_browser(url):
    driver=webdriver.Chrome()
    driver.implicitly_wait(30)
    driver.maximize_window()
    driver.get(url)
    pass
    return driver

@allure.step('browser closed')
def close_browser(driver):
    driver.close()
    pass

@allure.step('Text "{2}" Entered in locator:"{1}"')
def input_text(driver,locator,text):
    driver.find_element_by_xpath(locator).send_keys(text)
    pass

@allure.step('Clicked on locator: {1}')
def click(driver,locator):
    driver.find_element_by_xpath(locator).click()
    pass

@allure.step('Selected picklist')
def select_picklist_by_visible_text(driver,locator,text):
    select = Select(driver.find_element_by_xpath(locator))
    select.select_by_visible_text(text)
    pass

@allure.step('Deselected picklist')
def deselect_picklist_by_visible_text(driver,locator,text):
    select = Select(driver.find_element_by_xpath(locator))
    select.deselect_by_visible_text(text)
    pass

@allure.step('Selected picklist')
def select_picklist_by_index(driver,locator,index):
    select = Select(driver.find_element_by_xpath(locator))
    select.select_by_index(index)
    pass

@allure.step('Deselected picklist')
def deselect_picklist_by_index(driver,locator,index):
    select = Select(driver.find_element_by_xpath(locator))
    select.deselect_by_index(index)
    pass

@allure.step('Selected Picklist')
def select_picklist_by_value(driver,locator,value):
    select = Select(driver.find_element_by_xpath(locator))
    select.select_by_value(value)

@allure.step('Deselected Picklist')
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

@allure.step('Checkbox Selected')
def select_checkbox(driver,locator):
    isSelected=driver.find_element_by_xpath(locator).is_selected()
    if ~isSelected:
        driver.find_element_by_xpath(locator).click()

@allure.step('Checkbox Deselected')
def deselect_checkbox(driver,locator):
    isSelected=driver.find_element_by_xpath(locator).is_selected()
    if isSelected:
        driver.find_element_by_xpath(locator).click()

