import torch
import torchvision.transforms as transforms
from torchvision.models import resnet50
from PIL import Image
import os
import requests
import json
from telegram import Bot
from telegram import InputFile
from dotenv import load_dotenv
import asyncio

# .env dosyasını yükle
load_dotenv()

# Telegram bot token ve chat ID
BOT_TOKEN = os.getenv('BOT_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')

# Telegram botu ile mesaj gönderme fonksiyonu
async def send_telegram_message(image_path, caption):
    bot = Bot(token=BOT_TOKEN)
    with open(image_path, 'rb') as image_file:
        await bot.send_photo(chat_id=CHAT_ID, photo=image_file, caption=caption)

async def yorumla_ve_yazdir(image_folder):
    # Modeli yükle
    model = resnet50(weights='IMAGENET1K_V1')
    model.eval()

    # ImageNet sınıf isimlerini yükle
    LABELS_URL = "https://raw.githubusercontent.com/anishathalye/imagenet-simple-labels/master/imagenet-simple-labels.json"
    response = requests.get(LABELS_URL)
    labels = json.loads(response.text)

    # Klasördeki tüm görselleri al
    image_files = [f for f in os.listdir(image_folder) if f.endswith('.png')]

    # Görselleri yorumla ve sonuçları yazdır
    for img_file in image_files:
        img_path = os.path.join(image_folder, img_file)
        img = Image.open(img_path).convert('RGB')
        
        preprocess = transforms.Compose([
            transforms.Resize(256),
            transforms.CenterCrop(224),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
        ])
        
        img_tensor = preprocess(img)
        img_tensor = img_tensor.unsqueeze(0)
        
        with torch.no_grad():
            preds = model(img_tensor)
        
        # En olası tahminleri al
        _, indices = torch.topk(preds, 3)
        percentages = torch.nn.functional.softmax(preds, dim=1)[0] * 100
        decoded_preds = [(labels[idx], percentages[idx].item()) for idx in indices[0]]
        
        # Özel mesaj ile birlikte sonuçları yazdır
        caption = f"Görsel: {img_file}\n"
        caption += "Bu görsel, Selenium otomasyon testi ile her fonksiyon sonunda alınan bir ekran görüntüsüdür.\n"
        caption += "Bu fotoğraflarda hata var mı? İşte en olası tahminler:\n"
        for label, percentage in decoded_preds:
            caption += f"{label}: {percentage:.2f}%\n"
        caption += "\n"
        
        # Mesajı Telegram botu ile gönder
        await send_telegram_message(img_path, caption)