# Proje Kurulum Kılavuzu

Bu proje, belirli bağımlılıkları olan bir Python uygulamasıdır. Aşağıdaki adımları takip ederek projeyi kurabilir ve çalıştırabilirsiniz.

## 1. Sanal Makine (Virtual Environment) Oluşturma

Öncelikle, bağımlılıkları izole etmek için bir sanal makine oluşturun:
```bash
python3 -m venv myenv
```

## 2. Sanal Makineyi Aktifleştirme

**MacOS/Linux:**
```bash
source myenv/bin/activate
```

**Windows:**
```bash
myenv\Scripts\activate
```

## 3. Gerekli Paketleri Yükleme

Tüm bağımlılıkları içeren `requirements.txt` dosyasını yüklemek için:
```bash
pip install -r requirements.txt
```

Eğer `requirements.txt` dosyası eksikse veya belirli paketleri elle yüklemek isterseniz, aşağıdaki komutları kullanabilirsiniz:
```bash
pip install openai
pip install pytesseract
pip install fpdf
pip install unidecode
```

## 4. Ortam Değişkenleri (ENV Dosyası)

Projenin düzgün çalışabilmesi için `.env` dosyasını oluşturmanız ve ilgili ortam değişkenlerini tanımlamanız gerekmektedir. Örnek bir `.env` dosyası:
```env
API_KEY=your_api_key_here
SECRET_KEY=your_secret_key_here
```

Bu dosyanın `.gitignore` içinde olduğundan emin olun, böylece hassas bilgiler GitHub’a yüklenmez.

## 5. Uygulamayı Çalıştırma

Tüm bağımlılıklar yüklendikten sonra, uygulamayı şu şekilde çalıştırabilirsiniz:
```bash
python main.py
```

## 6. Sanal Ortamdan Çıkış Yapma

Eğer sanal ortamdan çıkmak isterseniz, şu komutu kullanabilirsiniz:
```bash
deactivate
```

