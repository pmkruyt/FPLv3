from selenium import webdriver
from selenium.webdriver.common.by import By

import time
import os
import numpy as np
import pandas as pd
from tqdm import tqdm

url='https://www.unibet.com/betting/sports/filter/football/england/premier_league/all/matches'

driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url)

#%%
#click initial buttons

cookies='//*[@id="CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll"]'





cookies = driver.find_elements(By.XPATH, cookies)[0]

cookies.click()

#%%
time.sleep(5)

fixture_class="b28b9"
fixtures_list_total=driver.find_elements(By.CLASS_NAME, fixture_class)

time.sleep(5)

amount_of_games=len(fixtures_list_total)

url_list=[]

# for i in range(3):
    

#     time.sleep(5)
#     fixtures_list[i].click()
#     time.sleep(5)
#     url=driver.current_url
#     url_list.append(url)
#     driver.back()
#     time.sleep(5)
    
#     fixture_class="b28b9"
#     fixtures_list2=driver.find_elements(By.CLASS_NAME, fixture_class)
#     fixtures_list2[1].click()
#     time.sleep(5)
#     print('done')
    
for i in tqdm(range(amount_of_games)):
    
    
    fixture_class="b28b9"
    globals()['fixtures_list%i' % i]=driver.find_elements(By.CLASS_NAME, fixture_class)
    #fixtures_list=driver.find_elements(By.CLASS_NAME, fixture_class)
    time.sleep(5)
    globals()['fixtures_list%i' % i][i].click()
    time.sleep(5)
    url=driver.current_url
    url_list.append(url)
    driver.back()
    time.sleep(5)
    
    # fixture_class="b28b9"
    # fixtures_list2=driver.find_elements(By.CLASS_NAME, fixture_class)
    # fixtures_list2[1].click()
    # time.sleep(5)
    # print('done')    
    
    
np.save('url_list.npy',url_list)

driver.close()