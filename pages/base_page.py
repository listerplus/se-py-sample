########################################################################
### FILE:       BasePage.py
### PURPOSE:    Selenium Sample script for Page Object
### AUTHOR:     Lister Sandalo
###
########################################################################

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import requests


class BasePage:
    """Base class to initialize the base page that will be called from all
    pages.
    Contain methods common to all page object.
    """
    #ref: https://selenium-python.readthedocs.io/page-objects.html

    def __init__(self, driver):
        self.driver = driver
        #self.wait_time = 10

    #adding methods - ref https://www.youtube.com/watch?v=qBK5I_QApCg
    def do_click(self, *locator, wait=10):
        WebDriverWait(self.driver, wait).until(EC.visibility_of_element_located(*locator)).click()

    def do_send_keys(self, *locator, wait=10):
        WebDriverWait(self.driver, wait).until(EC.visibility_of_element_located(*locator)).send_keys(text)

    def get_elemnent_text(self, *locator, wait=10):
        element = WebDriverWait(self.driver, wait).until(EC.visibility_of_element_located(*locator))
        return element.text

    def is_visible(self, *locator, wait=10):
        # element = EC.visibility_of_element_located(*locator)
        try:
            WebDriverWait(self.driver, wait).until(EC.visibility_of_element_located(*locator))
            return True
        except TimeoutException:
            return False

    def is_clickable(self, *locator, wait=10):
        element = EC.element_to_be_clickable(*locator)
        print(f"cdebug: {bool(element)}")
        return bool(element)

    def is_element_exist(self, *locator, wait=10):
        try:
            WebDriverWait(self.driver, wait).until(EC.presence_of_element_located(*locator))
            return True
        except TimeoutException:
            return False

    def get_title(self, wait=10):
        WebDriverWait(self.driver, wait).until(EC.title_is(title))
        return self.driver.title

    def get_url(self):
        return self.driver.current_url

    def is_image_broken(self, *locator, wait=10):
        img = WebDriverWait(self.driver, wait).until(EC.presence_of_element_located(*locator))
        try:
            response = requests.get(img.get_attribute('src'), stream=True)
            if response.status_code != 200:
                print(img.get_attribute('outerHTML') + " is broken.")
                return True
            if response.status_code:
                return False

        except requests.exceptions.MissingSchema:
            print("Encountered MissingSchema Exception")
            return True
        except requests.exceptions.InvalidSchema:
            print("Encountered InvalidSchema Exception")
            return True
        except BaseException as e:
            print(f"Encountered Some other Exception: {e}")
            return True

    def get_num_images_broken_on_page(self):
        broken_count = 0
        url = self.get_url()
        image_list = self.driver.find_elements(By.TAG_NAME, "img")
        print(f"Total number of images on {url} are: {len(image_list)}")

        for img in image_list:
            try:
                response = requests.get(img.get_attribute('src'), stream=True)
                if response.status_code != 200:
                    print(img.get_attribute('outerHTML') + " is broken.")
                    broken_count += 1

            except requests.exceptions.MissingSchema:
                print("Encountered MissingSchema Exception")
            except requests.exceptions.InvalidSchema:
                print("Encountered InvalidSchema Exception")
            except BaseException as e:
                print(f"Encountered Some other Exception: {e}")
        return broken_count
