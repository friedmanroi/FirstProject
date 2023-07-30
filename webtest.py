from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome(service=Service("C:\\Users\\user\\Downloads\\chromedriver-win32 (1)\\chromedriver-win32\\chromedriver.exe"))
# driver2 = webdriver.Firefox(service=Service("C:\\Users\\user\\Downloads\\geckodriver-v0.33.0-win32"))
# my_url = "http://walla.co.il"
# driver.get("http://walla.co.il")
# # driver2.get("http://ynet.co.il")
# title = driver.title
# print(title)
# driver.refresh()
# current_title = driver.title
# print("current url is:",current_title)
# driver.close()
# driver.get("https://translate.google.com")
# driver.find_element(By.CLASS_NAME, value="er8xn").send_keys("חתול")
# time.sleep(3)
driver.get("https://youtube.com/")
# driver.find_element(By.CLASS_NAME, value="ytd-searchbox").send_keys("boris berjch")
driver.find_element(By.XPATH,value = "//input[@id = 'search']").send_keys("boris_brejcha")
driver.find_element(By.XPATH, value ="//div[@style='%0']").click()
time.sleep(5)
# driver.find_element(By.CLASS_NAME,value="QFw9Te").send_keys("כלב")
# element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "search")))

