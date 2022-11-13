from selenium import webdriver
from selenium.webdriver.common.by import By

import time
import os
import numpy as np
import pandas as pd




url_list=np.load('url_list.npy')
raw_text_goalscorer_list=[]

url=url_list[4]

driver = webdriver.Chrome()
driver.maximize_window()

for i in range(len(url_list)):
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
    
    
    goal_scorer_button_xpath='//*[@id="react-tabs-1"]/div[2]/ul/li[6]/div/header'
    
    goal_scorer_button = driver.find_elements(By.XPATH, goal_scorer_button_xpath)
    
    goal_scorer_button[0].click()
    
    time.sleep(5)
    
    
    # cc="Button__StyledButton-sc-hll3g-0 jHFpSo OutcomeButton__StyledButton-sc-lxwzc0-11 bXvnxh KambiBC-betty-outcome"
    
    # cc = driver.find_elements(By.CLASS_NAME, cc)
    
    _gs='//*[@id="react-tabs-1"]/div[2]/ul/li[6]/div/div/ul/li/div/div[2]/div'
    
    raw_text_goalscorer = driver.find_elements(By.XPATH, _gs)[0].text
    raw_text_goalscorer_list.append(raw_text_goalscorer)
    time.sleep(5)
    
    
np.save('cache/raw_text_goalscorer_list.npy',raw_text_goalscorer_list)    