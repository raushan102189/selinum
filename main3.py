from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Create a new instance of Chrome driver
driver = webdriver.Chrome()

# Navigate to a website
driver.get('https://www.google.com')

# Open a new tab
driver..send_keys(Keys.CONTROL + 't')

# Switch to the new tab
driver.switch_to.window(driver.window_handles[-1])

# Navigate to a new link in the new tab
driver.get('https://www.facebook.com')
