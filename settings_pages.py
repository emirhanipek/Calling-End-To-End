

def settings_pages(driver):
    try:
        time.sleep(2)  # Sayfa yüklenmesi için bekleme
        
        # Company Name
        companyName = driver.find_element(By.XPATH, '//*[@id="companyName"]')
        companyName.clear()
        time.sleep(1)
        companyName.send_keys("Emirhan İpek Test 1")
        time.sleep(1)
        click_submit = driver.find_element(By.XPATH, '//*[@id="app"]/div/main/div/form/div[5]/button')
        click_submit.click()
        click_element(driver, By.XPATH, "/html/body/div[7]/div/div[6]/button[1]")
        time.sleep(2)
        
        # Short Name
        shortname = driver.find_element(By.XPATH, '//*[@id="shortName"]')
        shortname.clear()
        time.sleep(1)
        shortname.send_keys("Eİ TEST")
        time.sleep(1)
        click_submit = driver.find_element(By.XPATH, '//*[@id="app"]/div/main/div/form/div[5]/button')
        click_submit.click()
        time.sleep(2)
        click_element(driver, By.XPATH, "/html/body/div[7]/div/div[6]/button[1]")
        
        # Phone
        phone = driver.find_element(By.XPATH, '//*[@id="phone"]')
        phone.clear()
        time.sleep(1)
        phone.send_keys('+905413609917')
        time.sleep(1)
        click_submit = driver.find_element(By.XPATH, '//*[@id="app"]/div/main/div/form/div[5]/button')
        click_submit.click()
        time.sleep(2)
        click_element(driver, By.XPATH, "/html/body/div[7]/div/div[6]/button[1]")
        
        # Email
        email = driver.find_element(By.XPATH, '//*[@id="email"]')
        email.clear()
        time.sleep(1)
        email.send_keys('emirhan.ipek@siriusaitech.com')
        time.sleep(1)
        click_submit = driver.find_element(By.XPATH, '//*[@id="app"]/div/main/div/form/div[5]/button')
        click_submit.click()
        time.sleep(2)
        click_element(driver, By.XPATH, "/html/body/div[7]/div/div[6]/button[1]")
        
        # Address
        address = driver.find_element(By.XPATH, '//*[@id="address"]')
        address.clear()
        time.sleep(1)
        address.send_keys("İSTANBUL ESENYURT")
        time.sleep(1)
        click_submit = driver.find_element(By.XPATH, '//*[@id="app"]/div/main/div/form/div[5]/button')
        click_submit.click()
        time.sleep(2)
        click_element(driver, By.XPATH, "/html/body/div[7]/div/div[6]/button[1]")
        
        # Start Time
        startsAt = driver.find_element(By.XPATH, '//*[@id="startsAt"]')
        startsAt.clear()
        time.sleep(1)
        startsAt.send_keys("09:00")
        time.sleep(1)
        click_submit = driver.find_element(By.XPATH, '//*[@id="app"]/div/main/div/form/div[5]/button')
        click_submit.click()
        time.sleep(2)
        click_element(driver, By.XPATH, "/html/body/div[7]/div/div[6]/button[1]")
        
        # Finish Time
        finishesAt = driver.find_element(By.XPATH, '//*[@id="finishesAt"]')
        finishesAt.clear()
        time.sleep(1)
        finishesAt.send_keys("17:00")
        time.sleep(1)
        click_submit = driver.find_element(By.XPATH, '//*[@id="app"]/div/main/div/form/div[5]/button')
        click_submit.click()
        time.sleep(2)
        click_element(driver, By.XPATH, "/html/body/div[7]/div/div[6]/button[1]")
        
        # About Us
        aboutus = driver.find_element(By.XPATH, '//*[@id="about"]')
        aboutus.clear()
        time.sleep(1)
        aboutus.send_keys("""7/24 Transfer olarak, VIP taşımacılık hizmetlerimizle tüm Türkiye genelinde güvenli, konforlu ve zamanında ulaşım sağlıyoruz. Havalimanlarından başlayarak geniş transfer ağımız sayesinde müşterilerimize en iyi hizmeti sunmayı hedefliyoruz.
        Çalışma saatlerimiz hafta içi 09:00 - 17:30 arasındadır. Geniş araç filomuz ile her türlü transfer ihtiyacınıza cevap verecek kapasitedeyiz. Profesyonel ekibimiz ve deneyimli şoförlerimiz ile müşteri memnuniyetini ön planda tutuyor, her yolculuğunuzda kaliteli bir deneyim sunuyoruz.""")
        time.sleep(1)
        click_submit = driver.find_element(By.XPATH, '//*[@id="app"]/div/main/div/form/div[5]/button')
        click_submit.click()
        time.sleep(2)
        click_element(driver, By.XPATH, "/html/body/div[7]/div/div[6]/button[1]")
        
        # Assistant Name
        assistantName = driver.find_element(By.XPATH, '//*[@id="assistantName"]')
        assistantName.clear()
        time.sleep(1)
        assistantName.send_keys("7/24 Asistan")
        time.sleep(1)
        click_submit = driver.find_element(By.XPATH, '//*[@id="app"]/div/main/div/form/div[5]/button')
        click_submit.click()
        time.sleep(2)
        click_element(driver, By.XPATH, "/html/body/div[7]/div/div[6]/button[1]")

        print("Settings test başarıyla tamamlandı! 🎉")
        
    except Exception as e:
        print(f"Bir hata oluştu: {e}")