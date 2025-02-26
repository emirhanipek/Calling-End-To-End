import uuid
import pyautogui
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By  
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

# Tarayıcı başlatma fonksiyonu
def start_driver():
    options = Options()
    options.add_argument("--start-maximized")
    return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Dinamik e-posta ve isim oluşturma fonksiyonu
def generate_random_email_and_name():
    random_name = f"emirhan{uuid.uuid4().hex[:6]}"
    random_email = f"{random_name}@emirtest.com"
    return random_name, random_email

# Screenshot alma fonksiyonu
def take_screenshot(filename):
    screenshot = pyautogui.screenshot()
    screenshot.save(filename)

# Elemente tıklama fonksiyonu
def click_element(driver, by, value):
    element = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((by, value)))
    element.click()

# Formu doldurma fonksiyonu
def fill_form(driver, name, email):
    driver.find_element(By.ID, "fullName").send_keys(name)
    driver.find_element(By.ID, "email-address").send_keys(email)
    driver.find_element(By.ID, "password").send_keys("StrongPassword123")
    driver.find_element(By.ID, "confirm-password").send_keys("StrongPassword123")
    driver.find_element(By.ID, "agree-terms").click()

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

# Şirket bilgilerini doldurma fonksiyonu
def fill_company_info(driver):
    driver.find_element(By.ID, "companyName").clear()
    driver.find_element(By.ID, "companyName").send_keys("Sirius Ai Tech")
    driver.find_element(By.ID, "shortName").clear()
    driver.find_element(By.ID, "shortName").send_keys("Sirius")
    driver.find_element(By.ID, "companyEmail").clear()
    driver.find_element(By.ID, "companyEmail").send_keys("info@info.com")
    driver.find_element(By.ID, "phone").clear()
    driver.find_element(By.ID, "phone").send_keys("+90 541 360 99 17")
    driver.find_element(By.ID, "address").clear()
    driver.find_element(By.ID, "address").send_keys("İstanbul, Türkiye")

    # Logo yükleme input alanını bul
    logo_upload_input = driver.find_element(By.ID, "logo-upload")

    # Dosya yolunu input alanına gönder
    logo_path = "/Users/emirhanipek/Desktop/Testing/ss/kayıtolundu.png"  # Yüklemek istediğiniz dosyanın tam yolu
    logo_upload_input.send_keys(logo_path)


    # Çalışma saatleri

    try:
        driver.find_element(By.ID, "startsAt").send_keys("09:00")
    except hata:
        print("Başlangıc saati girerken hata oluştu")
    finally:
        print("Başlangıc saat girerken başaırılı oluştu")    
    driver.find_element(By.ID, "finishesAt").send_keys("18:00")


    driver.find_element(By.ID, "about").send_keys("Sirius ai tech bir yazılım ve yapay zeka sirketidir bu yazılım ve yapay zeka şirketi hakkında bilgi almak ve denemeleri test etmek icin sorunlarınız bana vereblirisiniz")

    driver.find_element(By.ID, "assistantName").clear()
    driver.find_element(By.ID, "assistantName").send_keys("Aylin")
    # Dil seçimi
    driver.find_element(By.XPATH, "//select[@class='w-full px-3 h-[41px] border border-gray-300 rounded-md text-black bg-transparent']").click()
    driver.find_element(By.XPATH, "//option[@value='en']").click()

    # Sektör seçimi
    driver.find_element(By.CLASS_NAME, "multiselect").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//*[@id='null-2']").click()

    # Input alanına tıklayalım
    input_field = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@class='flex-grow outline-none text-sm text-black bg-transparent']"))
    )

    #  Anahtar kelimeleri sırasıyla girip Enter tuşuna basalım
    keywords = ["keyword1", "keyword2", "keyword3", "keyword4", "keyword5", "keyword6"]
    for keyword in keywords:
        input_field.clear()  # Önceki değeri temizle
        input_field.send_keys(keyword)  # Anahtar kelimeyi gir
        input_field.send_keys(Keys.ENTER)  # Enter tuşuna bas

def call_page():
    print("Giden aramalar test ediliyor")

def incomepage():
    print("İncomePage Giriş Yapıldı")

