from utils import click_element
from selenium.webdriver.common.by import By  
from selenium.webdriver.common.keys import Keys

import time
def call_page(driver):
    driver.find_element(By.XPATH , '//*[@id="app"]/div/nav/nav/div/div/div[1]/div[2]/div/div/div[1]').click()
    time.sleep(2)

    driver.find_element(By.XPATH , '//*[@id="app"]/div/nav/nav/div/div/div[1]/div[2]/div/div/div[2]/a[1]').click()
    time.sleep(2)

    search_bar = driver.find_element(By.XPATH , '//*[@id="search"]')
    search_bar.click()
    search_bar.send_keys("emir")
    search_bar.send_keys(Keys.ENTER)

    #dropdown menü
    time.sleep(2)
    driver.find_element(By.XPATH , '//*[@id="app"]/div/main/div/div[2]/div/div[2]/div/div[2]').click()
    driver.find_element(By.XPATH , '//*[@id="status-0"]/span').click()

    date = driver.find_element(By.XPATH , '//*[@id="date"]')
    date.click()
    date.send_keys("01/01/2021")

    time.sleep(2)

    driver.find_element(By.XPATH , '//*[@id="app"]/div/main/div/div[2]/div/div[4]/button').click()
    time.sleep(2)

    name = driver.find_element(By.XPATH , '//*[@id="app"]/div/main/div/div[2]/div/form/div[1]/input')
    name.click()
    name.send_keys("emir")
    time.sleep(1)

    driver.find_element(By.XPATH , '//*[@id="app"]/div/main/div/div[2]/div/form/div[2]/div/div[2]').click()
    time.sleep(2)
    driver.find_element(By.XPATH , '//*[@id="null-0"]').click()
    time.sleep(2)

    #flowup mesajları
    driver.find_element(By.XPATH , '//*[@id="app"]/div/main/div/div[2]/div/form/div[3]/div/div/div[2]').click()
    time.sleep(2)
    # "sms" seçeneğini seç
    sms_option = driver.find_element(By.XPATH, "//span[contains(text(), 'sms')]")
    sms_option.click()
    time.sleep(2)

    return_call = driver.find_element(By.XPATH , '//*[@id="app"]/div/main/div/div[2]/div/form/div[4]/div[2]/div/input')
    return_call.click()
    return_call.send_keys("1")

    driver.find_element(By.XPATH , '//*[@id="default-checkbox"]').click()
    time.sleep(2)

    call_frequency = driver.find_element(By.XPATH , '//*[@id="app"]/div/main/div/div[2]/div/form/div[5]/div/input')
    call_frequency.click()
    call_frequency.send_keys("1")   

    description = driver.find_element(By.XPATH , '//*[@id="notes"]')
    description.click()
    description.send_keys("Kullanıcının bir ford marka arabası vardır 2021 model en son bakımlarını 3 mart günü yapmıştır.")

    driver.find_element(By.XPATH , '//*[@id="app"]/div/main/div/div[2]/div/form/div[7]/button[2]').click()

    click_element(driver,By.CLASS_NAME,"swal2-styled","call_page_ok_button")
    print("Giden Arama Sayfası Görüntülendi")
    time.sleep(2)

