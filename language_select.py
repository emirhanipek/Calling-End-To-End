from selenium.webdriver.common.by import By
import time
from utils import ss_alma

def language_select(driver):
    # Dil seçimi
    try : 
        driver.find_element(By.XPATH , '//*[@id="app"]/div/main/div/div[1]/div/div').click()
        time.sleep(2)
        driver.find_element(By.XPATH , '//*[@id="app"]/div/main/div/div[1]/div/div[2]/ul/li[1]/a').click()
        time.sleep(2)
        ss_alma("ss/dilsecimi_basarili.png")
    except Exception as e :
        print(f"Dil seçimi sorun oluştu : {e}")
        ss_alma("ss/dilsecimi_hata.png")