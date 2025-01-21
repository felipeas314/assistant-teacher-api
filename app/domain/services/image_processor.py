import pytesseract
from PIL import Image
import cv2
import numpy as np
from io import BytesIO
from transformers import BlipProcessor, BlipForConditionalGeneration

processor = BlipProcessor.from_pretrained("salesforce/blip-image-captioning-large")
model = BlipForConditionalGeneration.from_pretrained("salesforce/blip-image-captioning-large")

async def extract_text_from_image(image_bytes: bytes) -> str:
    image = Image.open(BytesIO(image_bytes))
    return pytesseract.image_to_string(image).strip()

async def caption_image(image_bytes: bytes) -> str:
    print("1")
    """
    Gera uma legenda (caption) em inglês para a imagem, recebendo bytes.
    Usamos o modelo BLIP disponível na Hugging Face 
    ('salesforce/blip-image-captioning-large').
    
    Dependências:
      - transformers, accelerate, torch, Pillow

    Exemplo de uso:
      caption = caption_image(image_bytes)
    """
    print("2")
    # Carregar o processador e o modelo pré-treinado (instanciar uma vez só, se possível)
    processor = BlipProcessor.from_pretrained("salesforce/blip-image-captioning-large")
    model = BlipForConditionalGeneration.from_pretrained("salesforce/blip-image-captioning-large")

    # Se houver GPU:
    # model.to("cuda")
    print("3")
    # Converter bytes em objeto de imagem PIL
    image = Image.open(BytesIO(image_bytes)).convert("RGB")

    # Preparar a entrada para o modelo
    inputs = processor(image, return_tensors="pt")
    # Se usar GPU, suba para CUDA:
    # inputs = {k: v.to("cuda") for k, v in inputs.items()}
    print("4")
    # Gera a legenda
    out = model.generate(**inputs, max_new_tokens=50)
    caption = processor.decode(out[0], skip_special_tokens=True)
    print("5")
    return caption