from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def logout(driver):
    # Çıkış yap
    driver.find_element(By.XPATH, "//*[@class='bg-transparent ml-4 hover:border-0 ring-0 focus:border-0 py-0 px-1 border-0 text-sm text-black text-opacity-50 hover:text-opacity-90']").click()
    try:
        ok_button = WebDriverWait(driver, 8).until(EC.element_to_be_clickable((By.CLASS_NAME, "swal2-confirm")))
        ok_button.click()
        print("Popup bulundu ve kapatıldı")
    except Exception:
        print("Popup bulunamadı veya otomatik kapandı.")

    try:
        ok_button = WebDriverWait(driver, 8).until(EC.element_to_be_clickable((By.CLASS_NAME, "swal2-confirm")))
        ok_button.click()
        print("Popup bulundu ve kapatıldı")
    except Exception:
        print("Popup bulunamadı veya otomatik kapandı.")
