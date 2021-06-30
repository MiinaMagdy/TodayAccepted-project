from datetime import date, timedelta
from selenium import webdriver
from getpass import getpass
from selenium.webdriver.common.keys import Keys
import time
import csv

# Login in codeforces Account
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

rows_table = driver.find_elements_by_xpath("/html/body/div[6]/div[4]/div[2]/div[4]/div[6]/table/tbody/tr") # count number of rows
rows = len(rows_table)

columns_table = driver.find_elements_by_xpath("/html/body/div[6]/div[4]/div[2]/div[4]/div[6]/table/tbody/tr[1]/th")
cols = len(columns_table)

# convert Html Table (submissions) to CSV file 

with open('C:\\Users\\phoen\\Documents\\accepted.csv', 'w') as file:        # all you need to do is to change the path to your directory
    csv_writer = csv.writer(file)
    # headers
    csv_writer.writerow(["id", "when", "who", "problem", "lang", "verdict", "time", "memory"])
    for r in range(2, rows + 1):
        entire_row = []
        for c in range(1, cols + 1):
            cell = driver.find_element_by_xpath("/html/body/div[6]/div[4]/div[2]/div[4]/div[6]/table/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
            entire_row.append(cell) 
        if not (entire_row == []):
            csv_writer.writerow(entire_row)

Accepted = 0
today = date.today()
# yester day date
yesterday = today - timedelta(days=1)
yester = str(yesterday)
yester = yester.split()[0]

yesterday = int(yester[8] + yester[9])
# count the number of accepted problems today
with open('C:\\Users\\phoen\\Documents\\accepted.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        if len(row) >= 8:
            date = int(row[1].split()[0][4] + row[1].split()[0][5])
            if date > yesterday and row[5] == "Accepted":
                print(f"\tProblem : {row[3]}")
                Accepted += 1


print(f"\nYou Have Solved {Accepted} Problems Today")

time.sleep(5)

driver.quit()
