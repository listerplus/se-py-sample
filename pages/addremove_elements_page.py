########################################################################
### FILE:       addremove_elements_page.py
### PURPOSE:    Selenium Sample script for Page Object
### AUTHOR:     Lister Sandalo
###
########################################################################

from selenium.webdriver.common.by import By
from .base_page import BasePage
from time import sleep
import random


class AddRemoveElementsPage(BasePage):

    """By locators - OR (Object Repository)"""
    HEADER = (By.XPATH, "//h3")
    ADDREMOVE_ELEMENTS_LINK = (By.XPATH, "//a[@href='/add_remove_elements/']")
    ADD_BTN = (By.XPATH, "//button[@onclick='addElement()']")
    DELETE_BTN = (By.XPATH, "//div/button[@onclick='deleteElement()']")

    """Constructor of the Add/Remove Elements Page"""
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
    
    """Page Actions"""
    def do_click_btn_add_element_randomtimes(self):
        ntimes = random.randint(1,6)
        for n in range(ntimes):
            self.do_click(self.ADD_BTN)
            sleep(1)
        return ntimes

    def is_exist_delete_btn(self):
        return self.is_visible(self.DELETE_BTN)

    def get_count_delete_btn(self):
        if self.is_exist_delete_btn:
            del_buttons = self.driver.find_elements(*self.DELETE_BTN)
            return len(del_buttons)
        else:
            return 0

    def do_click_delete_btn_ntimes(self, n = 1):
        for i in range(n):
            self.do_click(self.DELETE_BTN)
            sleep(1)
