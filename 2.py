import sys
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
import os
def get_driver_path():
    # Get the directory of the current executable or script
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, "msedgedriver.exe")

s = Service(get_driver_path())
#s = Service("C:/Users/shiinainori6/Desktop/edgedriver_win32/msedgedriver.exe")
options = webdriver.EdgeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Edge(service=s, options=options)
driver.get("https://www.accessdata.fda.gov/scripts/ires/index.cfm")
driver.implicitly_wait(10)
month = input("which month's enforcement data do you want: ")

date = driver.find_elements(By.LINK_TEXT, str(month))
if date:
    date[0].click()
else:
    print("Can not find any data from this month")
    driver.quit()

reports = driver.find_elements(By.PARTIAL_LINK_TEXT, "Enforcement Report for Week of "+str(month))
reports += driver.find_elements(By.PARTIAL_LINK_TEXT, "New Recalls Added Since Last Weekly Enforcement Report")

for i, report in enumerate(reports):
    print(f"{i + 1}: {report.text}")

choice = int(input("Enter the number of the link you want to click: ")) - 1
reports[choice].click()
driver.implicitly_wait(20)

ExpositorCSV = driver.find_elements(By.PARTIAL_LINK_TEXT, "Export to CSV")
if ExpositorCSV:
    ExpositorCSV[0].click()



