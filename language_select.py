from selenium.webdriver.common.by import By
import time


def language_select(driver):
    # Dil seçimi
    driver.find_element(By.XPATH , '//*[@id="app"]/div/nav/nav/div/div/div[2]/div/div[1]/div/div[1]').click()
    time.sleep(2)
    driver.find_element(By.XPATH , '//*[@id="app"]/div/nav/nav/div/div/div[2]/div/div[1]/div/div[2]/ul/li[1]/a').click()
    time.sleep(2)