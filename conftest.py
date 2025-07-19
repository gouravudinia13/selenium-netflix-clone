# conftest.py
import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()  # Make sure ChromeDriver is installed & in PATH
    driver.maximize_window()
    driver.get("file:///C:/Users/91828/Downloads/YouTube-Video-Summariser-main/selenium/netflix_clone.html")  # Update this path or use a test URL
    yield driver
    driver.quit()
