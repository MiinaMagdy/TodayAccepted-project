from selenium import webdriver
from getpass import getpass
from selenium.webdriver.common.keys import Keys
import time
import csv

username = input("Enter your Handle: ")
password = getpass("Enter your Password: ")

driver = webdriver.Chrome("D:\\Coding\\Selenium\\chromedriver.exe")
driver.get("https://codeforces.com/enter?back=%2F")

username_txtbox = driver.find_element_by_id("handleOrEmail")
username_txtbox.send_keys(username)

password_txtbox = driver.find_element_by_id("password")
password_txtbox.send_keys(password)
password_txtbox.send_keys(Keys.RETURN)

time.sleep(3)

driver.get("https://codeforces.com/submissions/" + username)

submission_table = driver.find_element_by_class_name("status-frame-datatable")

# print(submission_table.text)
for i in submission_table.text:
    print(i)

time.sleep(5)

# driver.quit()
