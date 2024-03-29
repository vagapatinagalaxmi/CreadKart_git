# 26/1/2024
# Testcase conftest
import time

import pytest
from selenium import webdriver

# @pytest.fixture
# def setup():
#     driver = webdriver.Chrome()
#     driver.get("https://automation.credence.in/login")
#     driver.maximize_window()
#     time.sleep(10)
#     return driver
# # # hadales with chrome
#
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("--headless")
# @pytest.fixture
# def setup():
# #
#     driver = webdriver.Chrome(options=chrome_options)
#     #driver = webdriver.Chrome()
#     driver.maximize_window()
#     driver.get("https://automation.credence.in/login")
#     return driver
# #https://automation.credence.in/login


# if want give browser at runtime we can write this code
import pytest
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.firefox.options import Options

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
# options = webdriver.EdgeOptions()
# firefox_options = Options()


def pytest_addoption(parser):
    parser.addoption("--browser")  # browser can recongrise the pytest/python


@pytest.fixture
def setup(request):
    browser = request.config.getoption("--browser")
    if browser == 'chrome':
        driver = webdriver.Chrome()
    elif browser == 'firefox':
        driver = webdriver.Firefox()
    elif browser == 'edge':
        driver = webdriver.Edge()

    else:

        driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://automation.credence.in/login")
    #driver.implicitly_wait(5)
    yield driver
    driver.quit()
