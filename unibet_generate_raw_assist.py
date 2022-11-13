from selenium import webdriver
from selenium.webdriver.common.by import By

import time
import os
import numpy as np
import pandas as pd
from tqdm import tqdm



url_list=np.load('url_list.npy')
raw_text_assist_list=[]
raw_text_2assist_list=[]


url=url_list[4]
amount_of_games=len(url_list)

driver = webdriver.Chrome()
driver.maximize_window()

for i in range(1):
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
    
    
    goal_scorer_button_xpath='//*[@id="react-tabs-1"]/div[2]/ul/li[8]/div/header'
    
    goal_scorer_button = driver.find_elements(By.XPATH, goal_scorer_button_xpath)
    if i > 0 and len(goal_scorer_button)==0:
        break
    goal_scorer_button[0].click()
    
    time.sleep(5)
       
    
    _gs='//*[@id="react-tabs-1"]/div[2]/ul/li[8]/div/div'
    
    raw_text_asist = driver.find_elements(By.XPATH, _gs)[0].text
    raw_text_assist_list.append(raw_text_asist)
    
    
    _gs2='//*[@id="react-tabs-1"]/div[2]/ul/li[8]/div/div/ul/li[4]/div'
    raw_text_2asist = driver.find_elements(By.XPATH, _gs)
    if len(raw_text_2asist)==0:
        print('2 assists odds not found')
        pass
    
    raw_text_2asist=raw_text_2asist[0].text
    raw_text_2assist_list.append(raw_text_2asist)
    
    time.sleep(5)
    
    
np.save('cache/raw_text_assist_list.npy', raw_text_assist_list)   
np.save('cache/raw_text_2assist_list.npy',raw_text_2assist_list)    