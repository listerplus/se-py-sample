########################################################################
### FILE:       test_broken_images.py
### PURPOSE:    Sample script for Selenium
### AUTHOR:     Lister Sandalo
###
########################################################################

from pages.main_page import MainPage
from pages.broken_images_page import BrokenImagesPage
from tests.base_test import BaseTest
from tests.data import TestData
import pytest_check as pycheck
from time import sleep


class TestBrokenImages(BaseTest):

    def test_01_navigate_to_page(self):
        main_page = MainPage(self.driver)
        main_page.do_click(main_page.BROKEN_IMAGES_LINK)
        brokenimages_page = BrokenImagesPage(self.driver)
        header_text = brokenimages_page.get_elemnent_text(brokenimages_page.HEADER)
        assert header_text == TestData.BROKENIMAGES_HEADER


    def test_02_check_broken_images(self):
        # Select checkbox 1 and verify state
        sleep(1)
        brokenimages_page = BrokenImagesPage(self.driver)
        broken_img_count = brokenimages_page.get_num_images_broken_on_page()
        print(f"Total broken image count: {broken_img_count}")
        pycheck.equal(broken_img_count, 2)

