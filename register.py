from selenium.webdriver.common.by import By  
from utils import click_element 
def register(driver, name, email):

    driver.find_element(By.ID, "fullName").send_keys(name)

    driver.find_element(By.ID, "email-address").send_keys(email)

    driver.find_element(By.ID, "password").send_keys("StrongPassword123")

    driver.find_element(By.ID, "confirm-password").send_keys("StrongPassword123")

    driver.find_element(By.ID, "agree-terms").click()

    click_element(driver, By.XPATH, "//button[@type='submit']")

    try:
        ok_button = click_element(driver,By.CLASS_NAME,"swal2-styled")
        ok_button.click()
    except Exception:
        print("Popup bulunamadı veya otomatik kapandı.")
