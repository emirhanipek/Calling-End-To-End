import asyncio
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By  
from webdriver_manager.chrome import ChromeDriverManager
from utils import random_mail_name , sendTelegramTextMessage , temizle_klasor
from company_info import kayıt_ol_sirket_bilgileri
from register import register
from logout import logout
from login import login
from call_page import call_page
from income_page import incomepage
from guidebook_page import rehber_sayfası
from settings_page import settings_pages
from model import yorumla_ve_yazdir
from language_select import language_select
from dashboard import dashboard

# Tarayıcı başlatma fonksiyonu
def start_driver():
    options = Options()
    options.add_argument("--start-maximized")
    return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Ana fonksiyon
def main():
    driver = start_driver()
    url = "https://portal.callingai.app/"

    try:
        driver.get(url)
        time.sleep(10)
        #random mail oluşturma
        name, email = random_mail_name()

        #language_select(driver)
         
        #driver.find_element(By.XPATH, '/html/body/div[1]/div/main/div/div[2]/div/div/p/a').click()
        #time.sleep(3)
             
        #register(driver, name, email)
        
        #kayıt_ol_sirket_bilgileri(driver)
             
        #logout(driver)
             
        login(driver, email)

        dashboard(driver)
       
        incomepage(driver)
     
        call_page(driver)
    
        rehber_sayfası(driver)
        
        settings_pages(driver)
     
        try:
            asyncio.run(yorumla_ve_yazdir("ss"))
            sendTelegramTextMessage("""
        *Call Ai Test Sonuclari*\n
        Register:Tamamlandi  
        Sirket Ekleme:Tamamlandi  
        Cikis Yap:Tamamlandi  
        Giris Yap:Tamamlandi  
        Income Page:Tamamlandi  
        Call Page:Tamamlandi  
        Guidebook:Tamamlandi  
        Settings:Tamamlandi  
        """)

            temizle_klasor("ss")
        except Exception as e :
            temizle_klasor("ss")
            print(f"Asenkron fonksiyon çalıştırma sorun oluştu : {e}")

    finally:
        print("Success")
        driver.quit()

# Scripti çalıştır
if __name__ == "__main__":
    main()