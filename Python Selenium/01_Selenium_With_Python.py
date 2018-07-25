from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# instantiate the web driver for the browser(s) like - .chrome() , .firefox(), .ie()
driver = webdriver.Chrome()
driver.get("https://facebook.com") # navigate to the URL using .get("URL") method

username = driver.find_element_by_name("email")
username.clear()
username.send_keys("prateeksingh1590")
username.text
     
password = driver.find_element_by_name("pass")
password.clear()
password.send_keys("Durg@v@ti@123")
password.send_keys(Keys.RETURN) # Keys.RETURN is equal to pressing 'ENTER' button

driver.get("https://www.facebook.com/groups/powershell/") # navigate to the URL using .get("URL") method
#driver.close()
