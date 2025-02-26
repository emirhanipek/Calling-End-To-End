from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def smooth_scroll():
    try:
        # Chrome driver'ı başlat
        driver = webdriver.Chrome()
        
        # Pencereyi maximize et
        driver.maximize_window()
        
        # Siteye git
        driver.get("https://www.browserstack.com/guide/selenium-scroll-tutorial")
        
        # Sayfanın yüklenmesini bekle
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )
        
        print("Sayfa yüklendi, aşağı scroll yapılıyor...")
        
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
        
        print("Scroll işlemi tamamlandı")
        
    except Exception as e:
        print(f"Bir hata oluştu: {str(e)}")
        
    finally:
        # Tarayıcıyı kapat
        driver.quit()

# Fonksiyonu çalıştır
if __name__ == "__main__":
    smooth_scroll()