def guidebooktest():
    print('Rehber Test Ediliyor')


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
# Ana işlem fonksiyonu
def register_user():
    driver = start_driver()
    url = "http://34.69.225.137:5000/"

    try:
        driver.get(url)

        # Kayıt sayfasını aç
        click_element(driver, By.XPATH, "//a[@href='/register']")
        take_screenshot("ss/girisekranı.png")

        # Formu doldur
        name, email = generate_random_email_and_name()
        fill_form(driver, name, email)
        click_element(driver, By.XPATH, "//button[@type='submit']")
        time.sleep(3)

        take_screenshot("ss/kayıtolundu.png")

        # Popup işlemi
        try:
            ok_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CLASS_NAME, "swal2-styled")))
            ok_button.click()
        except Exception:
            print("Popup bulunamadı veya otomatik kapandı.")

        # Şirket bilgilerini doldur
        time.sleep(6)
        fill_company_info(driver)
        time.sleep(4)
        click_element(driver, By.XPATH, "//button[@type='submit']")
        time.sleep(10)

        take_screenshot("ss/adminscreen.png")
        time.sleep(10)
        button = driver.find_element(By.XPATH, "//button[contains(@class, 'text-white') and contains(@class, 'bg-black/100')]")
        button.click()
        time.sleep(10)

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


        driver.find_element(By.ID, "email-address").send_keys(email)
        time.sleep(1)
        driver.find_element(By.ID, "password").send_keys("StrongPassword123")
        time.sleep(1)
        click_element(driver, By.XPATH, "//button[@type='submit']")
        time.sleep(5)
         
        scrool_bar(driver)
        print("Scroll işlemi tamamlandı")
        time.sleep(1)
        #dropdown acıyor
        call_actions = driver.find_element(By.XPATH, '//*[@id="app"]/div/nav/nav/div/div/div[1]/div[2]/div/div/div[1]')
        call_actions.click()
        time.sleep(1)
        income_call = driver.find_element(By.XPATH,'//*[@id="app"]/div/nav/nav/div/div/div[1]/div[2]/div/div/div[2]/a[2]')
        income_call.click() 
        time.sleep(1)
        scrool_bar(driver)
        incomepage()
        print("1")
        time.sleep(1)
        print("2")
        #dropdown acıyor
        call_actions = driver.find_element(By.XPATH, '//*[@id="app"]/div/nav/nav/div/div/div[1]/div[2]/div/div/div[1]')
        print("3")
        call_actions.click()
        print("4")
        time.sleep(1)   
        call = driver.find_element(By.XPATH,'//*[@id="app"]/div/nav/nav/div/div/div[1]/div[2]/div/div/div[2]/a[1]')
        print("5")
        call.click()
        print("6")
        time.sleep(1)
        print("7")
        scrool_bar(driver)
        print("8")
        call_page()
        print("9")
        time.sleep(1)
        print("10")
        guidebook = driver.find_element(By.XPATH,'//*[@id="app"]/div/nav/nav/div/div/div[1]/div[2]/div/a[2]')
        print("11")
        guidebook.click()
        time.sleep(1)
        print("12")
        scrool_bar(driver)
        print("13")
        guidebooktest()
        print("14")
        time.sleep(1)
        print("155")
        settings = driver.find_element(By.XPATH, '//*[@id="app"]/div/nav/nav/div/div/div[1]/div[2]/div/a[3]')
        settings.click()
        time.sleep(1)
        scrool_bar(driver)
        print("16")
        settings_pages(driver)
        print("17")
        time.sleep(1)
        language_button = driver.find_element(By.XPATH, '//*[@id="app"]/div/nav/nav/div/div/div[2]/div/div[1]/div/div[1]')
        language_button.click()
        time.sleep(1)
        language_value = driver.find_element(By.XPATH,'//*[@id="app"]/div/nav/nav/div/div/div[2]/div/div[1]/div/div[2]/ul/li[1]/a')
        language_value.click()


        
    except Exception as e:
        print(f"❌ Genel Hata: {e}")
        take_screenshot("ss/general_error.png")

    finally:
        print("success")
        take_screenshot("ss/işlembaşarılı.png")
        driver.quit()

# Scripti çalıştır
register_user()
