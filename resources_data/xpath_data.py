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
# import pandas as pd
# import custom_keywords.keywords_test as keywords_test
#
# class Location(driver):
#         city_name_loc