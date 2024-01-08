########################################################################
### FILE:       checkboxes_page.py
### PURPOSE:    Selenium Sample script for Page Object
### AUTHOR:     Lister Sandalo
###
########################################################################

from selenium.webdriver.common.by import By
from .base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class CheckboxesPage(BasePage):

    """By locators - OR (Object Repository)"""
    HEADER = (By.XPATH, "//h3")
    CHECKBOX_1 = (By.XPATH, '//*[@id="checkboxes"]/input[1]')
    CHECKBOX_2 = (By.XPATH, '//*[@id="checkboxes"]/input[2]')

    """Constructor of the Page"""
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
    
    """Page Actions"""

    def get_checkbox_state(self, *locator, wait=10):
        element = WebDriverWait(self.driver, wait).until(EC.visibility_of_element_located(*locator))
        return element.is_selected()

    def is_checkbox_selected(self, *locator, wait=10):
        element = WebDriverWait(self.driver, wait).until(EC.visibility_of_element_located(*locator))
        return element.is_selected()

