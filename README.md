# Selenium in Pytest Framework Project
A Selenium example of page object model in Pytest Framework (Python) for the page - https://the-internet.herokuapp.com/

## Pre Requisites
Install the following needed applications
- [Python (3.11)](https://www.python.org/downloads/) - Language
- [PyCharm](https://www.jetbrains.com/pycharm/download/#section=windows) or [Visual Studio](https://code.visualstudio.com/download) - IDE


  ### WebDrivers
   [chromedriver.exe](https://chromedriver.chromium.org/downloads) - Chrome 
   > Note: the chromedriver should be similar to your chrome browser version

   [msedgedriver.exe](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/) - Microsoft Edge
   > Browser usage share ref: https://gs.statcounter.com/browser-market-share

  ### Plugins
  API, Framework, and minimum plugins or libraries to install

  | Title | Description        | Installation                  | Notes |
  |--------|--------------------|-------------------------------|---|
  | [selenium](https://selenium-python.readthedocs.io/index.html) | API | ```pip install selenium```
  | [pytest](https://docs.pytest.org) | Framework | ```pip install -U pytest```
  | [pytest-html](https://pypi.org/project/pytest-html/) | plugin | ```pip install pytest-html``` 
  | [selenium-page-factory](https://github.com/NayakwadiS/selenium-page-factory) | package | ```pip install selenium-page-factory ``` 
  | [autopep8](https://pypi.org/project/autopep8/) | plugin | ```pip install autopep8 ``` | Automatically formats Python code to conform to PEP 8 style guide
  | [flake8](https://pypi.org/project/flake8/) | plugin | ```pip install flake8 ``` | Tests your code for errors against the PEP 8 style guide
  | [pytest-xdist](https://pypi.org/project/pytest-xdist/) | plugin | ```pip install pytest-xdist``` | If running test in parallel (optional)
  | [webdriver-manager](https://pypi.org/project/webdriver-manager/) | plugin | ```pip install webdriver-manager``` | Instead of downloading driver and unziping (optional)

## Running Test

- Open Terminal and run pytest from project directory:
C:\se-py-sample> python -m pytest .tests\<testcase1_name> .tests\<testcase2_name> <...>
- Html report will be generated under the reports folder

## References
- [Selenium with Python](https://selenium-python.readthedocs.io/page-objects.html)
- [The Selenium Browser Automation Project](https://www.selenium.dev/documentation/)
- [Best Selenium Practice Websites in 2023](https://bugbug.io/blog/software-testing/best-selenium-practice-websites/)
- [The Internet](https://the-internet.herokuapp.com/)
- [PEP 8 – Style Guide for Python Code](https://peps.python.org/pep-0008/)
- https://github.com/SeleniumHQ/seleniumhq.github.io/tree/trunk/examples/python/tests



*If you have WebDriver APIs in your test methods, You're Doing It Wrong ~ Simon Stewart*