import  pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select
import pytest
# from twocaptcha import TwoCaptcha
# from PIL import Image
# from PIL import Image
# from PIL import ImageDraw
# from PIL import ImageFont
# from pytesseract import pytesseract
# import time


def get_from_city():
    train_file=pd.read_excel("D:/Dev_Progs/irctc_project/trains_data.xlsx")
    return  train_file.iloc[0,1] 
# print(get_from_city())

def get_to_city():
    train_file=pd.read_excel("D:/Dev_Progs/irctc_project/trains_data.xlsx")
    return  train_file.iloc[1,1] 


# def get_captcha_text(driver):
#     with open('Logo.jpg', 'wb') as file:
#         l = driver.find_element(By.XPATH,"//img[@class='captcha-img']")
#         file.write(l.screenshot_as_png)
#     path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
#     image_path = r"D:/Dev_Progs/irctc_project/Logo.jpg"
#     img = Image.open(image_path)
#     pytesseract.tesseract_cmd = path_to_tesseract
#     text = pytesseract.image_to_string(img)
#     captcha_text=text[:-1]
#     return  captcha_text