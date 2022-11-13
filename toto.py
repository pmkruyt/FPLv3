from selenium import webdriver
from selenium.webdriver.common.by import By

import time
import os
import numpy as np
import pandas as pd


url='https://sport.toto.nl/wedden/sport/567/engeland-premier-league/wedstrijden'

driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url)

#%%
#click initial buttons

cookie='/html/body/div[1]/div[11]/div[2]/button'

cookies='/html/body/div[1]/div[11]/div[2]/button'

cookies = driver.find_elements(By.XPATH, cookies)[0]

cookies.click()


time.sleep(7)

load="content-loader__load-more-link"
load_button = driver.find_elements(By.CLASS_NAME, load)

for button in load_button:
    time.sleep(10)
    button.click()
    
#%%
#load fixtures    




fixture="event-list__item-link-anchor"
fixture="event-list__content"
fixture="event-list__item-link-anchor"
#fixture="event-card__icon event-card__icon--bet-builder"
#fixture='"event-list__item event-list__item--soccer'
fixture="event-list__item__event-market__market-count__link"
fixture_list = driver.find_elements(By.CLASS_NAME, fixture)

button0=fixture_list[0]

time.sleep(5)

button0.click()


