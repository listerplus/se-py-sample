########################################################################
### FILE:       test_addremove_elements.py
### PURPOSE:    Sample script for Selenium
### AUTHOR:     Lister Sandalo
###
########################################################################

from pages.main_page import MainPage
from pages.addremove_elements_page import AddRemoveElementsPage
from tests.base_test import BaseTest
from tests.data import TestData
import pytest_check as pycheck
from time import sleep


class TestAddRemoveElements(BaseTest):

    def test_01_navigate_to_page(self):
        main_page = MainPage(self.driver)
        main_page.do_click(main_page.ADDREMOVE_ELEMENTS_LINK)
        addremove_page = AddRemoveElementsPage(self.driver)
        header_text = addremove_page.get_elemnent_text(addremove_page.HEADER)
        assert header_text == TestData.ADDREMOVE_HEADER

    def test_02_page(self):
        # Check that there is no delete button\
        sleep(1)
        addremove_page = AddRemoveElementsPage(self.driver)
        flag = addremove_page.is_visible(addremove_page.DELETE_BTN, wait=2)
        pycheck.equal(flag, False)

        # Check that Add Element button is visible
        # We can skip the remaining test if this test fails, or remove this test as it is implied on the following tests
        flag = addremove_page.is_visible(addremove_page.ADD_BTN)
        pycheck.equal(flag, True)

    def test_03_add_elements(self):
        addremove_page = AddRemoveElementsPage(self.driver)
        sleep(2)
        num = addremove_page.do_click_btn_add_element_randomtimes()
        pycheck.equal(num, addremove_page.get_count_delete_btn())

    def test_04_remove_elements(self):
        addremove_page = AddRemoveElementsPage(self.driver)
        num = addremove_page.get_count_delete_btn()
        addremove_page.do_click_delete_btn_ntimes(num)
        pycheck.equal(0, addremove_page.get_count_delete_btn())

