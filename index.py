from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.get("http://34.69.225.137:5000/") 
time.sleep(4)
driver.find_element(By.XPATH, '//*[@id="app"]/div/main/div/div[2]/div/div/p/a').click()
print("tıklandı")
time.sleep(3)
