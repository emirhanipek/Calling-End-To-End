import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By  
from webdriver_manager.chrome import ChromeDriverManager
from utils import random_mail_name, scrool_bar
from company_info import kayıt_ol_sirket_bilgileri
from register import register
from logout import logout
from login import login
from call_page import call_page
from income_page import incomepage
from guidebook_page import rehber_sayfası
from settings_page import settings_pages

# Tarayıcı başlatma fonksiyonu
def start_driver():
    options = Options()
    options.add_argument("--start-maximized")
    return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Sayfa yönlendirme fonksiyonu
def navigate_to(driver, xpath):
    element = driver.find_element(By.XPATH, xpath)
    element.click()
    time.sleep(1)

# Kullanıcı kaydı ve işlemler
def register_user():
    driver = start_driver()
    url = "http://34.69.225.137:5000/"

    try:
        driver.get(url)
        time.sleep(4)
        print("1")
        driver.find_element(By.XPATH, '//*[@id="app"]/div/main/div/div[2]/div/div/p/a').click()
        time.sleep(5)
        print("2")
        name, email = random_mail_name()
        print("3")
        register(driver, name, email)
        print("4")
        time.sleep(6)
        print("5")
        kayıt_ol_sirket_bilgileri(driver)
        print("6")
        time.sleep(10)
    
        navigate_to(driver, "//button[contains(@class, 'text-white') and contains(@class, 'bg-black/100')]")
        print("7")
        time.sleep(14)
        print("8")
        logout(driver)
        print("9")
        time.sleep(14)
        login(driver, email)
        print("10")
        time.sleep(14)
        scrool_bar(driver)
        print("11")

        navigate_to(driver, '//*[@id="app"]/div/nav/nav/div/div/div[1]/div[2]/div/div/div[1]')
        print("12")
        time.sleep(10)
        print("13")
        time.sleep(2)
        navigate_to(driver, '//*[@id="app"]/div/nav/nav/div/div/div[1]/div[2]/div/div/div[2]/a[2]')
        print("14")
        time.sleep(2)
        scrool_bar(driver)
        print("15")
        time.sleep(2)
        incomepage(driver)
        time.sleep(2)
        print("16")

        
        navigate_to(driver, '//*[@id="app"]/div/nav/nav/div/div/div[1]/div[2]/div/div/div[1]')
        time.sleep(2)
        print("17")
        navigate_to(driver, '//*[@id="app"]/div/nav/nav/div/div/div[1]/div[2]/div/div/div[2]/a[1]')
        time.sleep(2)
        
        print("18")
        time.sleep(2)
        scrool_bar(driver)
        time.sleep(2)
        time.sleep(2)
        print("19")
        call_page(driver)
        time.sleep(2)
        print("20")
        navigate_to(driver, '//*[@id="app"]/div/nav/nav/div/div/div[1]/div[2]/div/a[2]')
        time.sleep(2)
        print("21")
        time.sleep(2)
        scrool_bar(driver)
        time.sleep(2)
        print("22")
        time.sleep(2)
        rehber_sayfası(driver)
        time.sleep(2)
        print("23")
        time.sleep(4)
        driver.find_element(By.XPATH,'//*[@id="app"]/div/nav/nav/div/div/div[1]/div[2]/div/a[3]').click()
        time.sleep(10)
        print("24")
        time.sleep(2)
        scrool_bar(driver)
        print("25")
        time.sleep(2)
        settings_pages(driver)
        time.sleep(2)
        print("26")
        time.sleep(2)
        navigate_to(driver, '//*[@id="app"]/div/nav/nav/div/div/div[2]/div/div[1]/div/div[1]')
        time.sleep(2)
        print("27")
        time.sleep(2)
        navigate_to(driver, '//*[@id="app"]/div/nav/nav/div/div/div[2]/div/div[1]/div/div[2]/ul/li[1]/a')    
        time.sleep(2)
        print("28")
        time.sleep(2)
    finally:
        print("Success")
        driver.quit()

# Scripti çalıştır
register_user()
