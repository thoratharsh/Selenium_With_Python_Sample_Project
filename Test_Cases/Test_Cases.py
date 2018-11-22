from selenium.webdriver.common.keys import Keys
import common_Functions as action
from Page_Objects import login_page as login
from Business_Functions import Login
import pytest

def test_login_to_orangeHRM():
    driver=action.open_browser("https://opensource-demo.orangehrmlive.com/")
    login = Login(driver)
    login.login_to_OrangeHRM()
    login.close_browser()

@pytest.mark.skip(reason="i dont want to run test case")
def test_test2():
    driver = action.open_browser()
    driver.get("https://www.fb.com")
    driver.close()