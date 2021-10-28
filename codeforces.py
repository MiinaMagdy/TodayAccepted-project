from datetime import date, timedelta
from selenium import webdriver
from getpass import getpass
from selenium.webdriver.common.keys import Keys
import time
import csv

# By Mina Magdy 😌🙋‍♂️

# Login To Codeforces Account
username = input("Enter your Handle: ")
password = getpass("Enter your Password: ")

# driver = webdriver.Chrome("D:\\Coding\\Selenium\\chromedriver.exe") # for Windows 10
driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver") # for Ubuntu
driver.get("https://codeforces.com/enter?back=%2F")

username_txtbox = driver.find_element_by_id("handleOrEmail")
username_txtbox.send_keys(username)

password_txtbox = driver.find_element_by_id("password")
password_txtbox.send_keys(password)
password_txtbox.send_keys(Keys.RETURN)

time.sleep(3)

# Write All Submissions in CSV File
driver.get("https://codeforces.com/submissions/" + username)

rows_table = driver.find_elements_by_xpath("/html/body/div[6]/div[4]/div[2]/div[4]/div[6]/table/tbody/tr") # count number of rows
rows = len(rows_table)

columns_table = driver.find_elements_by_xpath("/html/body/div[6]/div[4]/div[2]/div[4]/div[6]/table/tbody/tr[1]/th")
cols = len(columns_table)


with open('accepted.csv', 'w') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(["id", "when", "who", "problem", "lang", "verdict", "time", "memory"])
    for r in range(2, rows + 1):
        entire_row = []
        for c in range(1, cols + 1):
            cell = driver.find_element_by_xpath("/html/body/div[6]/div[4]/div[2]/div[4]/div[6]/table/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
            entire_row.append(cell) 
        if not (entire_row == []):
            csv_writer.writerow(entire_row)

# manipulate dates

months = {
    "Jan" : 1,
    "Feb" : 2,
    "Mar" : 3,
    "Apr" : 4,
    "May" : 5,
    "Jun" : 6,
    "Jul" : 7,
    "Aug" : 8,
    "Sep" : 9,
    "Oct" : 10,
    "Nov" : 11,
    "Dec" : 12
}

today = date.today()
yesterday = today - timedelta(days=1)

# Choose either today or yesterday
ChoosenDay = yesterday
choose = int(input("1-Today\n2-Yesterday\n>> "))
if choose == 1:
    ChoosenDay = today

# Quering For Accepted Problems' Solution For Today

Problems = set()

with open('accepted.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)
    Accepted = 0
    for row in reader:
        if len(row) >= 8:
            rowDate = row[1].split()[0]
            problem_date = date(int(rowDate[7] + rowDate[8] + rowDate[9] + rowDate[10]), months[rowDate[0] + rowDate[1] + rowDate[2]], int(rowDate[4] + rowDate[5]))
            if problem_date == ChoosenDay and row[5] == "Accepted":
                Problems.add(row[3])

for problem in Problems:
    print(f"\tProblem : {problem}")

input(f"\nYou Have Solved {len(Problems)} Problems Today\nPress Enter to Exit...")

time.sleep(3)
driver.quit()
