from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
import time



def pctg(absent_count, present_count):
    total = absent_count + present_count
    return round((present_count/total)*100,2)

def daysq(absent_count, present_count):
    total = absent_count + present_count
    return 3*total - 4*present_count


users = {"Kundan":['20951a1234','kundansai1212'],"Jaswanth":['20951a1228','jaswanth']}

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://samvidha.iare.ac.in")

for user in users:

    username = driver.find_element(By.ID,"txt_uname")
    password = driver.find_element(By.ID, "txt_pwd")

    username.send_keys(users[user][0])
    password.send_keys(users[user][1] + Keys.ENTER)

    WebDriverWait(driver, 2).until(
        EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Dashboard')]"))

    )

    driver.get("https://samvidha.iare.ac.in/home?action=std_bio")


    absent_count = len(driver.find_elements(By.XPATH, "//*[contains(text(), 'Absent')]"))
    present_count = len(driver.find_elements(By.XPATH, "//*[contains(text(), 'Present')]"))

    print(user)
    print("present : ", present_count)
    print("absent : ", absent_count)
    print("percentage: ", pctg(absent_count , present_count))
    print("days to reach 75%: ", daysq(absent_count,present_count),"days")
    print("**********************************")
    driver.get("https://samvidha.iare.ac.in/logout")




driver.quit()

#count = driver.find_element(By.XPATH, "//*[contains(text(), 'Dashboard')]").text
'''WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Absent')]"))

)'''
