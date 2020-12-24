from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time 
import random

driver = webdriver.Chrome()


views = 0
while views != 30:
    driver.get('https://youtube.com')
# Types into Searchbox
    searchbox = driver.find_element_by_xpath('/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div/div[1]/input')
    searchbox.send_keys('Jacob The Shiny')
#clicks search button
    SearchButton = driver.find_element_by_xpath('/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/button')
    SearchButton.click()
#Finds channel name
    driver.implicitly_wait(10)
    channelName = driver.find_element_by_xpath('//*[@id="channel-title"]')
    channelName.click()
#watches video 
    driver.implicitly_wait(10)
    video_thumbnail = driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-browse[2]/ytd-two-column-browse-results-renderer/div[1]/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-shelf-renderer/div[1]/div[2]/ytd-expanded-shelf-contents-renderer/div/ytd-video-renderer/div[1]/div/div[1]/div/h3/a')
    video_thumbnail.click()
#Adds to views counter and closes the current view/ Creates random timer to prevent from geting flaged by youtube
    views += 1
    time.sleep(150)
    print("Current view count is {}!".format(views))


print("task complete {} added to video".format(views))