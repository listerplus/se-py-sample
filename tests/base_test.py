########################################################################
### FILE:       base_test.py
### PURPOSE:    Sample script for Selenium
### AUTHOR:     Lister Sandalo
###
########################################################################

import pytest

@pytest.mark.usefixtures("init_driver")
class BaseTest:
    pass

