import pyautogui
import uuid
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By  

def close_popup(driver):
    try:
        ok_button = WebDriverWait(driver, 8).until(EC.element_to_be_clickable((By.CLASS_NAME, "swal2-confirm")))
        ok_button.click()
        print("Popup bulundu ve kapatıldı")
    except Exception:
        print("Popup bulunamadı veya otomatik kapandı.")
     

def random_mail_name():
    random_name = f"emirhan{uuid.uuid4().hex[:6]}"
    random_email = f"{random_name}@emirtest.com"
    return random_name, random_email

def scrool_bar(driver):
    # Smooth scroll aşağı
        driver.execute_script("""
            window.scrollTo({
                top: document.body.scrollHeight,
                behavior: 'smooth'
            });
        """)
        
        # Scroll'un tamamlanmasını bekle
        time.sleep(3)
        
        print("Yukarı scroll yapılıyor...")
        
        # Smooth scroll yukarı
        driver.execute_script("""
            window.scrollTo({
                top: 0,
                behavior: 'smooth'
            });
        """)
        
        # Scroll'un tamamlanmasını bekle
        time.sleep(3)

def click_element(driver, by, value):
    element = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((by, value)))
    element.click()

def ss_alma(filename):
    screenshot = pyautogui.screenshot()
    screenshot.save(filename)
