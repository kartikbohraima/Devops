from selenium import webdriver
email = "rishitaggarwal12@gmail.com"
password = "Rishit@123"
driver = webdriver.Chrome('chromedriver.exe')

driver.get("http://localhost/Devops/facebook/")
driver.find_element_by_id("email_login").send_keys(email)
driver.find_element_by_id("pass_login").send_keys(password)
driver.find_element_by_id("loginbutton").click()
