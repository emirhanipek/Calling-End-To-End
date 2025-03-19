from selenium.webdriver.common.by import By 
from utils import click_element , ss_alma
import time
def register(driver , name , email):
    try:
        driver.find_element(By.ID, "fullName").send_keys(name)
        driver.find_element(By.ID, "email-address").send_keys(email)
        driver.find_element(By.ID, "password").send_keys("StrongPassword123")
        driver.find_element(By.ID, "confirmPassword").send_keys("StrongPassword123")
        driver.find_element(By.ID, "agree-terms").click()
        click_element(driver, By.XPATH, "//button[@type='submit']", "register_button")
        time.sleep(1)
        try:
            print("2.17")
            ok_button = click_element(driver,By.CLASS_NAME,"swal2-styled","ok_button")
            ok_button.click()
        except Exception:
            print("Popup bulunamadı veya otomatik kapandı.")
        print("Register fonksiyonu bitti")
        ss_alma("ss/register_basarili.png")
    except Exception as e:
        print(f"Kayıt olurken hata oluştu : {e}")
        ss_alma("ss/register_hata.png")
