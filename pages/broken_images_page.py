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
import random


class BrokenImagesPage(BasePage):

    """By locators - OR (Object Repository)"""
    HEADER = (By.XPATH, "//h3")
    IMG_1 = (By.XPATH, '//*[@id="content"]/div/img[1]')
    IMG_2 = (By.XPATH, '//*[@id="content"]/div/img[2]')
    IMG_3 = (By.XPATH, '//*[@id="content"]/div/img[3]')

    """Constructor of the Page"""
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
    
    """Page Actions"""
