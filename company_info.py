import time
from selenium.webdriver.common.by import By  
from selenium.webdriver.common.keys import Keys
from utils import click_element , ss_alma

def kayıt_ol_sirket_bilgileri(driver):
    time.sleep(5)
    companyName = driver.find_element(By.ID, "companyName")
    companyName.clear()
    companyName.send_keys("Sirius Ai Tech")

    shortName = driver.find_element(By.ID, "shortName")
    shortName.clear()
    shortName.send_keys("Sirius")
    
    companyEmail = driver.find_element(By.ID, "companyEmail")
    companyEmail.clear()
    companyEmail.send_keys("info@info.com")

    phone = driver.find_element(By.ID, "phone")
    phone.clear()
    phone.send_keys("+90 541 360 99 17")

    adress = driver.find_element(By.ID, "address")
    adress.clear()
    adress.send_keys("İstanbul, Türkiye")

    logo_upload_input = driver.find_element(By.ID, "logo-upload")
    logo_path = "/Users/emirhanipek/Desktop/Testing/ss/kayıtolundu.png"
    logo_upload_input.send_keys(logo_path)


    startsAt = driver.find_element(By.ID, "startsAt")
    startsAt.clear()
    startsAt.send_keys("09:00")

    finishesAt = driver.find_element(By.ID, "finishesAt")
    finishesAt.clear()
    finishesAt.send_keys("18:00")

    about = driver.find_element(By.ID, "about")
    about.clear()
    about.send_keys("""Sirius ai tech bir yazılım ve yapay zeka sirketidir.
    Bu yazılım ve yapay zeka şirketi hakkında bilgi almak ve denemeleri test etmek icin sorunlarınız bana vereblirisiniz.""")
    
    assistantName = driver.find_element(By.ID, "assistantName")
    assistantName.clear()
    assistantName.send_keys("Aylin")

    # Dil seçimi
    driver.find_element(By.XPATH, "//select[@class='w-full px-3 h-[41px] border border-gray-300 rounded-md text-black bg-transparent']").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//option[@value='en']").click()

    # Sektör seçimi
    driver.find_element(By.CLASS_NAME, "multiselect").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//*[@id='null-2']").click()
    time.sleep(2)
    
    # Input alanına tıklayalım
    input_field_locator = (By.XPATH, "//input[@class='flex-grow outline-none text-sm text-black bg-transparent']")
    input_field = driver.find_element(*input_field_locator)
    keywords = ["yapay zeka", "bilişim", "sirius ai tech", "onemli veriler", "web tabanlı uygulamalar"]
    for keyword in keywords:
        input_field.send_keys(keyword)
        input_field.send_keys(Keys.ENTER) 

    click_element(driver, By.XPATH, "//button[@type='submit']", "kayıt_ol_sirket_bilgileri")
    time.sleep(10)
    ss_alma("ss/entegrasyon_page.png")
    driver.find_element(By.XPATH, "//button[contains(@class, 'text-white') and contains(@class, 'bg-black/100')]").click()
    time.sleep(15)  
    ss_alma("ss/anasayfa.png")
    print("Şirket bilgileri başarılı bir şekilde dolduruldu.")
