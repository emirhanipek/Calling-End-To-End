import pyautogui
import uuid
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By  
import random
import os
import shutil
import requests

def generate_phone_number():
    # Türkiye'deki GSM operatörlerinin numara başlıkları
    prefixes = ["501", "505", "506", "507", "531", "532", "533", "534", "535", "536", "537", "538", "539"]
    
    # Rastgele bir prefix seç
    prefix = random.choice(prefixes)
    
    # 7 haneli rastgele bir sayı oluştur
    number = "".join([str(random.randint(0, 9)) for _ in range(7)])
    
    # Formatlı telefon numarasını döndür
    return f"{prefix}-{number[:3]}-{number[3:]}"

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

def click_element(driver, by, value,image_name):
    ss_alma(f"ss/{image_name}.png")
    element = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((by, value)))
    element.click()

def ss_alma(filename):
    screenshot = pyautogui.screenshot()
    screenshot.save(filename)



def temizle_klasor(klasor_yolu):
    if os.path.exists(klasor_yolu):
        shutil.rmtree(klasor_yolu)  # Klasörü ve içeriğini sil
        os.makedirs(klasor_yolu)  # Klasörü tekrar oluştur


def clean_non_ascii(text):
    return ''.join([i if ord(i) < 128 else ' ' for i in text])

def sendTelegramTextMessage(message_text):
    """
    Telegram'a sadece metin mesajı gönderen fonksiyon
    
    Args:
        message_text (str): Gönderilecek metin mesajı
        
    Returns:
        dict: API yanıtı veya hata durumunda bilgi içeren sözlük
    """
    bot_token = os.getenv('BOT_TOKEN')
    chat_id = os.getenv('CHAT_ID')
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    
    try:
        # ASCII olmayan karakterleri temizle (isteğe bağlı)
        clean_text = clean_non_ascii(message_text)
        
        # Mesajı gönder
        payload = {
            "chat_id": chat_id,
            "text": clean_text,
            "parse_mode": "HTML"  # HTML formatında metin göndermeyi destekler
        }
        
        response = requests.post(url, data=payload)
        return response.json()
        
    except Exception as e:
        print(f"Telegram metin mesaji gonderme hatasi: {e}")
        return {"error": str(e)}
