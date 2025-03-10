from utils import click_element, scrool_bar
from selenium.webdriver.common.by import By  
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import datetime
import time
def call_page(driver):
    driver.find_element(By.XPATH , '//*[@id="app"]/div/nav/nav/div/div/div[1]/div[2]/div/div/div[1]').click()
    time.sleep(2)

    driver.find_element(By.XPATH , '//*[@id="app"]/div/nav/nav/div/div/div[1]/div[2]/div/div/div[2]/a[1]').click()
    time.sleep(2)

    search_bar = driver.find_element(By.XPATH , '//*[@id="search"]')
    search_bar.click()
    search_bar.send_keys("emir")
    search_bar.send_keys(Keys.ENTER)

    #dropdown menü
    time.sleep(2)
    driver.find_element(By.XPATH , '//*[@id="app"]/div/main/div/div[2]/div/div[2]/div/div[2]').click()
    driver.find_element(By.XPATH , '//*[@id="status-0"]/span').click()

    date = driver.find_element(By.XPATH , '//*[@id="date"]')
    date.click()
    date.send_keys("01/01/2021")

    time.sleep(2)

    driver.find_element(By.XPATH , '//*[@id="app"]/div/main/div/div[2]/div/div[4]/button').click()
    time.sleep(2)

    name = driver.find_element(By.XPATH , '//*[@id="app"]/div/main/div/div[2]/div/form/div[1]/input')
    name.click()
    today_date = datetime.datetime.now().strftime("%d/%m/%Y")
    name.send_keys(f"emir {today_date}")
    time.sleep(1)

    driver.find_element(By.XPATH , '//*[@id="app"]/div/main/div/div[2]/div/form/div[2]/div/div[2]').click()
    time.sleep(2)
    driver.find_element(By.XPATH , '//*[@id="null-0"]').click()
    time.sleep(2)

    #flowup mesajları
    driver.find_element(By.XPATH , '//*[@id="app"]/div/main/div/div[2]/div/form/div[3]/div/div/div[2]').click()
    time.sleep(2)
    # "sms" seçeneğini seç
    sms_option = driver.find_element(By.XPATH, "//span[contains(text(), 'sms')]")
    sms_option.click()
    time.sleep(2)

    return_call = driver.find_element(By.XPATH , '//*[@id="app"]/div/main/div/div[2]/div/form/div[4]/div[2]/div/input')
    return_call.click()
    return_call.send_keys("1")

    driver.find_element(By.XPATH , '//*[@id="default-checkbox"]').click()
    time.sleep(2)

    call_frequency = driver.find_element(By.XPATH , '//*[@id="app"]/div/main/div/div[2]/div/form/div[5]/div/input')
    call_frequency.click()
    call_frequency.send_keys("1")   

    description = driver.find_element(By.XPATH , '//*[@id="notes"]')
    description.click()
    description.send_keys("Kullanıcının bir ford marka arabası vardır 2021 model en son bakımlarını 3 mart günü yapmıştır.")

    driver.find_element(By.XPATH , '//*[@id="app"]/div/main/div/div[2]/div/form/div[7]/button[2]').click()

    click_element(driver,By.CLASS_NAME,"swal2-styled","call_page_ok_button")

    # konuşmaya tıkla
    div_xpath = f"//div[contains(text(), 'emir {today_date}')]"
    div_element = driver.find_element(By.XPATH, div_xpath)
    div_element.click()

    #follow up mesajıdır.
    followup_button = driver.find_element(By.XPATH , '//*[@id="app"]/div/main/div/div[4]/div[2]/button[1]')
    followup_button.click()

    message_add = driver.find_element(By.XPATH , '//*[@id="app"]/div/main/div/div[4]/div/div[2]/div/div/div/button[2]')
    message_add.click()

    status_add = driver.find_element(By.XPATH , '//*[@id="app"]/div/main/div/div[4]/div/div[2]/div/table/tbody/tr/td[1]/div/div[2]')
    status_add.click()

    status_add_element = driver.find_element(By.XPATH , '//*[@id="null-2"]')
    status_add_element.click()  

    message_text = driver.find_element(By.XPATH , '//*[@id="app"]/div/main/div/div[4]/div/div[2]/div/table/tbody/tr/td[2]/div/div[2]')
    message_text.send_keys("Bu bir follow-up mesajıdır")  

    driver.find_element(By.XPATH , '//*[@id="app"]/div/main/div/div[4]/div/div[2]/div/table/tbody/tr/td[3]/button[1]').click()

    message_add.click()

    status_add = driver.find_element(By.XPATH , '//*[@id="app"]/div/main/div/div[4]/div/div[2]/div/table/tbody/tr/td[1]/div/div[2]')
    status_add.click()

    status_add_element = driver.find_element(By.XPATH , '//*[@id="null-1"]')
    status_add_element.click()  

    message_text = driver.find_element(By.XPATH , 'Bu bir follow-up mesajıdır')

    driver.find_element(By.XPATH , '//*[@id="app"]/div/main/div/div[4]/div/div[2]/div/table/tbody/tr[2]/td[3]/button[2]').click()

    driver.find_element(By.XPATH , '//*[@id="app"]/div/main/div/div[4]/div/div[2]/div/table/tbody/tr/td[3]/button[2]')

    ok_button = WebDriverWait(driver, 8).until(EC.element_to_be_clickable((By.CLASS_NAME, "swal2-confirm")))
    ok_button.click()

    yapay_zeka_oluştur = driver.find_element(By.XPATH , '//*[@id="app"]/div/main/div/div[4]/div/div[2]/div/div/div/button[1]')
    yapay_zeka_oluştur.click()

    time.sleep(50)

    close_followup = driver.find_element(By.XPATH , '//*[@id="app"]/div/main/div/div[4]/div/div[3]/div[2]/button[2]')
    close_followup.click()

    #sohbet mesajı oluştur
    chat_add = driver.find_element(By.XPATH , '//*[@id="app"]/div/main/div/div[4]/div[2]/button[2]')
    chat_add.click()

    yapay_zeka_button = driver.find_element(By.XPATH , '//*[@id="app"]/div/main/div/div[3]/div/div/div[2]/div/div/div/button[1]')
    yapay_zeka_button.click()

    konu_message = driver.find_element(By.XPATH , '//*[@id="app"]/div/main/div/div[3]/div[1]/div/form/div[1]/textarea')
    konu_message.send_keys("Müşterimize abonelik yenileme teklifinde bulunacağız. Geçmiş faturalar ve kullanım analizleri doğrultusunda kişiye özel kampanyalar sunarak ikna etmeye çalışacağız.")

    driver.find_element(By.XPATH , '//*[@id="app"]/div/main/div/div[3]/div[1]/div/form/div[2]/button[2]').click()
    time.sleep(15)

    success = WebDriverWait(driver, 8).until(EC.element_to_be_clickable((By.CLASS_NAME, "swal2-confirm")))
    success.click()

    scrool_bar(driver)

    chat_follow_close = driver.find_element(By.XPATH , '//*[@id="app"]/div/main/div/div[3]/div/div/div[1]/button')
    chat_follow_close.click()

    #customer add

    customer_add = driver.find_element(By.XPATH , '//*[@id="app"]/div/main/div/div[4]/button[2]')
    customer_add.click()

    customer_select = driver.find_element(By.XPATH , '//*[@id="app"]/div/main/div/div[3]/div/form/div[1]/div/div[2]')
    customer_select.send_keys("emir ipek")
    customer_select.send_keys(Keys.RETURN)

    customer_info = driver.find_element(By.XPATH , '//*[@id="note"]')
    customer_info.send_keys("Müşterimizin abonelik süresi dolmak üzere. Müşterimizle iletişime geçerek abonelik süresini uzatmaya çalışacağız. ")
    
    driver.find_element(By.XPATH , '//*[@id="app"]/div/main/div/div[3]/div/form/div[3]/button[2]').click()

    customer_add_success = WebDriverWait(driver, 8).until(EC.element_to_be_clickable((By.CLASS_NAME, "swal2-confirm")))
    customer_add_success.click()

    print("Giden Arama Sayfası Görüntülendi")
    time.sleep(2)

