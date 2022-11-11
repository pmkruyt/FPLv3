from selenium import webdriver
from selenium.webdriver.common.by import By

import time
import os
import numpy as np

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


time.sleep(np.random.normal(2))

toon_meer_class="content-loader__load-more-link"
toon_meer_button = driver.find_elements(By.CLASS_NAME, toon_meer_class)

for button in toon_meer_button:
    button.click()
    
#%%
#load fixtures    

time.sleep(np.random.normal(5))


fixture="event-list__item-link-anchor"
fixture_list = driver.find_elements(By.CLASS_NAME, fixture)

button0=fixture_list[0]
button0.click()
