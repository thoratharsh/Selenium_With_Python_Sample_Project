from selenium.webdriver.common.keys import Keys
import common_Functions as action
from Page_Objects import login_page as login
import allure

class Login:
    def __init__(self,driver):
            self.driver=driver

    @allure.step('Login to OrangeHRM')
    def login_to_OrangeHRM(self):
        action.input_text(self.driver, login.username, "Admin")
        action.input_text(self.driver, login.password, "admin123")
        action.click(self.driver, login.login_button)

    @allure.step('Browser closed')
    def close_browser(self):
        action.close_browser(self.driver)

