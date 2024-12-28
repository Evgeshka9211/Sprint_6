import pytest
from selenium import webdriver
from constants import Urls

@pytest.fixture
def driver():
    firefox_options = webdriver.FirefoxOptions()
    firefox_options.add_argument('--window-size=1500,1000')
    driver = webdriver.Firefox(firefox_options)
    driver.get(Urls.scooter_main_page)
    yield driver
    driver.quit()