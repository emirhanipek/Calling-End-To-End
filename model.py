import os
import openai
from PIL import Image
import pytesseract
from fpdf import FPDF
import requests
from dotenv import load_dotenv
import asyncio
from datetime import date
import re
from unidecode import unidecode

def clean_non_ascii(text):
    return unidecode(text)

class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 12)
        self.cell(0, 20, "Call End-to-End Test Raporu", align="C", ln=True)

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 8)
        self.cell(0, 10, f"Sayfa {self.page_no()}", align="C")
    
    # Güvenli metin yazdırma metodu
    def safe_cell(self, w, h, txt='', border=0, ln=0, align='', fill=False, link=''):
        # Metni ASCII karakterlere dönüştür
        safe_txt = clean_non_ascii(txt)
        self.cell(w, h, safe_txt, border, ln, align, fill, link)
        
    def safe_multi_cell(self, w, h, txt='', border=0, align='', fill=False):
        # Metni ASCII karakterlere dönüştür
        safe_txt = clean_non_ascii(txt)
        self.multi_cell(w, h, safe_txt, border, align, fill)

def analyze_image(image_path):
    try:
        # Görseldaki metni al
        text = pytesseract.image_to_string(Image.open(image_path))
        
        # ASCII olmayan karakterleri temizle
        text = clean_non_ascii(text)
        
        # OpenAI API isteği yap
        client = openai.OpenAI()
        response = client.chat.completions.create(
            model="gpt-4o",  # Güncel model kullan
            messages=[
                {"role": "system", "content": clean_non_ascii("""
                Bir test uzmanısın ve bir uygulamanın uçtan uca (end-to-end) testlerini yazıyorsun.
                Belirli bölgelerde ekran görüntüleri (screenshot) aldın. Bu ekran görüntülerini yorumlamanı istiyorum.
                Detaylı bir analiz yapmana gerek yok, sadece testin durumunu değerlendir. Eğer bir hata,
                eksik yüklenen veri, veya başarısızlık (fail) varsa belirt. Eğer her şey sorunsuz çalışıyorsa
                'Geçti' şeklinde özetle.
                """)},       
                {"role": "user", "content": f"Bu görseldaki metin: {text}\nBu gorseli analiz et ve modern bir şekilde rapor et.Ve en sonunda gecti mi kaldı diye bir yorum yaz."}
            ],
            max_tokens=300
        )
        
        # Yanıtı ASCII karakterlere dönüştür - DÜZELTİLDİ
        return clean_non_ascii(response.choices[0].message.content.strip())
    
    except Exception as e:
        return f"Hata: {str(e)}"
def create_pdf(image_folder, output_pdf):
    pdf = PDF()
    pdf.add_page()
    pdf.set_font("Arial", "B", 16)
    pdf.safe_cell(0, 10, "Gorsel Analiz Raporu", ln=True, align='C')
    pdf.set_font("Arial", size=12)
    pdf.safe_cell(0, 10, f"Tarih: {date.today().strftime('%d.%m.%Y')}", ln=True)
    pdf.ln(5)

    # Klasördeki her görsel için
    for image_file in os.listdir(image_folder):
        if image_file.endswith(('.png', '.jpg', '.jpeg')):
            image_path = os.path.join(image_folder, image_file)
            analysis = analyze_image(image_path)

            pdf.add_page()
            pdf.set_font("Arial", "B", 14)
            pdf.safe_cell(0, 10, f"Gorsel: {image_file}", ln=True)
            pdf.ln(5)
            
            # Görsel ekle
            try:
                img_width = 180
                img = Image.open(image_path)
                width_ratio = img_width / img.width
                img_height = img.height * width_ratio
                pdf.image(image_path, x=25, y=40, w=img_width)
                
                # Analiz metni için yeterli boşluk bırak
                pdf.ln(img_height + 20)
            except Exception as e:
                pdf.ln(10)
                pdf.safe_cell(0, 10, f"Gorsel yuklenemedi: {str(e)}", ln=True)
                pdf.ln(10)
            
            pdf.set_font("Arial", "B", 8)
            pdf.safe_cell(0, 10, "Analiz:", ln=True)
            pdf.set_font("Arial", size=8)
            pdf.safe_multi_cell(0, 10, analysis)
            
    # PDF'i kaydet
    pdf.output(output_pdf)

def sendTelegramMessage(file_path):
    bot_token = os.getenv('BOT_TOKEN')
    chat_id = os.getenv('CHAT_ID')
    url = f"https://api.telegram.org/bot{bot_token}/sendDocument"
    
    try:
        with open(file_path, 'rb') as file:
            response = requests.post(url, data={"chat_id": chat_id}, files={"document": file})
        return response.json()
    except Exception as e:
        print(f"Telegram mesaj gonderme hatasi: {e}")
        return {"error": str(e)}

# Asenkron fonksiyon
async def yorumla_ve_yazdir(image_folder):
    try:
        print("PDF olusturuluyor...")
        output_pdf = "call_e2e_test_raporu.pdf"
        create_pdf(image_folder, output_pdf)
        
        print("Telegram'a gonderiliyor...")
        response = sendTelegramMessage(output_pdf)
        print("Islem tamamlandi.")
        return response
    except Exception as e:
        print(f"Islem sirasinda hata: {e}")
        return {"error": str(e)}

if __name__ == "__main__":
    load_dotenv()
    openai.api_key = os.getenv('  ')
    image_folder = "ss"
    output_pdf = "reports/call_e2e_test_raporu.pdf"

    try:
        create_pdf(image_folder, output_pdf)
        response = sendTelegramMessage(output_pdf)
        print("Rapor gonderildi:", response)
    except Exception as e:
        print(f"Hata olustu: {e}")