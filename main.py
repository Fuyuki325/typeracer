import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import keyboard
import requests
from bs4 import BeautifulSoup

def openTypeRacer():
    browser = webdriver.Firefox()
    browser.get('https://play.typeracer.com/')

    # Wait for and click the "Enter a Typing Race" button
    enter_race_button = WebDriverWait(browser, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".gwt-Anchor.prompt-button.bkgnd-green"))
    )
    enter_race_button.click()

    # Allow some extra time for all dynamic content to load
    time.sleep(5)
    inputElem = findInput(browser)
    text = parsing(browser)
    keyboard.wait('ctrl')
    typing(inputElem, text)



def findInput(browser):
  # Wait for and click the "Enter a Typing Race" button
  inputElem = browser.find_element(By.TAG_NAME, 'input')
  
  return inputElem

def parsing(browser):
  # Find all relevant elements that contain the text to type
  spans = browser.find_elements(By.CSS_SELECTOR, "span[unselectable='on']")
  text = ""

  span_count = len(spans)
  first_span = True

  print(span_count)
        
  for span in spans:
    span_text = span.text.strip()
    if span_count == 2:
      if first_span:
        text += span_text + ' '
        first_span = False
      else:
        text += span_text 
    elif span_count == 3:
      if first_span:
        text += span_text
        first_span = False
      else:
        text += span_text + ' '

  text = text.strip()

  return text

def typing(inputElem, text):
  for c in text:
    inputElem.send_keys(c)
    time.sleep(0.1)


openTypeRacer()