from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By  
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

def rehber_sayfası(driver):
    add_custom = driver.find_element(By.XPATH,'//*[@id="app"]/div/main/div/div[2]/div[2]/div[2]/button')
    add_custom.click()

    name = driver.find_element(By.XPATH,'//*[@id="app"]/div/main/div/div[5]/div/form/div[1]/input')
    name.send_keys("Emirhan İpek")
    time.sleep(1)

    phone_flag = driver.find_element(By.XPATH,'//*[@id="app"]/div/main/div/div[5]/div/form/div[2]/div/div/div')
    phone_flag.click()
    time.sleep(1)
    
    flag = driver.find_element(By.XPATH,'//*[@id="app"]/div/main/div/div[5]/div/form/div[2]/div/div/div/ul/li[223]')
    flag.click()
    time.sleep(1)

    phone_enter = driver.find_element(By.XPATH,'//*[@id="app"]/div/main/div/div[5]/div/form/div[2]/div/div/input')
    phone_enter.send_keys("+90 541 360 99 17")
    time.sleep(1)

    email = driver.find_element(By.XPATH,'//*[@id="email"]')
    email.send_keys("emirhanipek@siriusaitech.com")
    time.sleep(1)

    sektor = driver.find_element(By.XPATH,'//*[@id="app"]/div/main/div/div[5]/div/form/div[4]/div/div/div[2]')
    sektor.click()
    time.sleep(1)

    sektor_value = driver.find_element(By.XPATH,'//*[@id="null-3"]')
    sektor_value.click()
    time.sleep(1)

    is_status = driver.find_element(By.XPATH,'//*[@id="isActive"]')
    is_status.click()
    time.sleep(1)

    driver.find_element(By.XPATH,'//*[@id="isActive"]/option[1]').click()
    time.sleep(1)

    address = driver.find_element(By.XPATH,'//*[@id="adress"]')
    address.send_keys("Ferah Rezidance")
    time.sleep(1)

    note = driver.find_element(By.XPATH,'//*[@id="notes"]')
    note.send_keys("Bir arabası var ")
    time.sleep(1)

    driver.find_element(By.XPATH,'//*[@id="app"]/div/main/div/div[5]/div/form/div[8]/button[2]').click()

    try:
        ok_button = WebDriverWait(driver, 8).until(EC.element_to_be_clickable((By.CLASS_NAME, "swal2-confirm")))
        ok_button.click()
        print("Popup bulundu ve kapatıldı")
    except Exception:
        print("Popup bulunamadı veya otomatik kapandı.")

    time.sleep(1)

    search_bar = driver.find_element(By.XPATH,'//*[@id="search"]')
    time.sleep(1)   
    print('rehber 1')
    search_bar.send_keys("emir")
    time.sleep(1)
    print('rehber 2')
    search_bar.send_keys(Keys.RETURN)
    time.sleep(1)
    print('rehber 3')
    search_bar.clear()
    print('rehber 4')
    time.sleep(1)
    print('rehber 5')
    dropdown_müsteri = driver.find_element(By.XPATH , '//*[@id="status"]')
    dropdown_müsteri_all = driver.find_element(By.XPATH,'//*[@id="status"]/option[1]')
    dropdown_müsteri.click()
    print('rehber 6')
    time.sleep(1)
    dropdown_müsteri_all.click()
    print('rehber 7')
    time.sleep(1)
    print('rehber 8')

    print('GuideBook Bitti')

