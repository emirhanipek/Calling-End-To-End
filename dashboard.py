from utils import scrool_bar , ss_alma
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


def dashboard(driver):
    try:
        try:
            time.sleep(9)
            driver.find_element(By.XPATH , '//*[@id="app"]/div/main/div/div[3]/button/div[3]/div[2]').click()
    
            time.sleep(2)
            bossai_input = driver.find_element(By.XPATH , '//*[@id="bottom-search-bar"]/div/div/input')
   
            bossai_input.send_keys("Son 6 aydaki müşteri şikayetlerinin analizini göster")
    
            time.sleep(2)
    
            bossai_input.send_keys(Keys.ENTER)
    
            time.sleep(70)
    
            driver.find_element(By.XPATH , '//*[@id="top-bar"]/button[2]').click()
    
            time.sleep(2)
    
            driver.find_element(By.XPATH , '//*[@id="top-bar"]/button').click()
   
            print("Dashboard bossai başarılı")
        except:
            print("Dashboard bossai hatası")    

        try:
            driver.find_element(By.XPATH , '//*[@id="app"]/div/main/div/div[1]/div[2]/div/div[2]').click()
            time.sleep(1)
            driver.find_element(By.XPATH , '//*[@id="null-2"]').click()
            time.sleep(2)
            scrool_bar(driver)
            time.sleep(2)
            driver.find_element(By.XPATH ,'//*[@id="app"]/div/main/div/div[1]/div[2]/div/div[2]/div[1]/span/i').click()
            print("Dashboard search bar başarılı")

        except:
            print("Dashboard search bar hatası")
    except:
        print("Dashboard hatası")
        ss_alma("ss/dashboard_hatasi")