from selenium import webdriver
from selenium.webdriver.common.by import By

import time
import os
import numpy as np
import pandas as pd
from tqdm import tqdm



url_list=np.load('url_list.npy')
raw_text_2goal_list=[]
raw_text_3goal_list=[]
raw_text_4goal_list=[]

url=url_list[4]
amount_of_games=len(url_list)

driver = webdriver.Chrome()
driver.maximize_window()

for i in range(amount_of_games):
    print(i)
    driver.get(url_list[i])
    
    
    #%%
    #click initial buttons
    
    cookies='//*[@id="CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll"]'
    cookies = driver.find_elements(By.XPATH, cookies)
    if len(cookies)>0:
        cookies[0].click()
    
    #%%
    time.sleep(5)
    
    
    goal_scorer_button_xpath='//*[@id="react-tabs-1"]/div[2]/ul/li[7]/div'
    
    goal_scorer_button = driver.find_elements(By.XPATH, goal_scorer_button_xpath)
    if i > 0 and len(goal_scorer_button)==0:
        break
    goal_scorer_button[0].click()
    
    time.sleep(5)
       
    
    _gs2='//*[@id="react-tabs-1"]/div[2]/ul/li[7]/div/div/ul/li[1]/div'
    
    raw_text_2goal = driver.find_elements(By.XPATH, _gs2)[0].text
    raw_text_2goal_list.append(raw_text_2goal)
    time.sleep(5)
    
    _gs3='//*[@id="react-tabs-1"]/div[2]/ul/li[7]/div/div/ul/li[2]/div/div[2]'
    
    raw_text_3goal = driver.find_elements(By.XPATH, _gs3)[0].text
    raw_text_3goal_list.append(raw_text_3goal)
    time.sleep(5)
    
    _gs4='//*[@id="react-tabs-1"]/div[2]/ul/li[7]/div/div/ul/li[3]/div'
    
    raw_text_4goal = driver.find_elements(By.XPATH, _gs4)
    if len(raw_text_4goal)==0:
        print('4 goals odds not found')
        pass
    raw_text_4goal=raw_text_4goal[0].text
    
    raw_text_4goal_list.append(raw_text_4goal)
    time.sleep(5)
    
    
np.save('raw_text_2goal_list.npy',raw_text_2goal_list)  
np.save('raw_text_3goal_list.npy',raw_text_3goal_list)  
np.save('raw_text_4goal_list.npy',raw_text_4goal_list)    