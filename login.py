from utils import click_element , ss_alma
from selenium.webdriver.common.by import By
import time
from dotenv import load_dotenv
import os
load_dotenv()

def login(driver,email):
    email = driver.find_element(By.ID, "email-address")
    password = driver.find_element(By.ID, "password")
    try:
        try:
            email.send_keys("testexample.com")
            time.sleep(1)
            password.send_keys("StrongPassword123")
            time.sleep(2)
            click_element(driver, By.XPATH, "//button[@type='submit']", "login_button")
            print("Yanlış Email Yanlış Şifre Gecti")

        except :
            print("Yanlış Email Yanlış Şifre Hatası")


        try:
            email.clear()
            password.clear()
            password.send_keys("StrongPassword123")
            time.sleep(1)
            click_element(driver, By.XPATH, "//button[@type='submit']", "login_button")
            print("Boş Email Sifre Yanlıs Gecti")
        except :
            print("Boş Email Sifre Yanlıs Hatası")
        
        
        try:
            email.clear()
            password.clear()
            email.send_keys("test@example.com")
            click_element(driver, By.XPATH, "//button[@type='submit']", "login_button")
            time.sleep(3)
            print("Yanlış Email Bos Şifre Gecti")
        except :
            print("Yanlış Email Bos Şifre Hatası")

        # try:
        #     email.clear()
        #     password.clear()
        #     email.send_keys("emirhaipek@siriusaitech.com")
        #     password.send_keys("qwertyu")
        #     click_element(driver, By.XPATH, "//button[@type='submit']", "login_button")
        #     time.sleep(3)
        #     print("Doğru Email Yanlış Şifre Gecti")
        # except :
        #     print("Doğru Email Yanlış Şifre Hatası")
        
        # try :
        #     email.clear()
        #     password.clear()
        #     email.send_keys("test@example.com")
        #     password.send_keys("strongPassword123")
        #     time.sleep(1)
        #     click_element(driver, By.XPATH, "//button[@type='submit']", "login_button")
        #     print("Yanlış Email Yanlıs Sifre Gecti")
        # except :
        #     print("Yanlış Email Yanlıs Sifre Hatası")
        
        try:
            email.clear()
            password.clear()
            email.send_keys(os.getenv('EMAIL'))
            password.send_keys(os.getenv('PASSWORD'))
            time.sleep(1)
            click_element(driver, By.XPATH, "//button[@type='submit']", "login_button")
            print("Giriş Başarılı")
        except :
            print("Giriş Başarısız")

        print("Login fonksiyonu bitti")
        ss_alma("ss/login_basarili.png")    
        time.sleep(3)
    except Exception as e:
        ss_alma("ss/login_error.png")
        print(f"Login fonksiyonunda hata oluştu : {e}")