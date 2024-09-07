import time
from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def test_homepage():
    opt = webdriver.ChromeOptions()
    opt.add_argument("--start-maximized")
    chromedriver_autoinstaller.install()
    driver = webdriver.Chrome(options=opt)
    # driver = webdriver.Chrome(service=Service(executable_path="chromedriver.exe"))
    driver.get("https://www.irctc.co.in/")
    # driver.maximize_window()
    time.sleep(5)
    driver.find_element(By.XPATH, "//a[contains(text(),'LOGIN')]").click()
    driver.find_element(By.XPATH, "//input[@placeholder='User Name']").send_keys('davshakya')
    driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys('Ranjana21#')
    # captcha_text=keywords_test.get_captcha_text(driver)
    # time.sleep(2)
    # print(captcha_text)
    # driver.find_element(By.XPATH, "//input[@id='captcha']").send_keys(captcha_text)
    # driver.find_element(By.XPATH,"//button[normalize-space()='SIGN IN']").click()
    # driver.find_element(By.XPATH,"(//input[contains(@class,'ui-inputtext')])[1]").send_keys(keywords_test.get_from_city())
    # driver.find_element(By.XPATH,"//span[contains(text(),'-- Stations --')]/parent::li/following-sibling::li | (//div/ul[@id='pr_id_2_list']/li/span)[1]").click()
    # driver.find_element(By.XPATH,"(//input[contains(@class,'ui-inputtext')])[1]").send_keys(keywords_test.get_to_city())
    # driver.find_element(By.XPATH,"//span[contains(text(),'-- Stations --')]/parent::li/following-sibling::li").click()

test_homepage()


#hello this is demo_branch commit again changes done