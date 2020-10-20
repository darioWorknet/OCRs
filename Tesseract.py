
from PIL import Image
import pytesseract as tess
import os
# # If you don't have tesseract executable in your PATH, include the following:
tess.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# #If image is in the project folder
# #img = Image.open("Logo-Test.png")  

# #If image is not in the project folder
# img_to_open = r"D:\Google Drive\UPWORK\VBA_to_Python_to_C\ImageFunctions\CD_1.jpg"
# img = Image.open(img_to_open)

#If is needed to convert all files in specified folder
def load_images_from_folder(folder):
    images = []
    for filename in os.listdir(folder):
        try:
            img = Image.open(os.path.join(folder,filename))
            if img is not None:
                images.append(img)
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
    text = tess.image_to_string(img)

    name = extract_name(img.filename)
    print(name)

    new_folder = "Text_from_images"
    filename = folder + "/" + new_folder + "/"+ name + ".txt"

    #Save text as new txt file
    with open(filename, mode = 'w') as f:
        f.write(text)


