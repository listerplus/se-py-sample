########################################################################
### FILE:       dropdown_page.py
### PURPOSE:    Selenium Sample script for Page Object
### AUTHOR:     Lister Sandalo
###
########################################################################

from selenium.webdriver.common.by import By
from .base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import random
from selenium.webdriver.support.ui import Select


class DropdownPage(BasePage):

    """By locators - OR (Object Repository)"""
    HEADER = (By.XPATH, "//h3")
    DROPDOWN_OPTION = (By.XPATH, '//*[@id="dropdown"]')


    """Constructor of the Page"""
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
    
    """Page Actions"""

    # WebDriver’s support classes include one called a “Select”, which provides useful methods for interacting
    # reading ref: https://selenium-python.readthedocs.io/navigating.html#filling-in-forms
    def get_selected_text(self, *locator, wait=10):
        element = WebDriverWait(self.driver, wait).until(EC.presence_of_element_located(*locator))
        select = Select(element)
        return select.first_selected_option.text

    def get_selected_attr_value(self, *locator, wait=10):
        element = WebDriverWait(self.driver, wait).until(EC.presence_of_element_located(*locator))
        select = Select(element)
        return select.first_selected_option.get_attribute("value")

    def get_options_count(self, *locator, wait=10):
        select = Select(WebDriverWait(self.driver, wait).until(EC.presence_of_element_located(*locator)))
        options = select.options
        return len(options)

    def get_options_list(self, *locator, wait=10):
        select = Select(WebDriverWait(self.driver, wait).until(EC.presence_of_element_located(*locator)))
        options = [option.text for option in select.options]
        return options

    # list returned by select.options
    # [<selenium.webdriver.remote.webelement.WebElement (session="9d0c92f90b10c1470764df57712bdccb", element="9958ABBF45D75CF1437993B7EE6687A6_element_11")>,
    # <selenium.webdriver.remote.webelement.WebElement (session="9d0c92f90b10c1470764df57712bdccb",element="9958ABBF45D75CF1437993B7EE6687A6_element_13")>,
    # <selenium.webdriver.remote.webelement.WebElement (session="9d0c92f90b10c1470764df57712bdccb", element="9958ABBF45D75CF1437993B7EE6687A6_element_15")>]

    def do_select_random(self, *locator, wait=10):
        select = Select(WebDriverWait(self.driver, wait).until(EC.presence_of_element_located(*locator)))
        options_count = len(select.options)
        to_select = random.randint(1, options_count-1)
        select.select_by_value(str(to_select))
        return str(to_select)

