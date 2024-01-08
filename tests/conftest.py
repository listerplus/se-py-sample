########################################################################
### FILE:       conftest.py
### PURPOSE:    Selenium Example
###
########################################################################

import pytest
from selenium import webdriver
#from webdriver_manager.chrome import ChromeDriverManager
#from webdriver_manager.firefox import GeckoDriverManager
#from selenium.webdriver.edge.service import Service as EdgeService
#from webdriver_manager.microsoft import EdgeChromiumDriverManager
from data import TestData
from datetime import datetime
import pytest_html
from datetime import datetime
from time import sleep
import warnings
import os
#import lib_programname
import shutil
import logging


sut = TestData()
sut.ver = '001'
driver = None

@pytest.fixture(params=["chrome", "edge"], scope='class')    # runs on all the browsers written on params
def init_driver(request):
    global driver
    if request.param == "chrome":
        #driver = webdriver.Chrome(ChromeDriverManager().install())     # if using webdriver-manager
        #driver = webdriver.Chrome(executable_path=sut.CHROME_EXE_PATH)
        driver = webdriver.Chrome()
    if request.param == "firefox":
        #driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())     # if using webdriver-manager
        #driver = webdriver.Firefox(executable_path=sut.FIREFOX_EXE_PATH)
        driver = webdriver.Firefox()
    if request.param == "edge":
        #driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))     # if using webdriver-manager
        #driver = webdriver.Firefox(executable_path=sut.EDGE_EXE_PATH)
        driver = webdriver.Firefox()
    request.cls.driver = driver
    #web_driver.implicitly_wait(10)
    print("Browser: ", request.param)
    driver.get(sut.BASE_URL_01)
    #web_driver.maximize_window()
    yield
    print("Close Driver")
    driver.close()


@pytest.fixture(autouse=True)
def set_warnings():
    """Configure warnings to show while running tests."""
    warnings.simplefilter("once")
    warnings.simplefilter("ignore", DeprecationWarning)

    warnings.filterwarnings(
        "ignore",
        category=ImportWarning,
        message=r".*exec_module\(\) not found; falling back to load_module\(\)",
    )
    warnings.filterwarnings(
        "ignore",
        category=DeprecationWarning,
        message=r".*setDaemon\(\) is deprecated, set the daemon attribute instead.*",
    )
    warnings.filterwarnings(
        "ignore",
        category=DeprecationWarning,
        message=r".* notifyAll\(\) is deprecated, use notify_all\(\) instead.*",
    )

########################################################################
### HOOKS

def pytest_configure(config):
    # Uncomment - config._metadata["Project"] - if to be used on specific projects
    # config._metadata["Project"] = dut.project
    now = datetime.now().strftime('%Y%m%d-%H%M%S')
    if not os.path.exists('./reports'):
        os.makedirs('./reports')
    config.option.htmlpath = f"./reports/report_{now}.html"
    config.option.self_contained_html = True


#Get page screenshot if test fail
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    now = datetime.now().strftime('%Y%m%d-%H%M%S')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    if report.when == 'call':
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            report_directory = os.path.dirname(item.config.option.htmlpath)     # ./reports
            file_name = report.nodeid.replace("::", "_") + f"_{now}.png"       # test_*.py_<class>_<method>[browser].png
            dst = os.path.join(report_directory, file_name)
            # file_name = "screenshot" + now.strftime("%S%H%d%m%Y") + ".png"
            driver.save_screenshot(dst)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra
