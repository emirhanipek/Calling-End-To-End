from utils import click_element
from selenium.webdriver.common.by import By  
import time


def login(driver,email):
    driver.find_element(By.ID, "email-address").send_keys(email)
    time.sleep(1)
    driver.find_element(By.ID, "password").send_keys("StrongPassword123")
    time.sleep(1)
    click_element(driver, By.XPATH, "//button[@type='submit']")
    time.sleep(5)