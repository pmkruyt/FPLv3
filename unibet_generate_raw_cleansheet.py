from selenium import webdriver
from selenium.webdriver.common.by import By




import time
import os
import numpy as np
import pandas as pd
from tqdm import tqdm



url_list=np.load('url_list.npy')
raw_text_home_list=[]
raw_text_away_list=[]


url=url_list[4]
amount_of_games=len(url_list)

driver = webdriver.Chrome()
driver.maximize_window()


#%%
def click_fulltime_button():

    fulltime_button_xpath='//*[@id="react-tabs-1"]/div[2]/ul/li[3]/div'
    fulltime_button = driver.find_elements(By.XPATH, fulltime_button_xpath)
    fulltime_button[0].click()
    time.sleep(5)


def show_full_list():
    show_full_class="KambiBC-bet-offer-subcategory__extras-wrapper"
    show_full_class=driver.find_elements(By.CLASS_NAME, show_full_class)
    
    for i in range(len(show_full_class)):
        print('i:',i)
        time.sleep(0.1)
        try:
            show_full_class[i].click() 
        except Exception:
            
            continue 

#%%

for i in tqdm(range(amount_of_games)):
    print(i)
    driver.get(url_list[i])
    
    
    #%%
    #click initial buttons
    
    cookies='//*[@id="CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll"]'
    cookies = driver.find_elements(By.XPATH, cookies)
    time.sleep(5)
    if len(cookies)>0:
        cookies[0].click()
    
    
    
    
    #%%
    time.sleep(5)
    
    temp1=driver.find_elements(By.XPATH,"//*[contains(text(), 'Total Goals by')]")
    
    if len(temp1)==0:
        click_fulltime_button()
        
    time.sleep(5)
    show_full_list()
    
    time.sleep(5)
    
    home_goals_button='//*[@id="react-tabs-1"]/div[2]/ul/li[3]/div/div/ul/li[7]'
    home_goals_button=driver.find_elements(By.XPATH, home_goals_button)    
    raw_text_home_list.append(home_goals_button[0].text)
    
    time.sleep(5)
    
    away_goals_button='//*[@id="react-tabs-1"]/div[2]/ul/li[3]/div/div/ul/li[8]'
    away_goals_button=driver.find_elements(By.XPATH, away_goals_button)    
    raw_text_away_list.append(away_goals_button[0].text)
    
    # time.sleep(12)   
    
    
    # if len(temp1)==0:
    #     click_fulltime_button()
        
    # time.sleep(12)   
    # temp1=driver.find_elements(By.XPATH,"//*[contains(text(), 'Total Goals by')]")   
    
    # temp2=temp1[0]
    
   
    
np.save('cache/raw_text_home_list.npy',raw_text_home_list)  
np.save('cache/raw_text_away_list.npy',raw_text_away_list)        
   
    
   