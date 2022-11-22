import pytest
from selenium import webdriver
import pandas_gbq
import os

"""
options = webdriver.ChromeOptions()
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')
driver = webdriver.Remote(
command_executor='http://localhost:4444/wd/hub',
options=options
)


chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--window-size=1920,1080')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')"""


query = """
	
"""
result = pandas_gbq.read_gbq(query)
print(result)
"""
#driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get('https://www.google.com/')

print("Docker magic!!")
"""
