from PIL import Image
import cv2
import numpy as np
import requests
import io
import json
import os


def extract_text(file):
    img = cv2.imread(file)

    _, compressedimage = cv2.imencode(".jpg", img, [1, 90])
    file_bytes = io.BytesIO(compressedimage)

    url_api = "https://api.ocr.space/parse/image"

    result = requests.post(url_api,
                files = {file: file_bytes},
                data = {"apikey": "551ce5581588957",
                        "language": "eng",
                        "OCREngine": "2",
                        "detectOrientation": "true"})

    result = result.content.decode()
    result = json.loads(result)

    print (result)

    parsed_results = result.get("ParsedResults")[0]
    text_detected = parsed_results.get("ParsedText")
    print(text_detected)

    return text_detected


def load_images_from_folder(folder):
    images = []
    for filename in os.listdir(folder):
        try:
            img = Image.open(os.path.join(folder,filename))
            if img is not None:
                images.append(img.filename)
        except:
            print ("not image")
    return images


def extract_name (filename):
    head, tail = os.path.split(filename)
    name = os.path.splitext(tail)[0]
    return name


folder = r"D:\Google Drive\UPWORK\VBA_to_Python_to_C\ImageFunctions"
images = load_images_from_folder (folder)

for img in images:
    text = extract_text(img)

    name = extract_name(img)
    print(name)

    new_folder = "API_text"
    filename = folder + "/" + new_folder + "/"+ name + ".txt"

    #Save text as new txt file
    with open(filename, mode = 'w') as f:
        f.write(text)


