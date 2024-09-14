import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="class")
def setup(request):

    # Set up WebDriver
    driver = webdriver.Chrome(executable_path="C:\\Users\\rhari\\OneDrive\\DOM\\project_1\\testdata.csv")
    driver.maximize_window()

    # Access the OrangeHRM site
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    # Assign the WebDriver instance to the class that calls this fixture
    request.cls.driver = driver

    # Yield to allow the tests to execute, then quit the driver after tests are done
    yield
    driver.quit()
