import pytesseract
from PIL import Image
import json


def extract_text_from_image(image_path):
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    return text


def save_text_as_file(text, output_file_path):
    data = {'text': text}
    with open(output_file_path, 'w') as file:
        json.dump(data, file)


def process_image(image_path, output_file_path):
    text = extract_text_from_image(image_path)
    save_text_as_file(text, output_file_path)
