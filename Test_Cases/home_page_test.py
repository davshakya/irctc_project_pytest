import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select
import pytest
# from pytesseract import pytesseract
import custom_keywords.keywords_test
import pandas as pd
import custom_keywords.keywords_test as keywords_test
import resources_data.xpath_data as xpath_data



@pytest.mark.usefixtures("setup")
class   test_irctc_project():
    def test_homepage(self,driver):
        # driver = webdriver.Chrome(executable_path="C:\work\chromedriver.exe")
        # driver.get("https://www.irctc.co.in/")
        # driver.maximize_window()
        driver.find_element(By.XPATH, "//a[contains(text(),'LOGIN')]").click()
        time.sleep(5)
        driver.find_element(By.XPATH, "//input[@placeholder='User Name']").send_keys('davshakya')
        driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys('Ranjana21#')
        captcha_text=keywords_test.get_captcha_text(driver)
        time.sleep(2)
        print(captcha_text)
        driver.find_element(By.XPATH, "//input[@id='captcha']").send_keys(captcha_text)
        driver.find_element(By.XPATH,"//button[normalize-space()='SIGN IN']").click()
        driver.find_element(By.XPATH,"(//input[contains(@class,'ui-inputtext')])[1]").send_keys(keywords_test.get_from_city())
        driver.find_element(By.XPATH,"//span[contains(text(),'-- Stations --')]/parent::li/following-sibling::li | (//div/ul[@id='pr_id_2_list']/li/span)[1]").click()
        driver.find_element(By.XPATH,"(//input[contains(@class,'ui-inputtext')])[1]").send_keys(keywords_test.get_to_city())
        driver.find_element(By.XPATH,"//span[contains(text(),'-- Stations --')]/parent::li/following-sibling::li").click()


