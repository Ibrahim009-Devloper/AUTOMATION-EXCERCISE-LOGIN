import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def setup():
    chrome_option = Options()
    # chrome_option.add_argument("--headless=new")
    chrome_option.add_argument("--no-sandbox")
    chrome_option.add_argument("--disable-dev-shm-usage")


    driver = webdriver.Chrome(options= chrome_option)
    driver.implicitly_wait(20)
    driver.maximize_window()
    yield driver

    driver.quit()