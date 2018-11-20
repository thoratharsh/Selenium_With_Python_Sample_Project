from selenium.webdriver.common.keys import Keys
import common_Functions as actions

def test_test1():
    driver=actions.open_browser()
    driver.get("https://www.google.com")
    driver.close()

def test_test2():
    driver = actions.open_browser()
    driver.get("https://www.fb.com")
    driver.close()