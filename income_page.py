from utils import scrool_bar
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys

def incomepage(driver):
    
    scrool_bar(driver)
    search_by = driver.find_element(By.XPATH,'//*[@id="search"]')
    search_by.click()
    search_by.send_keys("Emirhan")
    search_by.send_keys(Keys.ENTER)

    print("İncomePage Giriş Yapıldı")

