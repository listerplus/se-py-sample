########################################################################
### FILE:       data.py
### PURPOSE:    Selenium Sandbox
###
########################################################################


class TestData:
    BASE_URL_01 = 'https://the-internet.herokuapp.com/'
    PORT = 8080
    PROJECT = 'PROJ'
    VER = "None"

    CHROME_EXE_PATH = "../driver"
    FIREFOX_EXE_PATH = "../driver"
    EDGE_EXE_PATH = "../driver"

    MAIN_PAGE_TITLE = "The Internet"
    MAIN_PAGE_HEADER = "Welcome to the-internet"

    ADDREMOVE_HEADER = "Add/Remove Elements"
    CHECKBOXES_HEADER = "Checkboxes"
    DROPDOWN_HEADER = "Dropdown List"
    DROPDOWN_OPTIONS = ["Please select an option",
                        "Option 1",
                        "Option 2"]
    BROKENIMAGES_HEADER = "Broken Images"