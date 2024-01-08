########################################################################
### FILE:       main_page.py
### PURPOSE:    Selenium Sample script for Page Object
### AUTHOR:     Lister Sandalo
###
########################################################################

from .base_page import BasePage
from selenium.webdriver.common.by import By

class MainPage(BasePage):
    
    ADDREMOVE_ELEMENTS_LINK = (By.XPATH, "//a[@href='/add_remove_elements/']")
    BROKEN_IMAGES_LINK = (By.XPATH, "//a[@href='/broken_images']")
    CHECKBOXES_LINK = (By.XPATH, "//a[@href='/checkboxes']")
    DROPDOWN_LINK = (By.XPATH, "//a[@href='/dropdown']")

