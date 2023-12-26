import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.chrome.service import Service


@pytest.fixture()
def setup(request):
    request.cls.driver = webdriver.Chrome(service=Service(executable_path="C:/work/chromedriver.exe"))
    request.cls.driver.get("https://www.irctc.co.in/")
    request.cls.driver.maximize_window()
    yield
    time.sleep(5)
    request.cls.driver.quit()

