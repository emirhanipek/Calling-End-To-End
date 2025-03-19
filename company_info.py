import time
from selenium.webdriver.common.by import By  
from selenium.webdriver.common.keys import Keys
from utils import click_element , ss_alma

def kayıt_ol_sirket_bilgileri(driver):
    try :
        try:
            time.sleep(5)
            companyName = driver.find_element(By.ID, "companyName")
            companyName.clear()
            companyName.send_keys("Sirius Ai Tech")
        except Exception as e:
            print(f"Şirket adı girilirken hata oluştu : {e}")

        try:
            time.sleep(2)
            shortName = driver.find_element(By.ID, "shortName")
            shortName.clear()
            shortName.send_keys("Sirius")
        except Exception as e:
            print(f"Kısa ad girilirken hata oluştu : {e}")
    
        try:
            time.sleep(2)
            companyEmail = driver.find_element(By.ID, "companyEmail")
            companyEmail.clear()
            companyEmail.send_keys("info@info.com")
        except Exception as e:
            print(f"Şirket maili girilirken hata oluştu : {e}")

        try:
            time.sleep(2)
            phone = driver.find_element(By.ID, "phone")
            phone.clear()
            phone.send_keys("+90 541 360 99 17")
        except Exception as e:
            print(f"Telefon numarası girilirken hata oluştu : {e}")
        
        try:
            time.sleep(2)
            adress = driver.find_element(By.ID, "address")
            adress.clear()
            adress.send_keys("İstanbul, Türkiye")
        except Exception as e:
            print(f"Adres girilirken hata oluştu : {e}")

        try:
            time.sleep(2)
            logo_upload_input = driver.find_element(By.ID, "logo-upload")
            logo_path = "/Users/emirhanipek/Desktop/Call End To End/Calling-End-To-End/ss/ok_button.png"
            logo_upload_input.send_keys(logo_path)
        except Exception as e:
            print(f"Logo yüklenirken hata oluştu : {e}")

        try:
            time.sleep(2)
            startsAt = driver.find_element(By.ID, "startsAt")
            startsAt.clear()
            startsAt.send_keys("09:00")
        except Exception as e:
            print(f"Başlangıç saati girilirken hata oluştu : {e}")

        try:
            time.sleep(2)
            finishesAt = driver.find_element(By.ID, "finishesAt")
            finishesAt.clear()
            finishesAt.send_keys("18:00")
        except Exception as e:
            print(f"Bitiş saati girilirken hata oluştu : {e}")
        
        try:
            time.sleep(2)
            about = driver.find_element(By.ID, "about")
            about.clear()
            about.send_keys("""Sirius ai tech bir yazılım ve yapay zeka sirketidir.
            Bu yazılım ve yapay zeka şirketi hakkında bilgi almak ve denemeleri test etmek icin sorunlarınız bana vereblirisiniz.""")
        except Exception as e:
            print(f"Hakkında girilirken hata oluştu : {e}")
        
        try:
            time.sleep(2)
            assistantName = driver.find_element(By.ID, "assistantName")
            assistantName.clear()
            assistantName.send_keys("Aylin")
        except Exception as e:
            print(f"Asistan adı girilirken hata oluştu : {e}")

        try:
            time.sleep(2)
            driver.find_element(By.XPATH, "//select[@class='w-full px-3 h-[41px] border border-gray-300 rounded-md text-black bg-transparent']").click()
            time.sleep(1)
            driver.find_element(By.XPATH, "//option[@value='en']").click()
        except Exception as e:
            print(f"Dil seçimi yapılırken hata oluştu : {e}")
        
        try:
            driver.find_element(By.CLASS_NAME, "multiselect").click()
            time.sleep(2)
            driver.find_element(By.XPATH, "//*[@id='null-2']").click()
            time.sleep(2)
        except Exception as e:
            print(f"Kategoriler seçilirken hata oluştu : {e}")

        try:
            input_field_locator = (By.XPATH, "//input[@class='flex-grow outline-none text-sm text-black bg-transparent']")
            print("3.23")
            input_field = driver.find_element(*input_field_locator)
            print("3.24")
            keywords = ["yapay zeka", "bilişim", "sirius ai tech", "onemli veriler", "web tabanlı uygulamalar"]
            for keyword in keywords:
                input_field.send_keys(keyword)
                input_field.send_keys(Keys.ENTER) 
        except Exception as e:
            print(f"Anahtar kelimeler girilirken hata oluştu : {e}")
        
        try:
            click_element(driver, By.XPATH, "//button[@type='submit']", "kayıt_ol_sirket_bilgileri")
            time.sleep(10)
        except Exception as e:
            print(f"Şirket bilgileri kaydedilirken hata oluştu : {e}")
            time.sleep(10)
            ss_alma("ss/entegrasyon_page.png")
    

        driver.find_element(By.XPATH, "//button[contains(@class, 'text-white') and contains(@class, 'bg-black/100')]").click()
        time.sleep(15)  
        ss_alma("ss/anasayfa_basarili.png")
        
    except Exception as e:    
        print("Şirket bilgileri başarılı bir şekilde dolduruldu.")
        ss_alma("ss/anasayfa_hata.png")
