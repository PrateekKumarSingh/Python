from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://mail.markit.com/owa")
#assert "Python" in driver.title
username = driver.find_element_by_name("username")
username.clear()
username.send_keys("markit\prateekkumar.singh")

password = driver.find_element_by_name("password")
password.clear()
password.send_keys("Welcome@123456")
#assert "No results found." not in driver.page_source

button = driver.find_element_by_class_name("signinbutton")
button.click()
#elem.send_keys(Keys.RETURN)
#driver.close()
