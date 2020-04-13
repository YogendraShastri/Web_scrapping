from selenium import webdriver      
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd
import bs4
import requests
import lxml


combined  = []
k=1
for i in range(2,5):
     str1 = 'https://www.sikayetvar.com/akbank?page='+str(i)
     HOME_PAGE_URL = str1
     PATIENCE_TIME = 60
     driver = webdriver.Chrome()
     driver.get(HOME_PAGE_URL)
     list_of_hrefs = []
     content_blocks = driver.find_elements_by_class_name("card-body")   
     for block in content_blocks:
         elements = block.find_elements_by_tag_name("a")
         for el in elements:
             list_of_hrefs.append(el.get_attribute("href"))
     lenght = len(list_of_hrefs)
     driver.close()
     for link in list_of_hrefs:
         str2 = link 
         res = requests.get(str2)
         soup = bs4.BeautifulSoup(res.text,'lxml')
         cust_comments = soup.select('.card-text')
         site_comments = soup.select('.card-txt')
         comments = cust_comments+site_comments
         print('new thing '+'\n')
         comments_final = []
         for i in comments:
             print(i.text)
             comments_final.append(i.text)
         print('\nyo baby i m here\n')
         df = pd.DataFrame(comments_final)
         df.to_csv('new_file'+str(k)+'.csv',encoding='utf-8')
         df = pd.read_csv('/home/yogi/Documents/webscrapping/new_file'+str(k)+'.csv',index_col= None, header = 0)
         k+=1
         combined.append(df)
         frame = pd.concat(combined, axis = 0, ignore_index = True)
     df = pd.DataFrame(combined)
     df.to_csv('sikayet_tesiting.csv') 

