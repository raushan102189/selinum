from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Initialize the browser and go to the login page
browser = webdriver.Chrome("../chromedriver.exe ")
browser.get("https://youtu.be/kVO_2yvZFVA")
time.sleep(10)
browser.find_element_by_tag_name('body').send_keys('k')

browser.find_element_by_tag_name('body').send_keys('m')

#open new tab
# browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't')
def work():
    browser.get("https://youtu.be/kVO_2yvZFVA")

    
    time.sleep(5)

    browser.switch_to.window(browser.window_handles[-1])



for c  in range(10):
    # work()
    pass


