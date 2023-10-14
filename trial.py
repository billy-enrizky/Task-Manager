import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
import re
import requests
from bs4 import BeautifulSoup
import pytesseract
from PIL import Image

import pytesseract
from PIL import Image

# Load the image
image = Image.open("image.jpg")

# Perform OCR
text = pytesseract.image_to_string(image)
# Print or use the extracted text

# Your input prompt to generate a list of ingredients for a food dish
prompt = f"From this text, find all dishes: {text}"

# Using Chrome to access web
driver = webdriver.Edge()

# Open the website
driver.get('https://www.perplexity.ai/')

search_box = driver.find_element(
    by=By.XPATH,
    value='//textarea[@placeholder="Ask anything..."]')
search_box.send_keys(prompt)
wait = WebDriverWait(driver, 30, 5).until(lambda d: d.find_element(by=By.XPATH, value='//textarea[@placeholder="Ask follow-up..."]'))
search_box.send_keys(Keys.ENTER)
wait = WebDriverWait(driver, 30, 5).until(lambda d: d.find_element(by=By.XPATH, value='//textarea[@placeholder="Ask follow-up..."]'))
answer = driver.find_element(by=By.CLASS_NAME, value='prose')
table = answer.find_element(by=By.XPATH, value='//table[@class="border w-full border-borderMain dark:border-borderMainDark"]')
