   from selenium import webdriver
import pytesseract  
from PIL import ImageFilter
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.expected_conditions import presence_of_element_located,presence_of_all_elements_located
import os
from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.support.select import Select
from datetime import date

ChromeOptions=webdriver.ChromeOptions()
ChromeOptions.add_experimental_option("prefs",{"download.default_directory":"C:\\Users\\pooja\\OneDrive\\Desktop\\PCR\\CURRENT DIRECTORY"})
def senmail(subject,message):
    many_person="malhotrapuja33@gmail.com" #"shivi.jhori@sequelstring.com"
    EMAIL_ADDRESS = "malhotrapuja33@gmail.com"
    EMAIL_PASSWORD = ""
    msg=EmailMessage()
    msg['Subject']=subject
    msg['from']=EMAIL_ADDRESS
    msg['To']=many_person
    msg.set_content(message)
##    msg.attach(MIMEText(message))
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                      smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)

                      smtp.send_message(msg)

import numpy as np
##import cv2 as cv
from PIL import Image
##import pandas as pd
##import time
##import shutil
##from datetime import datetime,timedelta
##import re
##import pyodbc
##from sap_automation import sap_automate
##from mail_trigger import send_mail
##import subprocess
##from Excel_Conversion import excel_conversion
from python_anticaptcha import AnticaptchaClient, ImageToTextTask
from datetime import date
   
# calling the today
# function of date class
today = date.today()
   
# Converting the date to the string
Str = date.isoformat(today)
print("String Representation", Str)

##import socket
user_name='HMCL_RAJASTHAN'
password='123'
driver= webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=ChromeOptions)
##driver=webdriver.Chrome(r"C:\Program Files\chromedriver\chromedriver")
driver.maximize_window()
try:
    driver.get('https://ewaybillgst.gov.in/login.aspx')
except:
    try:
        driver.refresh()
        driver.get('https://ewaybillgst.gov.in/login.aspx')
    except:
         driver.refresh()
        
    
    
wait=WebDriverWait(driver,10)
condition=0
while condition<5:
    try:
        user_id = wait.until(EC.presence_of_element_located((By.ID,"txt_username"))).send_keys(user_name)
        passw = wait.until(EC.presence_of_element_located((By.ID,"txt_password"))).send_keys(password)
        path1=r'C:/Users/OneDrive/Desktop/sql string/screenshot'

        driver.save_screenshot(r'C:/Users/sql string/screenshot/captha.png')
        image = Image.open(r'C:/Users/sql string/screenshot/captha.png')
        width, height = image.size
        print("widhth",width, "height",height)
        left = 560
        top = 245
        right = 720
        bottom = 280
        image = image.crop((left, top, right, bottom))
        image.save(r'C:/Users/Desktop/sql string/screenshot/captha.png')
        api_key = 'b2b510888e9324fdf42975d81168b15a'
        captcha_fp = open(r'C:/Users/pooja/OneDrive/Desktop/sql string/screenshot/captha.png', 'rb')
        client = AnticaptchaClient(api_key)
        task = ImageToTextTask(captcha_fp)
        job = client.createTask(task)
        job.join()

        result = job.get_captcha_text()

        print( result)
 
        capt = WebDriverWait(driver,8).until(EC.presence_of_element_located((By.XPATH,'//*[@id="txtCaptcha"]'))).send_keys(result)
                        
                       
         submitbutton = WebDriverWait(driver,15).until(EC.presence_of_element_located((By.XPATH,'/html/body/form/div[3]/div[2]/div/div/div[2]/div[1]/div/div[4]/input'))).click()
        
    except:
        try:
          condition+=1
        except:
            print("CAPTCHA FAIL")
exit_button = WebDriverWait(driver,2).until(EC.presence_of_element_located((By.XPATH,'//*[@id="A1"]'))).click()


driver.refresh()
try:
    report_button = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="R40"]/a'))).click()
    time.sleep(2)
    EWB_REPORT=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="R4"]/li[1]/a'))).click()
     time.sleep(2)
    OUT_REPORT=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'/html/body/form/div[3]/div/div[1]/div/div/div/ul/li[4]/ul/li[1]/ul/li[1]/a'))).click()
    time.sleep(0.8)
except:
    senmail(subject="PORTAL NOT WORKING",message="PORTAL NOT WORKING")
   
#SELECT DROPDOWNLIST    
try:
    sel = Select(driver.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_ddlUserId"]'))
    #select by select_by_visible_text() method
    time.sleep(2)
    sel.select_by_visible_text("ALL")
    time.sleep(2)
    sel.select_by_Index(20)
    time.sleep(1)
except:
   pass
#GO BUTTON
try:
  go_button=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="ctl00_ContentPlaceHolder1_btn_submit"]'))).click()
except:
    senmail(subject="RECORD NOT DOWNLOAD",message="RECORD NOT DOWNLOAD")
    

  
time.sleep(2)
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")#SCROLLL

#adding preferences to ChromeOptions


#DOWNLOADING FILE
try:
    download=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,'ctl00_ContentPlaceHolder1_List_genMe_btn_export_excel'))).click()
except:
    try:
     download=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="ctl00_ContentPlaceHolder1_List_genMe_btn_export_excel"]'))).click()
    except:
       senmail(subject="EXCEL NOT DOWNLOAD",message="EXCEL NOT DOWNLOAD")



                         
        
    


  
