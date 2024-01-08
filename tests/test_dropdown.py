########################################################################
### FILE:       test_dropdown.py
### PURPOSE:    Sample script for Selenium
### AUTHOR:     Lister Sandalo
###
########################################################################

from pages.main_page import MainPage
from pages.dropdown_page import DropdownPage
from tests.base_test import BaseTest
from tests.data import TestData
import pytest_check as pycheck
from time import sleep


class TestDropdown(BaseTest):

    def test_01_navigate_to_page(self):
        main_page = MainPage(self.driver)
        main_page.do_click(main_page.DROPDOWN_LINK)
        dropdown_page = DropdownPage(self.driver)
        header_text = dropdown_page.get_elemnent_text(dropdown_page.HEADER)
        assert header_text == TestData.DROPDOWN_HEADER

    def test_02_option_list(self):
        # Verify dropdown options
        sleep(1)
        dropdown_page = DropdownPage(self.driver)
        option_list = dropdown_page.get_options_list(dropdown_page.DROPDOWN_OPTION)
        pycheck.equal(sorted(option_list), sorted(TestData.DROPDOWN_OPTIONS))
        # Verify initial dropdown value
        selected_default = dropdown_page.get_selected_text(dropdown_page.DROPDOWN_OPTION)
        pycheck.equal(selected_default, TestData.DROPDOWN_OPTIONS[0])

    def test_03_select_option(self):
        sleep(1)
        dropdown_page = DropdownPage(self.driver)
        selected_value = dropdown_page.do_select_random(dropdown_page.DROPDOWN_OPTION)
        pycheck.equal(selected_value, dropdown_page.get_selected_attr_value(dropdown_page.DROPDOWN_OPTION))
