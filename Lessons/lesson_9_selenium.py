from selenium import webdriver
import time

from selenium.webdriver.common.by import By

dr = webdriver.Opera()
dr.get('https://duckduckgo.com/')

# el = dr.find_element_by_name('q')
el2 = dr.find_element(By.NAME, 'q')
el2.send_keys('python')

button = dr.find_element_by_id('search_button_homepage')

time.sleep(2)

button.click()

time.sleep(2)

link = dr.find_elements_by_partial_link_text('python')


link[3].click()

# dr.quit() - close all tab of browser
# dr.close() - close current tab
