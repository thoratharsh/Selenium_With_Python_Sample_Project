from selenium.webdriver.common.keys import Keys
import common_Functions as action
from Page_Objects import login_page as login
import pytest

def test_login_to_orangeHRM():
    driver=action.open_browser("https://opensource-demo.orangehrmlive.com/")
    action.input_text(driver,login.username,"Admin")
    action.input_text(driver, login.password, "admin123")
    action.click(driver,login.login_button)
    action.close_browser(driver)

@pytest.mark.skip(reason="i dont want to run test case")
def test_test2():
    driver = action.open_browser()
    driver.get("https://www.fb.com")
    driver.close()