########################################################################
### FILE:       LoginPage.py
### PURPOSE:    Selenium Sample script for Page Object
### AUTHOR:     Lister Sandalo
###
########################################################################

from selenium.webdriver.common.by import By

from base_page import BasePage

class LoginPage(BasePage):

    EMAIL = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "loginBtn")
    SIGNUP_LINK = (By.LINK_TEXT, "Sign up")

    def __init__(self, driver):
        super().__init__(driver)

    def get_login_page_title(self, title):
        return self.get_title(title)
    
    def is_signup_link_exist(self):
        return self.is_visible(self.SIGNUP_LINK)
    
    