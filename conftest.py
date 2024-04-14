import pytest
from selenium import webdriver
driver=None
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="Firefox"
    )

@pytest.fixture(scope="class")
def browser(request):
    global driver
    browser_name=request.config.getoption("browser_name")
    if browser_name=="chrome":
        driver=webdriver.Chrome()

    elif browser_name=="firefox":
        driver=webdriver.Firefox()

    elif browser_name=="ie":
        driver=webdriver.Ie()
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()


    request.cls.driver=driver
    yield
    driver.close()
@pytest.fixture(scope="class")
def webbrowser(request):
    driver = webdriver.Firefox()
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    request.cls.driver=driver

