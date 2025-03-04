from utils import click_element , ss_alma , scrool_bar
from selenium.webdriver.common.by import By
import time

from dotenv import load_dotenv
import os

load_dotenv()

def login(driver,email):
    #gecersiz email formatı
    driver.find_element(By.ID, "email-address").send_keys("testexample.com")
    time.sleep(1)
    driver.find_element(By.ID, "password").send_keys("StrongPassword123")
    time.sleep(1)
    click_element(driver, By.XPATH, "//button[@type='submit']", "login_button")
    ss_alma("ss/login/gecersiz_email.png")
    time.sleep(3)
    driver.find_element(By.ID, "email-address").clear()
    driver.find_element(By.ID, "password").clear()



    #bos email
    driver.find_element(By.ID, "email-address").send_keys("")
    time.sleep(1)
    driver.find_element(By.ID, "password").send_keys("StrongPassword123")
    time.sleep(1)
    click_element(driver, By.XPATH, "//button[@type='submit']", "login_button")
    ss_alma("ss/login/bos_email.png")
    time.sleep(3)
    driver.find_element(By.ID, "email-address").clear()
    driver.find_element(By.ID, "password").clear()


    #bos sifre
    driver.find_element(By.ID, "email-address").send_keys("test@example.com")
    time.sleep(1)
    driver.find_element(By.ID, "password").send_keys("")
    time.sleep(1)
    click_element(driver, By.XPATH, "//button[@type='submit']", "login_button")
    ss_alma("ss/login/bos_sifre.png")
    time.sleep(3)
    driver.find_element(By.ID, "email-address").clear()
    driver.find_element(By.ID, "password").clear()

    #yanlıs sifre pop up cıkıyor hata mesajı
    # driver.find_element(By.ID, "email-address").send_keys("emirhaipek@siriusaitech.com")
    # time.sleep(1)
    # driver.find_element(By.ID, "password").send_keys("qwertyu")
    # time.sleep(1)
    # click_element(driver, By.XPATH, "//button[@type='submit']", "login_button")
    # ss_alma("ss/login/yanlıs_sifre.png")
    # time.sleep(3)
    # driver.find_element(By.ID, "email-address").clear()
    # driver.find_element(By.ID, "password").clear()


    #yanlıs giriş pop up cıkıyor hata mesajı
    # driver.find_element(By.ID, "email-address").send_keys("test@example.com")
    # time.sleep(1)
    # driver.find_element(By.ID, "password").send_keys("strongPassword123")
    # time.sleep(1)
    # click_element(driver, By.XPATH, "//button[@type='submit']", "login_button")
    # ss_alma("ss/login/yanlıs_giris.png")
    # time.sleep(3)
    # driver.find_element(By.ID, "email-address").clear()
    # driver.find_element(By.ID, "password").clear()


    #("Login Doğru giriş")
    driver.find_element(By.ID, "email-address").send_keys(os.getenv('EMAIL'))
    time.sleep(1)
    driver.find_element(By.ID, "password").send_keys(os.getenv('PASSWORD'))
    time.sleep(1)

    click_element(driver, By.XPATH, "//button[@type='submit']", "login_button")
    time.sleep(8)
    scrool_bar(driver)
    time.sleep(2)
    driver.find_element(By.XPATH , '//*[@id="app"]/div/nav/nav/div/div/div[1]/div[2]/div/div/div[1]')


