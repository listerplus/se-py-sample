########################################################################
### FILE:       test_checkboxes.py
### PURPOSE:    Sample script for Selenium
### AUTHOR:     Lister Sandalo
###
########################################################################

from pages.main_page import MainPage
from pages.checkboxes_page import CheckboxesPage
from tests.base_test import BaseTest
from tests.data import TestData
import pytest_check as pycheck
from time import sleep


class TestCheckboxes(BaseTest):

    def test_01_navigate_to_page(self):
        main_page = MainPage(self.driver)
        main_page.do_click(main_page.CHECKBOXES_LINK)
        checkboxes_page = CheckboxesPage(self.driver)
        header_text = checkboxes_page.get_elemnent_text(checkboxes_page.HEADER)
        assert header_text == TestData.CHECKBOXES_HEADER

    def test_02_select_checkboxes(self):
        # Select checkbox 1 and verify state
        sleep(1)
        checkboxes_page = CheckboxesPage(self.driver)
        checkboxes_page.do_click(checkboxes_page.CHECKBOX_1)
        flag1 = checkboxes_page.is_checkbox_selected(checkboxes_page.CHECKBOX_1)
        pycheck.equal(flag1, True)

        checkboxes_page.do_click(checkboxes_page.CHECKBOX_1)
        pycheck.equal(checkboxes_page.is_checkbox_selected(checkboxes_page.CHECKBOX_1), False)

        # Select checkbox 2 and verify state
        checkboxes_page.do_click(checkboxes_page.CHECKBOX_2)
        flag2 = checkboxes_page.is_checkbox_selected(checkboxes_page.CHECKBOX_2)
        pycheck.equal(flag2, False)

        checkboxes_page.do_click(checkboxes_page.CHECKBOX_2)
        pycheck.equal(checkboxes_page.is_checkbox_selected(checkboxes_page.CHECKBOX_2), True)

