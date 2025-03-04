import asyncio
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By  
from webdriver_manager.chrome import ChromeDriverManager
from utils import random_mail_name
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

# Tarayıcı başlatma fonksiyonu
def start_driver():
    options = Options()
    options.add_argument("--start-maximized")
    return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Ana fonksiyon
def main():
    driver = start_driver()
    url = "http://34.69.225.137:5000/"

    try:
        driver.get(url)
        time.sleep(4)
        #random mail oluşturma
        name, email = random_mail_name()
        # Kayıt ol
        #register(driver, name, email)
        # Şirket bilgilerini doldur 
        #kayıt_ol_sirket_bilgileri(driver)
        # Çıkış yap
        #logout(driver)
        # Giriş yap
        login(driver, email)
        # Giriş yapınca karşımıza çıkan sayfalar
        incomepage(driver)
        # Arama sayfası
        call_page(driver)
        # Rehber sayfası
        rehber_sayfası(driver)
        # Ayarlar sayfası
        settings_pages(driver)
        # Dil
        language_select(driver)
    
        # Asenkron fonksiyonu çalıştır
        asyncio.run(yorumla_ve_yazdir("ss"))
    finally:
        print("Success")
        driver.quit()

# Scripti çalıştır
if __name__ == "__main__":
    main()