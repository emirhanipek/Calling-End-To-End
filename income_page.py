from utils import scrool_bar
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys
from utils import ss_alma
import time
def incomepage(driver):
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="app"]/div/nav/nav/div/div/div[1]/div[2]/div/div/div[1]').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="app"]/div/nav/nav/div/div/div[1]/div[2]/div/div/div[2]/a[2]').click()
    time.sleep(2)
    scrool_bar(driver)

    search_by = driver.find_element(By.XPATH,'//*[@id="search"]')
    search_by.click()
    search_by.send_keys("Emirhan")
    time.sleep(1)
    search_by.send_keys(Keys.ENTER)
    time.sleep(1)
    search_by.clear()

    # driver.find_element(By.XPATH,'//*[@id="app"]/div/main/div/div[2]/div[2]/button').click()
    # time.sleep(1)

    # scrool_bar(driver)
    # time.sleep(1)

    # for zoomin in range(1, 5):
    #     driver.find_element(By.XPATH,'//*[@id="app"]/div/main/div/div[2]/div[2]/div/div/div/div[2]/div[2]/div/button[1]').click()
    #     time.sleep(0.2)

    # time.sleep(1)

    # for zoomout in range(1, 5):
    #     driver.find_element(By.XPATH , '//*[@id="app"]/div/main/div/div[2]/div[2]/div/div/div/div[2]/div[2]/div/button[2]').click()
    #     time.sleep(0.2)


    # time.sleep(1)
    # ss_alma("ss/income_diagram.png")

    # driver.find_element(By.XPATH , '//*[@id="app"]/div/main/div/div[2]/div[2]/div/div/div/div[1]/button/svg//*[@id="app"]/div/main/div/div[2]/div[2]/div/div/div/div[1]/button/svg')

    time.sleep(2)

    ss_alma("ss/income_page.png")
    

    print("İncomePage Giriş Yapıldı")
