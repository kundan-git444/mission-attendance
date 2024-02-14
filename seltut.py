import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
import time



def pertg(absent_count, present_count):
    total = absent_count + present_count
    return (present_count/total)*100

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://samvidha.iare.ac.in")


username = driver.find_element(By.ID,"txt_uname")
password = driver.find_element(By.ID, "txt_pwd")

username.send_keys("20951a1234")
password.send_keys("kundansai1212" + Keys.ENTER)

WebDriverWait(driver, 2).until(
    EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Dashboard')]"))

)

driver.get("https://samvidha.iare.ac.in/home?action=std_bio")


absent_count = len(driver.find_elements(By.XPATH, "//*[contains(text(), 'Absent')]"))
present_count = len(driver.find_elements(By.XPATH, "//*[contains(text(), 'Present')]"))


print(absent_count , present_count)
print(pertg(absent_count , present_count))
driver.get("https://samvidha.iare.ac.in/logout")




driver.quit()

#count = driver.find_element(By.XPATH, "//*[contains(text(), 'Dashboard')]").text
'''WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Absent')]"))

)'''
